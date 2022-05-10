from common import CityBlock, Euklid, Minkowski, printResult, normalElection, distanceSumElection, sumOfReciprocalOfTheSquaresOfDistances
from parser import getLearnData, getTestData, getKeyAttribute

LEARN_DATA = getLearnData()
TEST_DATA = getTestData()
DATA_WITH_METRICS = []
KEY_ATTRIBUTE = getKeyAttribute()

EU = []
CB = []
M3 = []

for testItem in TEST_DATA:
    resEU = []
    for learnItem in LEARN_DATA:
        DATA_WITH_METRICS.append(
            {**learnItem,
             'EU': Euklid(learnItem, testItem),
             'CB': CityBlock(learnItem, testItem),
             'M3': Minkowski(learnItem, testItem)
             })
    # Then, I need to sort this data by type
    sortedEU = sorted(DATA_WITH_METRICS, key=lambda x: x['EU'], reverse=False)
    sortedCB = sorted(DATA_WITH_METRICS, key=lambda y: y['CB'], reverse=False)
    sortedM3 = sorted(DATA_WITH_METRICS, key=lambda z: z['M3'], reverse=False)
    # Get 1/3/5 from top
    for i in range(1, 6, 2):
        recordsFromTop = []
        useAdditionalMetrics = False

        for item in sortedEU[:i]:
            recordsFromTop.append(item[KEY_ATTRIBUTE])

        for recordFromTop in recordsFromTop:
            if recordFromTop != testItem[KEY_ATTRIBUTE]:
                useAdditionalMetrics = True

        if not useAdditionalMetrics:
            resEU.append(1)
        else:
            resEU.append(2)
        # normalElectionEU = normalElection(sortedEU[:i])
        # distanceSumElectionEU = distanceSumElection(sortedEU[:i])
        # sumOfReciprocalEU = sumOfReciprocalOfTheSquaresOfDistances(sortedEU[:i])
        #
        # normalElectionCB = normalElection(sortedCB[:i])
        # distanceSumElectionCB = distanceSumElection(sortedCB[:i])
        # sumOfReciprocalCB = sumOfReciprocalOfTheSquaresOfDistances(sortedCB[:i])
        #
        # normalElectionM3 = normalElection(sortedM3[:i])
        # distanceSumElectionM3 = distanceSumElection(sortedM3[:i])
        # sumOfReciprocalM3 = sumOfReciprocalOfTheSquaresOfDistances(sortedM3[:i])
        # print('-------')
    EU.append(resEU)
    DATA_WITH_METRICS = []

    # And push it to EU, CB, M3

printResult('Euklid', EU)
# printResult('City block', CB)
# printResult('Minkowski', M3)
