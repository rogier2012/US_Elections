import json
from pprint import pprint

with open('votes.json') as data_file:
    data = json.load(data_file)


def get_plurality_total_winner(data):
    # initialize result dict
    result = {"C":0, "T":0, "J":0}
    transitionTable = {"CJT":"C", "CTJ":"C", "JCT":"J", "JTC":"J", "TJC":"T", "TCJ": "T"}
    for state in data:
        for triple, win in transitionTable.items():
            result[win] = result[win]+state[triple]
    check = 0
    for k,v in result.items():
        check = check+v
    assert check == 324893002
    return result




pprint(get_plurality_total_winner(data))
