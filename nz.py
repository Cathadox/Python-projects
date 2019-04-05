from pandas import Series
from numpy import mean
from sklearn.metrics import mean_squared_error
from matplotlib import pyplot

def MA(window,X,threshold_max):
    # TODO ask if this is ok?
    thresholds=list()
    reducedTransmissions=list()
    for threshold in range(1,threshold_max+1,1):
        transferedPackages = window
        totalNumberOfPackages = len(X)

        history = [X[i] for i in range(window)]
        test = [X[i] for i in range(window, len(X))]
        predictions = list()
        # walk forward over time steps in test
        for t in range(len(test) + window):
            if t < window:
                pass #No printing here
                #print('predicted=NONE expected=' + str(X[t]))
            else:
                t1 = t - window
                length = len(history)
                prediction = mean([history[i] for i in range(length - window, length)])
                observed = test[t1]
                predictions.append(prediction)

                predictionError = abs(prediction - observed)
                # TODO ask if this check is ok or should I always put observed values in history?

                if predictionError <= threshold:
                    history.append(prediction)
                else:
                    history.append(observed)
                    transferedPackages += 1

                #print('predicted=%f, expected=%f' % (prediction, observed))

        error = mean_squared_error(X, history)
        percentOfReducedTransmissions = 100 - ((transferedPackages * 1.0 / totalNumberOfPackages) * 100)

        reducedTransmissions.append(percentOfReducedTransmissions)
        #thresholds.append(threshold)

    return reducedTransmissions





#TODO ask if this is ok for threshold
#threshold_max is 10% from satisfactory  level  of PM10 (100µg/m3) , should I iterrate through more thresholds?
threshold_max=10  # 10% from 100

# prepare situation
#TODO implement reading from csv file, this is data from measurements_Kumanovo_PM10D
X = [125.265,61.4149,96.7307,106.377,90.884,78.5903,76.5308,90.7557,66.6694,62.6649,57.4191,14.7862,36.5333,36.9824,49.4362,78.3973,87.4137,47.6187,29.3271,34.5471,36.2308,35.4654,38.8116,54.337,67.6416,46.0058,35.5383,35.6887,43.4799]
every2Day=[X[i] for i in range(len(X)) if i%2==0 ]
every3Day=[X[i] for i in range(len(X)) if i%3==0 ]

# threshold and transmissions on daily basis, comparison between the MA(1),MA(2),MA(3) algorithms

MA1ReducedTransmissions=MA(1,X,threshold_max)
MA2ReducedTransmissions=MA(2,X,threshold_max)
MA3ReducedTransmissions=MA(3,X,threshold_max)
print(MA1ReducedTransmissions)
pyplot.subplot(xlabel='Threshold', ylabel='% of reduced transmissions',title='Data for PM10 particles in Kumanovo for March 2019 on daily basis!')
pyplot.plot(MA1ReducedTransmissions,color='yellow', label='MA(1)')
pyplot.plot(MA2ReducedTransmissions,color='blue', label='MA(2)')
pyplot.plot(MA3ReducedTransmissions, color='red', label='MA(3)')
pyplot.legend(loc='best')

pyplot.show()


#MA1 FREQUENCIES
#
# MA1EveryDay=MA(1,X,threshold_max)
# MA1EverySecondDay=MA(1,every2Day,threshold_max)
# MA1EveryThirdDay=MA(1,every3Day,threshold_max)
#
# pyplot.subplot(xlabel='Threshold', ylabel='% of reduced transmissions',title='Data for PM10 particles in Kumanovo for March 2019!')
# pyplot.plot(MA1EveryDay,color='yellow', label='MA(1) measures every day')
# pyplot.plot(MA1EverySecondDay,color='blue', label='MA(1) measures every second day')
# pyplot.plot(MA1EveryThirdDay, color='red', label='MA(1) measures every third day')
# pyplot.legend(loc='best')
#
# pyplot.show()


#MA2 WITH DIFFERENT FREQUENCIES

# MA2EveryDay=MA(1,X,threshold_max)
# MA2EverySecondDay=MA(2,every2Day,threshold_max)
# MA2EveryThirdDay=MA(2,every3Day,threshold_max)
#
# pyplot.subplot(xlabel='Threshold', ylabel='% of reduced transmissions',title='Data for PM10 particles in Kumanovo for March 2019!')
# pyplot.plot(MA2EveryDay,color='yellow', label='MA(2) measures every day')
# pyplot.plot(MA2EverySecondDay,color='blue', label='MA(2) measures every second day')
# pyplot.plot(MA2EveryThirdDay, color='red', label='MA(2) measures every third day')
# pyplot.legend(loc='best')
#
# pyplot.show()


#MA3 with different frequencies

# MA3EveryDay=MA(3,X,threshold_max)
# MA3EverySecondDay=MA(3,every2Day,threshold_max)
# MA3EveryThirdDay=MA(3,every3Day,threshold_max)
#
# pyplot.subplot(xlabel='Threshold', ylabel='% of reduced transmissions',title='Data for PM10 particles in Kumanovo for March 2019!')
# pyplot.plot(MA3EveryDay,color='yellow', label='MA(3) measures every day')
# pyplot.plot(MA3EverySecondDay,color='blue', label='MA(3) measures every second day')
# pyplot.plot(MA3EveryThirdDay, color='red', label='MA(3) measures every third day')
# pyplot.legend(loc='best')
#
# pyplot.show()