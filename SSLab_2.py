import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pyplot
from sklearn.metrics import mean_squared_error

dataset_test_pm = pd.read_csv("merenja_karpos.csv")
dataset_test_so = pd.read_csv("merenja_so2_karpos.csv")

dataset_test_pm['MA_1'] = dataset_test_pm.Karpos.rolling(2).mean()
dataset_test_pm['MA_2'] = dataset_test_pm.Karpos.rolling(3).mean()
dataset_test_pm['MA_3'] = dataset_test_pm.Karpos.rolling(4).mean()

dataset_test_so['MA_1'] = dataset_test_so.Karpos.rolling(2).mean()
dataset_test_so['MA_2'] = dataset_test_so.Karpos.rolling(3).mean()
dataset_test_so['MA_3'] = dataset_test_so.Karpos.rolling(4).mean()

sent_packages_1 = 1
sent_packages_2 = 2
sent_packages_3 = 3

transmission_percentage_1 = list()
transmission_percentage_2 = list()
transmission_percentage_3 = list()

original_list_pm = dataset_test_pm['Karpos'].values
MA_1_pm_list = dataset_test_pm['MA_1'].values
MA_2_pm_list = dataset_test_pm['MA_2'].values
MA_3_pm_list = dataset_test_pm['MA_3'].values

original_list_so = dataset_test_so['Karpos'].values
MA_1_so_list = dataset_test_so['MA_1'].values
MA_2_so_list = dataset_test_so['MA_2'].values
MA_3_so_list = dataset_test_so['MA_3'].values

for threshold in range(1, 5):
    for i in range(len(original_list_pm)):
        pla = abs(MA_1_pm_list[i]-original_list_pm[i])
        pla1 = abs(MA_1_so_list[i]-original_list_so[i])
        if pla > threshold and pla1 >threshold:
          sent_packages_1 += 1
    transmission_percentage_1.append(100 - ((sent_packages_1 * 1.0 / len(original_list_pm)) * 100))

for threshold in range(1, 5):
    for i in range(len(original_list_pm)):
        pla = abs(MA_2_pm_list[i]-original_list_pm[i])
        pla1 = abs(MA_2_so_list[i]-original_list_so[i])
        print(pla,pla1)
        if pla > threshold and pla1 > threshold+1:
          sent_packages_2 += 1
    transmission_percentage_2.append(100 - ((sent_packages_2 * 1.0 / len(original_list_pm)) * 100))

for threshold in range(1, 5):
    for i in range(len(original_list_pm)):
        pla = abs(MA_3_pm_list[i]-original_list_pm[i])
        pla1 = abs(MA_3_so_list[i] - original_list_so[i])
        if pla > threshold and pla1>threshold:
          sent_packages_3 += 1
    transmission_percentage_3.append(100 - ((sent_packages_3 * 1.0 / len(original_list_pm)) * 100))

pyplot.subplot(xlabel='Threshold', ylabel='% of reduced transmissions')
pyplot.plot(transmission_percentage_1,color='yellow', label='MA(1)')
pyplot.plot(transmission_percentage_2,color='blue', label='MA(2)')
pyplot.plot(transmission_percentage_3,color='red',label='MA(3)')
pyplot.legend(loc='best')
pyplot.show()

print(transmission_percentage_1)
print(transmission_percentage_2)
print(transmission_percentage_3)
print(dataset_test_so)

