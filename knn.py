from common import CityBlock, Euklid, Minkowski, printResult, normalElection, distanceSumElection, sumOfReciprocalOfTheSquaresOfDistances
from parser import getLearnData, getTestData, getKeyAttribute

LEARN_DATA = getLearnData()
TEST_DATA = getTestData()
DATA_WITH_METRICS = []
KEY_ATTRIBUTE = getKeyAttribute()

RESULT = {
    "EU": {
        "normalElection": [],
        "distanceSumElection": [],
        "sumOfReciprocal": [],
    },
    "CB": {
        "normalElection": [],
        "distanceSumElection": [],
        "sumOfReciprocal": [],
    },
    "M3": {
        "normalElection": [],
        "distanceSumElection": [],
        "sumOfReciprocal": [],
    }
}

for testItem in TEST_DATA:
    for learnItem in LEARN_DATA:
        DATA_WITH_METRICS.append(
            {**learnItem,
             "EU": Euklid(learnItem, testItem),
             "CB": CityBlock(learnItem, testItem),
             "M3": Minkowski(learnItem, testItem)
             })
    # Then, sort this data by type
    sortedEU = sorted(DATA_WITH_METRICS, key=lambda x: x["EU"], reverse=False)
    sortedCB = sorted(DATA_WITH_METRICS, key=lambda y: y["CB"], reverse=False)
    sortedM3 = sorted(DATA_WITH_METRICS, key=lambda z: z["M3"], reverse=False)
    sortedMetrics = [{"type": "EU", "records": sortedEU}, {"type": "CB", "records": sortedCB}, {"type": "M3", "records": sortedM3}]
    # Get 1/3/5 from top
    for i in range(1, 6, 2):
        for metric in sortedMetrics:
            normalElectionRes = normalElection(metric["records"][:i], testItem)

            if normalElectionRes:
                RESULT[metric["type"]]["normalElection"].append(1)
            else:
                RESULT[metric["type"]]["normalElection"].append(0)

            distanceSumElectionRes = distanceSumElection(metric["records"][:i], testItem, metric["type"])

            if distanceSumElectionRes:
                RESULT[metric["type"]]["distanceSumElection"].append(1)
            else:
                RESULT[metric["type"]]["distanceSumElection"].append(0)

            sumOfReciprocalRes = sumOfReciprocalOfTheSquaresOfDistances(metric["records"][:i], testItem, metric["type"])

            if sumOfReciprocalRes:
                RESULT[metric["type"]]["sumOfReciprocal"].append(1)
            else:
                RESULT[metric["type"]]["sumOfReciprocal"].append(0)

    DATA_WITH_METRICS = []


printResult("Euklid", RESULT["EU"])
printResult("City block", RESULT["CB"])
printResult("Minkowski", RESULT["M3"])
