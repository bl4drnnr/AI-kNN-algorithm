from common import CityBlock, Euklid, Minkowski, printResult, normalElection, distanceSumElection, sumOfReciprocalOfTheSquaresOfDistances
from parser import getLearnData, getTestData

LEARN_DATA = getLearnData()
TEST_DATA = getTestData()
DATA_WITH_METRICS = []

EU = []
CB = []
M3 = []

for testItem in TEST_DATA:
    for learnItem in LEARN_DATA:
        DATA_WITH_METRICS.append(
            {**learnItem,
             'EU': Euklid(learnItem, testItem),
             'CB': CityBlock(learnItem, testItem),
             'M3': Minkowski(learnItem, testItem)
             })
    # Then, I need to sort this data by type
    sortedEU = sorted(DATA_WITH_METRICS, key=lambda x: x['EU'], reverse=True)
    sortedCB = sorted(DATA_WITH_METRICS, key=lambda y: y['CB'], reverse=True)
    sortedM3 = sorted(DATA_WITH_METRICS, key=lambda z: z['M3'], reverse=True)
    # Get 1/3/5 from top
    for i in range(1, 6, 2):
        normalElectionEU = normalElection(sortedEU)
        distanceSumElectionEU = distanceSumElection(sortedEU)
        sumOfReciprocalEU = sumOfReciprocalOfTheSquaresOfDistances(sortedEU)

        normalElectionCB = normalElection(sortedCB)
        distanceSumElectionCB = distanceSumElection(sortedCB)
        sumOfReciprocalCB = sumOfReciprocalOfTheSquaresOfDistances(sortedCB)

        normalElectionM3 = normalElection(sortedM3)
        distanceSumElectionM3 = distanceSumElection(sortedM3)
        sumOfReciprocalM3 = sumOfReciprocalOfTheSquaresOfDistances(sortedM3)
        
    DATA_WITH_METRICS = []

    # And push it to EU, CB, M3

printResult('Euklid', EU)
printResult('City block', CB)
printResult('Minkowski', M3)
