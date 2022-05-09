import json

learn = open('learn.json')
test = open('test.json')
TEST_DATA = json.load(test)
TEST_DATA = TEST_DATA['inputdata']
LEARN_DATA = json.load(learn)
LEARN_DATA = LEARN_DATA['inputdata']
ALL_POSSIBLE_ATTRIBUTES = {}


def getLearnData():
    return LEARN_DATA


def getTestData():
    return TEST_DATA


def getKeyAttribute():
    return list(TEST_DATA[0])[-1]


def getQuantityOfDecisionClasses():
    decisionClasses = {}

    for item in LEARN_DATA:
        if decisionClasses.get(item[list(item)[-1]]) is None:
            decisionClasses[item[list(item)[-1]]] = 0

    return len(list(decisionClasses))

