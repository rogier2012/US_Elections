import sys

points_distribution = [2,1,0]
def get_loser(candidates):
    return min(candidates, key=candidates.get)

def get_winner_triple(triple, c1, c2):
    if triple.index(c1) < triple.index(c2):
        return c1
    else:
        return c2

def borda_runoff(data):
        # initialize result dict
    result = {"C": 0, "T": 0, "J": 0}
    triples = ["CJT", "CTJ", "JCT", "JTC", "TJC", "TCJ"]
    for state in data:
        for index, val in enumerate(triples):
            result[val[0]] += points_distribution[0]*state[val]
            result[val[1]] += points_distribution[1]*state[val]
            result[val[2]] += points_distribution[2]*state[val]
    check = 0
    for k, v in result.items():
        check = check + v
    print(result)
    assert check == ((324893002*points_distribution[0])+(324893002*points_distribution[1]) + (324893002*points_distribution[2]))
    max = -sys.maxsize-1
    winner = ""
    del result[get_loser(result)]
    c1 = list(result.keys())[0]
    c2 = list(result.keys())[1]
    top_2_result = {c1: 0, c2: 0}
    for state in data:
        for index, val in enumerate(triples):
            top_2_result[get_winner_triple(val, c1, c2)] += state[val]
    print(top_2_result)

    for c in top_2_result:
        if top_2_result[c] > max:
            max = top_2_result[c]
            winner = c

    if winner == "T":
        winner = "Trump"
    elif winner == "C":
        winner = "Clinton"
    elif winner == "J":
        winner = "Johnson"
    return ("Winner is " + winner + " with all" + " seats")




