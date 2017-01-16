import json


def get_plurality_winner(item):
    t = item.get("TJC",0) + item.get("TCJ",0)
    c = item.get("CTJ", 0) + item.get("CJT", 0)
    j = item.get("JTC", 0) + item.get("JCT", 0)
    # print(state["name"] + " t: "+ str(t) + " c: "+ str(c) + " j :"+ str(j))
    if t >= c:
        if t >= j:
            return "Trump"
        else:
            return "Johnson"
    else:
        if c >= j:
            return "Clinton"
        else:
            return "Johnson"


json_data = open("votes.json").read()
votes = json.loads(json_data)

result = dict()

for state in votes:
    winner = get_plurality_winner(state)
    seats = state.get("seats",0)
    # print(state.get("name") + " winner: " +  str(winner) + " with " + str(seats))
    result[winner] = result.get(winner,0) + seats

winner = ""
max = 0
for r in result:
    if result[r] > max:
        max = result[r]
        winner = r

print("Winner is " + winner + " with " + str(max) + " seats")
print(result)




