import json
from pprint import pprint

with open('votes.json') as data_file:
    data = json.load(data_file)


def get_winner(candidates):
    return max(candidates, key=candidates.get)

def get_loser(candidates):
    return min(candidates, key=candidates.get)

def get_winner_triple(triple, c1, c2):
    if triple.index(c1) < triple.index(c2):
        return c1
    else:
        return c2

def get_plurality_total_winner(data):
    # initialize result dict
    result = {"C":0, "T":0, "J":0}
    transitionTable = {"CJT":"C", "CTJ":"C", "JCT":"J", "JTC":"J", "TJC":"T", "TCJ": "T"}
    for state in data:
        top_2 = get_top_2(state)
        c1 = list(top_2.keys())[0]
        c2 = list(top_2.keys())[1]
        top_2_result = {c1:0, c2:0}
        for triple, candidate in transitionTable.items():
            win = get_winner_triple(triple, c1, c2)
            top_2_result[win] =  top_2_result[win] + state[triple]
        winner = get_winner(top_2_result)
        result[winner] = result[winner] + state['seats']

    print(result)
    return result


def get_top_2(state):
    # initialize result dict
    result = {"C":0, "T":0, "J":0}
    transitionTable = {"CJT":"C", "CTJ":"C", "JCT":"J", "JTC":"J", "TJC":"T", "TCJ": "T"}
    for triple, win in transitionTable.items():
        result[win] = result[win]+state[triple]
    del result[get_loser(result)]
    return result







pprint(get_plurality_total_winner(data))
