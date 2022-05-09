from common import CityBlock, Euklid, Minkowski, printResult
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
    sortedCB = sorted(DATA_WITH_METRICS, key=lambda x: x['CB'], reverse=True)
    sortedM3 = sorted(DATA_WITH_METRICS, key=lambda x: x['M3'], reverse=True)
    DATA_WITH_METRICS = []
    # Get 1/3/5 from top
    # And push it to EU, CB, M3

printResult('Euklid', EU)
printResult('City block', CB)
printResult('Minkowski', M3)
