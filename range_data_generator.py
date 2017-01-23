import json
import random

json_data = open("votes.json").read()
votes = json.loads(json_data)

rangeTable = [[2,2],[1,1],[0,0]]

def randomTable():
    res = list()
    for i in range(0,3):
        res.append(random.uniform(0,5))
    res = list(reversed(sorted(res)))
    return res


def generate_range(triple, amount, rand=False):
    res = {triple[0]:0, triple[1]:0, triple[2]:0}
    if(rand):
        for i in range(0, amount):
            random_table = randomTable()
            res[triple[0]] += random_table[0]
            res[triple[1]] += random_table[1]
            res[triple[2]] += random_table[2]
    else:
        for i in range(0,len(rangeTable)):
            for j in range(0, amount):
                res[triple[i]] += random.uniform(rangeTable[i][1], rangeTable[i][0])
    return res

def get_data(data):
    result = {"C": 0, "T": 0, "J": 0}
    triples = {"CJT":0, "CTJ":0, "JCT":0, "JTC":0, "TJC":0, "TCJ":0}
    # for state in data:
    step = 100
    total = 324893002//step
    for key, val in triples.items():
        total_score_trip = {"T": 0, "C": 0, "J":0}
        for state in data:
            generate_amount = state[key] // step
            temp_res = (generate_range(key, generate_amount, False))
            for k,v in temp_res.items():
                total_score_trip[k] += v
        for k1,v1 in total_score_trip.items():
            result[k1] += v1

    # print(result)
    # for k,v in result.items():
    #     result[k] = v/total
    print(result)

for i in range(0,10):
    get_data(votes)
