from common import CityBlock, Euklid, Minkowski
from parser import getLearnData, getTestData

LEARN_DATA = getLearnData()
TEST_DATA = getTestData()

EU = []
CB = []
M3 = []

for learnItem in LEARN_DATA:
    for testItem in TEST_DATA:
        print()
