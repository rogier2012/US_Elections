
def get_plurality_loser(item,x,y,z):
    t = item.get("TJC", 0) * x + item.get("TCJ",0) * x + item.get("CTJ", 0) * y +\
        item.get("JTC", 0) * y + item.get("CJT",0) * z + item.get("JCT", 0) * z
    c = item.get("TJC", 0) * z + item.get("TCJ",0) * y + item.get("CTJ", 0) * x +\
        item.get("JTC", 0) * z + item.get("CJT",0) * x + item.get("JCT", 0) * y
    j = item.get("TJC", 0) * y + item.get("TCJ",0) * z + item.get("CTJ", 0) * z +\
        item.get("JTC", 0) * x + item.get("CJT",0) * y + item.get("JCT", 0) * x
    # print(state["name"] + " t: "+ str(t) + " c: "+ str(c) + " j :"+ str(j))
    if t >= c:
        if c >= j:
            return ["T", "C"]
        else:
            return ["T","J"]
    else:
        if t >= j:
            return ["C","T"]
        else:
            return ["C","J"]

def get_winner_triple(triple, c1, c2):
    if triple.index(c1) < triple.index(c2):
        return c1
    else:
        return c2


def borda_with_runoff_state(votes,x=3,y=1,z=0):
    result = dict()
    result['J'] = 0
    result['C'] = 0
    result['T'] = 0
    for state in votes:
        winners = get_plurality_loser(state,x,y,z)
        w1 = winners[0]
        w2 = winners[1]
        resultInter = dict()
        resultInter[get_winner_triple("TJC",w1,w2)] = resultInter.get(get_winner_triple("TJC",w1,w2),0) + state.get("TJC", 0)
        resultInter[get_winner_triple("TCJ", w1, w2)] = resultInter.get(get_winner_triple("TCJ",w1,w2),0) + state.get("TCJ", 0)
        resultInter[get_winner_triple("CTJ", w1, w2)] = resultInter.get(get_winner_triple("CTJ",w1,w2),0) + state.get("CTJ", 0)
        resultInter[get_winner_triple("CJT", w1, w2)] = resultInter.get(get_winner_triple("CJT",w1,w2),0) + state.get("CJT", 0)
        resultInter[get_winner_triple("JTC",w1,w2)] = resultInter.get(get_winner_triple("JTC",w1,w2),0) + state.get("JTC", 0)
        resultInter[get_winner_triple("JCT",w1,w2)] = resultInter.get(get_winner_triple("JCT",w1,w2),0) + state.get("JCT", 0)
        if resultInter[w1] >= resultInter[w2]:
            result[w1] = result[w1] + state.get("seats",0)
        else:
            result[w2] = result[w2] + state.get("seats",0)

    winner = ""
    max = 0
    for r in result:
        if result[r] > max:
            max = result[r]
            winner = r
    if winner == "T":
        winner = "Trump"
    elif winner == "C":
        winner = "Clinton"
    elif winner == "J":
        winner = "Johnson"
    print(result)
    return ("Winner is " + winner + " with " + str(max) + " seats")
