import json
from pprint import pprint



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
    max = 0
    winner = ""
    for c in result:
        if result[c] > max:
            max = result[c]
            winner = c

    if winner == "T":
        winner = "Trump"
    elif winner == "C":
        winner = "Clinton"
    elif winner == "J":
        winner = "Johnson"
    return ("Winner is " + winner + " with all"  + " seats")




