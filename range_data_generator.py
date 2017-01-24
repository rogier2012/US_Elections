import json
import random

import sys

json_data = open("votes.json").read()
votes = json.loads(json_data)

rangeTable = [[5, 3], [3, 2], [2, 1]]



def min_candidate(candidates):
    return min(candidates, key=candidates.get)

def get_winner_triple(triple, c1, c2):
    if triple.index(c1) < triple.index(c2):
        return c1
    else:
        return c2

def get_runoff_winner(candidates):
    triples = ["CJT", "CTJ", "JCT", "JTC", "TJC", "TCJ"]
    del candidates[min_candidate(candidates)]
    c1 = list(candidates.keys())[0]
    c2 = list(candidates.keys())[1]
    top_2_result = {c1: 0, c2: 0}
    for state in votes:
        for index, val in enumerate(triples):
            top_2_result[get_winner_triple(val, c1, c2)] += state[val]
    print(top_2_result)
    max = -sys.maxsize - 1
    for c in top_2_result:
        if top_2_result[c] > max:
            max = top_2_result[c]
            winner = c
    return winner



def randomTable():
    res = list()
    for i in range(0, 3):
        res.append(random.uniform(0, 5))
    res = list(reversed(sorted(res)))
    return res


def generate_range(triple, amount, rand=False):
    res = {triple[0]: 0, triple[1]: 0, triple[2]: 0}
    if rand:
        for i in range(0, amount):
            random_table = randomTable()
            res[triple[0]] += random_table[0]
            res[triple[1]] += random_table[1]
            res[triple[2]] += random_table[2]
    else:
        for i in range(0, len(rangeTable)):
            for j in range(0, amount):
                res[triple[i]] += random.uniform(rangeTable[i][1], rangeTable[i][0])
    return res


def get_data(data):
    result = {"C": 0, "T": 0, "J": 0}
    triples = {"CJT": 0, "CTJ": 0, "JCT": 0, "JTC": 0, "TJC": 0, "TCJ": 0}
    # for state in data:
    step = 100
    total = 324893002 // step
    for key, val in triples.items():
        total_score_trip = {"T": 0, "C": 0, "J": 0}
        for state in data:
            generate_amount = state[key] // step
            temp_res = (generate_range(key, generate_amount, False))
            for k, v in temp_res.items():
                total_score_trip[k] += v
        for k1, v1 in total_score_trip.items():
            result[k1] += v1

    print(result)
    for k, v in result.items():
        result[k] = v / total
    print(result)


def get_data_state(data):
    result = {"C": 0, "T": 0, "J": 0}
    triples = {"CJT": 0, "CTJ": 0, "JCT": 0, "JTC": 0, "TJC": 0, "TCJ": 0}
    step = 100

    for state in data:
        score_state = {"T": 0, "C": 0, "J": 0}
        for k, v in triples.items():
            temp_res = (generate_range(k, state[k] // step, True))
            for alternative, score in temp_res.items():
                score_state[alternative] += score
        maxi = -sys.maxsize - 1
        winner = ""
        for k, v in score_state.items():
            if v > maxi:
                maxi = v
                winner = k
        result[winner] += state.get("seats", 0)

    return result

total = dict()
times = 5
for i in range(times):
    res1 = get_data_state(votes)
    for key, value in res1.items():
        total[key] = total.get(key, 0) + (value/times)

print(total)