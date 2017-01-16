import json


# json_data = open("votes.json").read()
# votes = json.loads(json_data)


def overall_plurality_runoff(votes):
    result = dict()
    for state in votes:
        result['TCJ'] = result.get("TCJ",0) + state.get("TCJ",0)
        result['TJC'] = result.get("TJC", 0) + state.get("TJC", 0)
        result['CTJ'] = result.get("CTJ", 0) + state.get("CTJ", 0)
        result['CJT'] = result.get("CJT", 0) + state.get("CJT", 0)
        result['JTC'] = result.get("JTC",0) + state.get("JTC",0)
        result['JCT'] = result.get("JCT",0) + state.get("JCT",0)

    result1 = dict()
    result1["T"] = result["TCJ"] + result["TJC"]
    result1["C"] = result["CTJ"] + result["CJT"]
    result1["J"] = result["JTC"] + result["JCT"]
    # print(result1)
    if result1["T"] > result1["C"]:
        if result1["C"] > result1["J"]:
            del result1["J"]
        else:
            del result1["C"]
    else:
        if result1["T"] > result1["J"]:
            del result1["J"]
        else:
            del result1["T"]

    final_candidates = list(result1.keys())
    final_result = dict()
    for candidate in final_candidates:
        other = final_candidates[(final_candidates.index(candidate) + 1) % 2]
        for ranking in result:
            if ranking.find(candidate) < ranking.find(other):
                final_result[candidate] = final_result.get(candidate,0) + result[ranking]


    winner = ""
    max = 0
    for r in final_result:
        if final_result[r] > max:
            max = final_result[r]
            if r == "J":
                winner = "Johnson"
            elif r == "C":
                winner = "Clinton"
            else:
                winner = "Trump"

    return "Winner is " + winner + " with all" + " seats"