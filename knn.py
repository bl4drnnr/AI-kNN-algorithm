from common import CityBlock, Euklid, Minkowski, printResult
from parser import getLearnData, getTestData

LEARN_DATA = getLearnData()
TEST_DATA = getTestData()

EU = []
CB = []
M3 = []

for learnItem in LEARN_DATA:
    for testItem in TEST_DATA:
        EU.append(CityBlock(learnItem, testItem))
        CB.append(Euklid(learnItem, testItem))
        M3.append(Minkowski(learnItem, testItem))


printResult('Euklid', EU)
printResult('City block', CB)
printResult('Minkowski', M3)
