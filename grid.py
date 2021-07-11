import math
import pandas as pd
import numpy as np
import psutil
import platform
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
    #print(int(positive_number_each_portion))
    #print(int(negative_number_each_portion))
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

# 3 ways to calculate AUC
# def calculate_valuation_AUC(k,portion_array):
#     entire_dataset = pd.DataFrame()
#     for i in range(k):
#         entire_dataset=pd.concat([entire_dataset, portion_array[i]])
#     grid_search_dt,begin,end,cpu_information=DTM_classifier(entire_dataset)
#     return grid_search_dt.cv_results_,begin,end,cpu_information

def calculate_downlevel_AUC(k,portion_array,flag):
    y_pred_entire= pd.DataFrame()
    cv_results_down= []
    validation_array={}
    for i in range(k):
        validation_dataset = pd.DataFrame()
        validation_dataset = pd.concat([validation_dataset, portion_array[i]])
        new_dataset = pd.DataFrame()
        for j in range(k):
            if j != i:
                new_dataset=pd.concat([new_dataset, portion_array[j]])

        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        grid_search_dt,begin,end,cpu_information,validation_auc,validation_f1=DTM_classifier(new_dataset,validation_dataset)

        cv_results_down.append(grid_search_dt.cv_results_)
        validation_array.append(validation_auc)
        #print(grid_search_dt.cv_results_['mean_test_score'])
    return cv_results_down,begin,end,cpu_information,validation_array

#def calculate_combined_AUC(entire_dataset):






    #for i in range

    # print(len(grid_search_dt.cv_results_['params']))
    # print(grid_search_dt.cv_results_['split0_test_score'])




def DTM_classifier(new_dataset,validation_dataset):
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
                                  scoring=scoring, refit='AUC',
                                  return_train_score=True,
                                  cv=5,
                                  n_jobs=-1
                                  )
    begin = datetime.now()
    grid_search_dt.fit(X, np.ravel(y))
    end = datetime.now()
    y_pred_proba = grid_search_dt.predict_proba(X_validation)[:, 1]
    y_pred = grid_search_dt.predict(X_validation)
    validation_auc = roc_auc_score(y_validation, y_pred_proba)
    print(validation_auc)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    validation_f1 = f1_score (y_validation, y_pred)
    cpu_information = record_cpu_information()
    print("begin" + str(begin))
    print("end:" + str(end))
    return grid_search_dt,begin,end,cpu_information,validation_auc,validation_f1

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
    cpu_information['mean_core_percent_usage'] = str(sum(cpu_information['each_core_percentage'])/Number_of_Cores_Used)+'%'
    #cpu_percentage.append(str(f"Total CPU Usage: {psutil.cpu_percent()}%"))
    return cpu_information


def format_output(cvresult_down, k, table, outcome, begin, end, cpu_information, validation_array):
    # cpu_information = record_cpu_information()
    result_array = []
    combinations_number = len(cvresult_down[0]['params'])
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
        # different way to calculate AUC will generate different mean_fit_time
        # result['mean_fit_time'] =
        # result['std_fit_time'] =
        # result['mean_score_time'] =
        # result['std_score_time'] =
        result['parameters_and_values'] = cvresult_down[0]['params'][i]
        # split[0:5]
        result['split_random_seed'] = 7
        result['mean_test_auc'] = []
        result['std_test_auc'] = []
        result['rank_test_auc'] = []
        result['combined_test_auc'] = []  # not finish
        result['mean_train_auc'] = []
        result['std_train_auc'] = []

        result['validation_auc'] = []
        result['rank_validation_auc'] = []
        result['test_validation_avg'] = []
        result['rank_test_validation'] = []
        result['validation_f1'] = []
        result['rank_validation_f1'] = []

        for j in range(k):
            result['mean_test_auc'].append(cvresult_down[j]['mean_test_AUC'][i])
            result['std_test_auc'].append(cvresult_down[j]['std_test_AUC'][i])
            result['rank_test_auc'].append(cvresult_down[j]['rank_test_AUC'][i])
            result['mean_train_auc'].append(cvresult_down[j]['mean_train_AUC'][i])
            result['std_train_auc'].append(cvresult_down[j]['std_train_AUC'][i])

        result_array.append(result)
    return result_array[0:10]

def main(table,k,flag,Outcome):
    portion_array = splitDataset(table,k)
    cv_result_down,begin,end,cpu_information,validation_array = calculate_downlevel_AUC(k,portion_array,flag)
    #cv_result_top,begin,end,cpu_information = calculate_toplevel_AUC(k,portion_array)
    #print(cv_result_top)
    print(cv_result_down[0])
    result = format_output(cv_result_down,k,table,Outcome,begin,end,cpu_information,validation_array)
    return result


k = 5
flag = 1
table = "\LSDBDistantRecurrenceNotreatment_5Year_NoDays_Digital.txt"
outcome = 'distant_recurrence'
print(main(table,k,flag,outcome))
#def newdataset_split():

