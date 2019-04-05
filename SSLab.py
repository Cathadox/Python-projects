
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pyplot
from sklearn.metrics import mean_squared_error



#Ги читаме податоците од страницата за мерење на атмосферски гасови и честици во Македонија
#преку табела во csv формат и ја чуваме како дводимензионална низа со 2 колони(време и вредност на PM10 честици)

dataset_test = pd.read_csv('merenja_karpos.csv')
#Низата ја претвораме во Dataframe
dataset_test1 = pd.DataFrame(dataset_test.Karpos)
#Ја намалуваме фрекфенцијата на мерењата(од стартот фрекфенцијата е едно мерење/сат)
delay_metrics = 200
for index, rows in dataset_test1.iterrows():
    if(index%delay_metrics==0):
        dataset_test1 = dataset_test1.drop(index, axis=0)
#Оттука додаваме нови колони во Датафрејмот кадешто калкуриаме Moving Average со период од 1, 2 и 3

dataset_test1['MA_1'] = dataset_test1.Karpos.rolling(2).mean()
dataset_test1['MA_2'] = dataset_test1.Karpos.rolling(3).mean()
dataset_test1['MA_3'] = dataset_test1.Karpos.rolling(4).mean()
#Пресметуваме процент на редуцирана трансмисија

total_packages_1 = 1
total_packages_2 = 2
total_packages_3 = 3
transmission_Percentage_1 = list()
transmission_Percentage_2 = list()
transmission_Percentage_3 = list()
original_list = dataset_test1['Karpos'].values
MA_1_list = dataset_test1['MA_1'].values
MA_2_list = dataset_test1['MA_2'].values
MA_3_list = dataset_test1['MA_3'].values

for threshold in range(1,3):
    for i in range(len(original_list)):
        pla = abs(MA_1_list[i]-original_list[i])
        if pla > (threshold/10):
          total_packages_1 += 1
    transmission_Percentage_1.append(100 - ((total_packages_1 * 1.0 / len(original_list)) * 100))

for threshold in range(1, 3):
    for i in range(len(original_list)):
            pla = abs(MA_2_list[i]-original_list[i])
            if pla <= threshold:
                total_packages_2 += 1
                print(total_packages_2)

    transmission_Percentage_2.append(100 - ((total_packages_2 * 1.0 / len(original_list)) * 100))
for threshold in range(1, 3):
    for i in range(len(original_list)):
            pla = abs(MA_3_list[i]-original_list[i])
            if pla <= threshold:
                total_packages_3 += 1
                print(total_packages_3)
    transmission_Percentage_3.append(100 - ((total_packages_3 * 1.0 / len(original_list)) * 100))


pyplot.subplot(xlabel='Threshold', ylabel='% of reduced transmissions')
pyplot.plot(transmission_Percentage_1,color='yellow', label='MA(1)')
pyplot.plot(transmission_Percentage_2,color='blue', label='MA(2)')
pyplot.plot(transmission_Percentage_3,color='red',label='MA(3)')

pyplot.legend(loc='best')

plt.show()
#for index, rows in dataset_test1['Karpos'].iterrows():

#Го цртаме графот на колоните за да ја визуелизираме разлика од оригиналните податоци и податоците добиени
#со алгоритамот MA(1), MA(2), MA(3)

plt.figure(figsize=(15, 10))
plt.grid(True)
plt.plot(dataset_test1['Karpos'], color='blue', label='Originalni podatoci')
plt.plot(dataset_test1['MA_1'], label='MA(1)')
plt.plot(dataset_test1['MA_2'], label='MA(2)')
plt.plot(dataset_test1['MA_3'], label='MA(3)')
plt.legend(loc='best')
plt.show()
dataset_test1_1 = dataset_test1.dropna()
#Го печатиме датасетот
print(dataset_test1_1)
#Ги печатиме RMSE
RMSE_1= np.sqrt(mean_squared_error(dataset_test1_1['Karpos'], dataset_test1_1['MA_1']))
RMSE_2= np.sqrt(mean_squared_error(dataset_test1_1['Karpos'], dataset_test1_1['MA_2']))
RMSE_3= np.sqrt(mean_squared_error(dataset_test1_1['Karpos'], dataset_test1_1['MA_3']))
print('RMSE_MA(1):', RMSE_1, 'RMSE_MA(2):', RMSE_2, 'RMSE_MA(3):', RMSE_3)
#Ја печатиме листата со проценти на трансмисии
print(transmission_Percentage_1)
print(transmission_Percentage_2)
print(transmission_Percentage_3)
plt.plot

