import pandas as pd
from sklearn.utils import shuffle
def splitDataset(table,k):
    dataset = pd.read_table(
        "..\dataset\Original"+str(table),
        delim_whitespace=True)
    #print(dataset['distant_recurrence'].value_counts())
    negative_dataset = dataset.loc[dataset[list(dataset.columns.values)[-1]] == 0]
    positive_dataset = dataset.loc[dataset[list(dataset.columns.values)[-1]] == 1]
    positive_dataset_shape = positive_dataset.shape[0]
    negative_dataset_shape = negative_dataset.shape[0]
    all_record = dataset.shape[0]
    total_number = negative_dataset_shape // 0.8
    append_positive_number = int(total_number - all_record)
    append_dataset = positive_dataset.sample(n=append_positive_number, random_state=7, replace=True)
    #  reconstruct: dataset 20% positive 80% negative
    reconstruct_dataset = pd.concat([dataset, append_dataset])

    negative_dataset = reconstruct_dataset.loc[reconstruct_dataset['distant_recurrence'] == 0]
    positive_dataset = reconstruct_dataset.loc[reconstruct_dataset['distant_recurrence'] == 1]
    positive_number_each_portion = positive_dataset.shape[0] // k
    negative_number_each_portion = negative_dataset.shape[0] // k
    portion_array = []
    n = 0
    for i in range(0, negative_dataset.shape[0], negative_number_each_portion + 1):
        negative_portion = negative_dataset.iloc[i:i + negative_number_each_portion]
        portion_array.append(negative_portion)
    # print(portion_array[0])
    # print(portion_array[1])
    for i in range(0, positive_dataset.shape[0], positive_number_each_portion + 1):
        positive_portion = positive_dataset.iloc[i: i + positive_number_each_portion]
        portion_array[n] = pd.concat([portion_array[n], positive_portion])
        portion_array[n] = shuffle(portion_array[n])
        # portion_array[n].sample(frac=1)
        n += 1
    return portion_array
