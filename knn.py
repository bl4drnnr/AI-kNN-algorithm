from common import CityBlock, Euklid, Minkowski, printResult, normalElection, distanceSumElection, \
    sumOfReciprocalOfTheSquaresOfDistances
from parser import getLearnData, getTestData, getKeyAttribute

LEARN_DATA = getLearnData()
TEST_DATA = getTestData()
DATA_WITH_METRICS = []
KEY_ATTRIBUTE = getKeyAttribute()

EU = {
    'normalElection': [],
    'distanceSumElection': [],
    'sumOfReciprocal': [],
}
CB = {
    'normalElection': [],
    'distanceSumElection': [],
    'sumOfReciprocal': [],
}
M3 = {
    'normalElection': [],
    'distanceSumElection': [],
    'sumOfReciprocal': [],
}


for testItem in TEST_DATA:
    for learnItem in LEARN_DATA:
        DATA_WITH_METRICS.append(
            {**learnItem,
             'EU': Euklid(learnItem, testItem),
             'CB': CityBlock(learnItem, testItem),
             'M3': Minkowski(learnItem, testItem)
             })
    # Then, sort this data by type
    sortedEU = sorted(DATA_WITH_METRICS, key=lambda x: x['EU'], reverse=False)
    sortedCB = sorted(DATA_WITH_METRICS, key=lambda y: y['CB'], reverse=False)
    sortedM3 = sorted(DATA_WITH_METRICS, key=lambda z: z['M3'], reverse=False)
    # Get 1/3/5 from top
    # @TODO Fix duplicates lines
    for i in range(1, 6, 2):
        normalElectionEU = normalElection(sortedEU[:i], testItem)
        if normalElectionEU:
            EU['normalElection'].append(1)
        else:
            EU['normalElection'].append(0)
        distanceSumElectionEU = distanceSumElection(sortedEU[:i], testItem, 'EU')
        if distanceSumElectionEU:
            EU['distanceSumElection'].append(1)
        else:
            EU['distanceSumElection'].append(0)
        print('----------')
        # sumOfReciprocalEU = sumOfReciprocalOfTheSquaresOfDistances(sortedEU[:i])
        # if sumOfReciprocalEU:
        #     EU['sumOfReciprocal'].append(1)
        # else:
        #     EU['sumOfReciprocal'].append(0)

        normalElectionCB = normalElection(sortedCB[:i], testItem)
        if normalElectionCB:
            CB['normalElection'].append(1)
        else:
            CB['normalElection'].append(0)
        distanceSumElectionCB = distanceSumElection(sortedCB[:i], testItem, 'CB')
        if distanceSumElectionCB:
            CB['distanceSumElection'].append(1)
        else:
            CB['distanceSumElection'].append(0)
        # sumOfReciprocalCB = sumOfReciprocalOfTheSquaresOfDistances(sortedEU[:i])
        # if sumOfReciprocalCB:
        #     CB['sumOfReciprocal'].append(1)
        # else:
        #     CB['sumOfReciprocal'].append(0)

        normalElectionM3 = normalElection(sortedM3[:i], testItem)
        if normalElectionM3:
            M3['normalElection'].append(1)
        else:
            M3['normalElection'].append(0)
        distanceSumElectionM3 = distanceSumElection(sortedM3[:i], testItem, 'M3')
        if distanceSumElectionM3:
            M3['distanceSumElection'].append(1)
        else:
            M3['distanceSumElection'].append(0)
        # normalElectionM3 = sumOfReciprocalOfTheSquaresOfDistances(sortedM3[:i])
        # if normalElectionM3:
        #     M3['sumOfReciprocal'].append(1)
        # else:
        #     M3['sumOfReciprocal'].append(0)
    DATA_WITH_METRICS = []


printResult('Euklid', EU)
printResult('City block', CB)
printResult('Minkowski', M3)
