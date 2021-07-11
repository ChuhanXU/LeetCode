import csv
import pandas as pd
import numpy as np
import psutil
from statistics import mean
from numpy import std
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedShuffleSplit
from time import time
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from datetime import datetime
from sklearn.metrics import make_scorer
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score

# split the entire dataset into k portions and make sure 20% positive and 20% negative in each portion
# table : tablename
# k : the number of portions
def splitDataset(table,k):
    dataset = pd.read_table(
        "..\dataset\Original\DistantRecurrence"+str(table),
        delim_whitespace=True)
    #print(dataset['distant_recurrence'].value_counts())
    negative_dataset = dataset.loc[dataset['distant_recurrence'] == 0]
    positive_dataset = dataset.loc[dataset['distant_recurrence'] == 1]
    negative_number_each_portion = int(negative_dataset.shape[0]/k)

    positive_number_each_portion = int(int(negative_dataset.shape[0]/k)/0.8)-int(negative_dataset.shape[0]/k)
    print(int(positive_number_each_portion))
    print(int(negative_number_each_portion))
    # print(negative_dataset)
    # print(positive_dataset)
    # print(dataset)
    #
    # all portions will be stored in portion_array
    portion_array=[]
    for i in range (0,dataset.shape[0],negative_number_each_portion+1):
        # randomly select 750 rows data from negative set or divide the data set into 5 equal portion (randomly select or evenly select)
        # even
        #negative_each_portion = negative_dataset[i:i+negative_number_each_portion]
        #random
        negative_each_portion = negative_dataset.sample(negative_number_each_portion)
        # randomly select positive data rows
        positive_each_portion = positive_dataset.sample(positive_number_each_portion)
        portion = pd.concat([negative_each_portion, positive_each_portion])
        portion_array.append(portion)

    return portion_array


def calculate_downlevel_AUC(k,portion_array,flag):
    y_pred_entire= pd.DataFrame()
    cv_results_down= []
    validation_array=[]
    parameter_combined_pred={}
    begin = datetime.now()
    for i in range(k):
        y_pred_entire=pd.concat([y_pred_entire,pd.DataFrame(portion_array[i]['distant_recurrence'])])
        validation_dataset = pd.DataFrame()
        validation_dataset = pd.concat([validation_dataset, portion_array[i]])
        new_dataset = pd.DataFrame()
        for j in range(k):
            if j != i:
                new_dataset=pd.concat([new_dataset, portion_array[j]])


        grid_search_dt,cpu_information,validation_hash,parameter_combined_pred=DTM_classifier(new_dataset,validation_dataset,parameter_combined_pred)
        cv_results_down.append(grid_search_dt.cv_results_)
        validation_array.append(validation_hash)
    #str = "{'criterion': 'entropy', 'max_depth': 50, 'splitter': 'random'}"
    #print(y_pred_entire)
    combined_validation_auc = []
    for pred_combined in list(parameter_combined_pred.values()):
        combined_validation_auc.append(roc_auc_score(y_pred_entire, pred_combined))
    end = datetime.now()
    #print(combined_validation_auc)

    #print(grid_search_dt.cv_results_['mean_test_score'])
    return cv_results_down,begin,end,cpu_information,validation_array,combined_validation_auc

# Function to replace each element of the list by its rank in the list
def transform(arr):
    sorted_list = sorted(arr,reverse=True)
    rank = 1
    sorted_rank_list = [1]
    for i in range(1, len(sorted_list)):
        if sorted_list[i] != sorted_list[i - 1]:
            rank += 1
        sorted_rank_list.append(rank)

    rank_list = []
    # zip function returns iterator of tuple pairs of matching values in two inputss
    # dict function casts 1nd value in tuple as key and 2nd value in tuple as value
    item_rank_dict = dict(zip(sorted_list, sorted_rank_list))

    for item in arr:
        item_rank = item_rank_dict[item]
        rank_list.append(item_rank)
    return rank_list



def DTM_classifier(new_dataset,validation_dataset,parameter_combined_pred):
    seed = 7
    #test_size = 0.2
    #print(new_dataset['distant_recurrence'].value_counts())
    X = new_dataset.iloc[:,:-1]
    y = new_dataset.iloc[:,-1:]
    X_validation = validation_dataset.iloc[:,:-1]
    y_validation = validation_dataset.iloc[:,-1:]

    scoring = {'AUC': 'roc_auc', 'f1': make_scorer(f1_score)}
    model = DecisionTreeClassifier(random_state=seed)
    parameters = [{'criterion': ['gini', 'entropy'],
                   'splitter': ['best', 'random'],
                   'max_depth': [4, 5, 6, 10, 50],
                   # 'max_features':['auto','sqrt','log2','None']
                   }]
    grid_search_dt = GridSearchCV(estimator=model,
                                  param_grid=parameters,
                                  scoring=scoring,
                                  refit='AUC',
                                  return_train_score=True,
                                  cv=5,
                                  n_jobs=-1
                                  )

    grid_search_dt.fit(X, np.ravel(y))

    validation_hash= {}
    validation_hash['validation_auc']=[]
    validation_hash['validation_f1']=[]
    validation_hash['rank_validation_auc']=[]
    validation_hash['index_rank_validation_f1']=[]


    for parameter_set in grid_search_dt.cv_results_['params']:
        model = DecisionTreeClassifier(criterion=parameter_set['criterion'],max_depth=parameter_set['max_depth'],splitter=parameter_set['splitter'])
        model.fit(X,y)
        y_pred_proba = model.predict_proba(X_validation)[:, 1]
        y_pred = model.predict(X_validation)
        if str(parameter_set) not in parameter_combined_pred:
            parameter_combined_pred[str(parameter_set)] = pd.DataFrame()
            parameter_combined_pred[str(parameter_set)] = pd.concat([parameter_combined_pred[str(parameter_set)],pd.DataFrame(y_pred_proba)])
        else:
            parameter_combined_pred[str(parameter_set)] = pd.concat(
                [parameter_combined_pred[str(parameter_set)], pd.DataFrame(y_pred_proba)])
        validation_auc = roc_auc_score(y_validation, y_pred_proba)
        validation_f1 = f1_score(y_validation, y_pred)
        validation_hash['validation_auc'].append(validation_auc)
        validation_hash['validation_f1'].append(validation_f1)
    rank_validation_auc = transform(validation_hash['validation_auc'])
    index_rank_validation_f1 = transform(validation_hash['validation_f1'])
    validation_hash['rank_validation_auc'] = rank_validation_auc
    validation_hash['index_rank_validation_f1'] = index_rank_validation_f1
    cpu_information = record_cpu_information()
    return grid_search_dt,cpu_information,validation_hash,parameter_combined_pred

    # print(entire_dataset)
    # print(entire_dataset['distant_recurrence'].value_counts())

def record_cpu_information():
    Number_of_Cores_Used = 0
    cpu_information = {}
    cpu_information['each_core_percentage']=[]

    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        cpu_information['each_core_percentage'].append(int(percentage))
        if percentage != 0:
            Number_of_Cores_Used+=1
    cpu_information['number_of_cores_used'] = Number_of_Cores_Used
    if Number_of_Cores_Used == 0:
        cpu_information['mean_core_percent_usage']='0'

    else:
        cpu_information['mean_core_percent_usage'] = str(sum(cpu_information['each_core_percentage'])/Number_of_Cores_Used)+'%'
    #cpu_percentage.append(str(f"Total CPU Usage: {psutil.cpu_percent()}%"))
    return cpu_information


def format_output(cvresult_down, k, table, outcome, begin, end, cpu_information, validation_array,combined_validation_auc):
    #print(validation_array)
    # cpu_information = record_cpu_information()
    result_array = []
    combinations_number = len(cvresult_down[0]['params'])
    #in order to rank them i need to store 20 mean_validations
    mean_validation_array = []
    mean_of_all_means_array = []
    mean_validation_f1_array = []
    mean_test_validation_array=[]
    for i in range(combinations_number):
        result = {}
        result['experiment_id'] = i
        result['ml_classifier_name'] = 'Decision Tree'
        result['implementation_language'] = 'Python 3.8.5 '
        result['full_dataset_name'] = table
        result['outcome_type'] = outcome
        result[
            'app_file_path'] = 'chx37\PycharmProjects\ProjectW81XWH1910495-stage1\dataset\Original\DistantRecurrence' + str(
            table)
        result['host'] = '130.49.206.141'
        result['compute_manufacture'] = 'To Be Filled By O.E.M.'
        result['computer_name'] = 'xij6-lab1-dt.univ.pitt.edu'
        result['os'] = 'Microsoft Windows 10 Enterprise 2016 LSTB'
        result['system_type'] = 'x64-based PC'
        result['cpu_gpu'] = 'cpu'
        result[
            'cpu_gpu_model'] = 'cpu:Intel(R)Core(TM)i7-4790K CPU @ 4.00GHz, 4001 Mhz, 4 Core(s), 8 Logical Processor(s); gpu:NVIDIA Quadro K2200'
        result['processing_unit_speed'] = '4.00GHz'
        result['ram'] = '32768MB RAM'
        # we can't get specific cpu_information for every experiment, we can get cpu information for different way to calculate AUC
        result['number_of_cores_used'] = cpu_information['number_of_cores_used']
        result['mean_core_percent_usage'] = cpu_information['mean_core_percent_usage']
        # we can't get start_date_time for every experiment, the start_time will the start_time of one grid search including all combinations of parameters
        result['start_date_time'] = begin
        result['end_date_time'] = end
        # the running_time is the time to run one time gridsearch including all parameters combination
        # the mean_fit_time is the time to run one experiment including one set of parameter,can we use mean_fit_time to represent running time
        result['running _time'] = str(end - begin)[:-3]

        result['mean_fit_time'] = []
        result['std_fit_time'] = []
        result['mean_score_time'] = []
        result['std_score_time'] =[]
        result['parameters_and_values'] = cvresult_down[0]['params'][i]
        # split[0:5]
        result['split_random_seed'] = 7
        result['mean_validation_auc'] = []
        result['std_validation_auc'] = []
        result['rank_mean_validation_auc'] = []
        result['mean_of_all_means'] = []
        result['std_of_all_means'] = []
        result['rank_mean_of_all_means'] = []
        result['combined_validation_auc'] = combined_validation_auc[i]
        result['mean_validation_f1'] = []
        result['std_validation_f1'] = []
        result['rank_validation_f1'] = []

        #array
        result['i_split_random_seed'] = [7,7,7,7,7]
        result['mean_test_auc'] = []
        result['std_test_auc'] = []
        result['rank_test_auc'] = []
        result['combined_test_auc'] = [0,0,0,0,0]  # not finish
        result['mean_train_auc'] = []
        result['std_train_auc'] = []
        result['validation_auc'] = []
        result['rank_validation_auc'] = []
        result['test_validation_avg'] = []
        result['rank_test_validation'] = []
        result['validation_f1'] = []
        result['index_rank_validation_f1'] = []



        for j in range(k):
            result['mean_test_auc'].append(cvresult_down[j]['mean_test_AUC'][i])
            result['std_test_auc'].append(cvresult_down[j]['std_test_AUC'][i])
            result['rank_test_auc'].append(cvresult_down[j]['rank_test_AUC'][i])
            result['mean_train_auc'].append(cvresult_down[j]['mean_train_AUC'][i])
            result['std_train_auc'].append(cvresult_down[j]['std_train_AUC'][i])
            result['mean_fit_time'].append(cvresult_down[j]['mean_fit_time'][i])
            result['std_fit_time'].append(cvresult_down[j]['std_fit_time'][i])
            result['mean_score_time'].append(cvresult_down[j]['mean_score_time'][i])
            result['std_score_time'].append(cvresult_down[j]['std_score_time'][i])

        for element in validation_array:
            result['validation_auc'].append(element['validation_auc'][i])
            result['rank_validation_auc'].append(element['rank_validation_auc'][i])
            result['validation_f1'].append(element['validation_f1'][i])
            result['index_rank_validation_f1'].append(element['index_rank_validation_f1'][i])


        for j in range(k):
            test_validation=[result['mean_test_auc'][j],result['validation_auc'][j]]
            result['test_validation_avg'].append(mean(test_validation))
        mean_test_validation_array.append(result['test_validation_avg'])# 20 arrays

        result['mean_validation_auc'] = mean(result['validation_auc'])
        result['std_validation_auc'] = std(result['validation_auc'])
        result['mean_of_all_means']=mean(result['mean_test_auc'])
        result['std_of_all_means']=std(result['mean_test_auc'])
        result['mean_validation_f1'] = mean(result['validation_f1'])
        result['std_validation_f1'] = std(result['validation_f1'])
        result['mean_fit_time']=mean(result['mean_fit_time'])
        result['std_fit_time']=std(result['std_fit_time'])
        result['mean_score_time']=mean(result['mean_score_time'])
        result['std_score_time']=std(result['std_score_time'])
        # record the mean value for rank
        mean_validation_array.append(result['mean_validation_auc'])
        mean_of_all_means_array.append(result['mean_of_all_means'])
        mean_validation_f1_array.append(result['mean_validation_f1'])
        result_array.append(result)

    rank_mean_validation_array = transform(mean_validation_array)
    rank_mean_of_all_means_array= transform(mean_of_all_means_array)
    rank_mean_validation_f1_array= transform(mean_validation_f1_array)

    fold_array = [[],[],[],[],[]]#5 array in fold_array, each array contains 20 average
    rank_array = []#5 array in fold_array, each array contains 20 average
    for i in range(k):
        for j in range(combinations_number):
            fold_array[i].append(mean_test_validation_array[j][i])
        rank_fold_array = transform(fold_array[i])
        rank_array.append(rank_fold_array)
    #print(rank_array)


    for i in range(combinations_number):
        result_array[i]['rank_mean_validation_auc']=rank_mean_validation_array[i]
        result_array[i]['rank_mean_of_all_means'] = rank_mean_of_all_means_array[i]
        result_array[i]['rank_validation_f1'] = rank_mean_validation_f1_array[i]
        result_array[i]['rank_test_validation'] = []

        for j in range(k):
            result_array[i]['rank_test_validation'].append(rank_array[j][i])

    return result_array

def output(record,k):
    values = list(record.values())
    list_value = []
    for i in range(36):
        list_value.append(values[i])
    for j in range(k):
        for i in range(36,len(values),1):
            list_value.append(values[i][j])
    return list_value
file_name = '..\Results.csv'

def data_write_csv(file_name, datas):
    with open(file_name, 'a+',newline='') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        # writing the data rows
        csvwriter.writerow('')
        print("hello")
        csvwriter.writerows(datas)


def main(table,k,flag,Outcome):
    portion_array = splitDataset(table,k)
    cv_result_down,begin,end,cpu_information,validation_array,combined_validation_auc = calculate_downlevel_AUC(k,portion_array,flag)
    result_array= format_output(cv_result_down,k,table,Outcome,begin,end,cpu_information,validation_array,combined_validation_auc)
    datas =[]
    for record in result_array:
        print(record)
        final_record=output(record,k)
        datas.append(final_record)

    #data_write_csv(file_name, datas)
    print("saved successfully")

k = 5
flag = 1
table = "\LSDBDistantRecurrenceNotreatment_5Year_NoDays_Digital.txt"
outcome = 'distant_recurrence'
print(main(table,k,flag,outcome))
