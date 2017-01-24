import json
import random
import math
import time
import sys
from threading import Thread


#  Trump is a sort of polarizing alternative.
#  CTJ: C-J <= 3 don't really care
#  CJT: (C+J)-T > 6
#  TCJ: T-(C+J) >= 3
#  TJC: T-(J+C) >= 3
#  JCT: (C+J)-T > 6
#  JTC:  J-C <= 3 don't really care


def give_stars(rule):
    if rule == "CTJ" or rule == "JTC":
        r1, r2, r3 = 0, 0, 0
        while r1 <= r2 or r2 <= r3 or (r1 - r3) > 3:
            r1 = random.uniform(0, 5)
            r2 = random.uniform(0, 5)
            r3 = random.uniform(0, 5)
        if rule == "CTJ":
            return {"C": r1, "T": r2, "J": r3}
        else:
            return {"J": r1, "T": r2, "C": r3}
    elif rule == "CJT" or rule == "JCT":
        r1, r2, r3 = 0, 0, 0
        while r1 <= r2 or r2 <= r3 or ((r1 + r2) - r3) <= 7:
            r1 = random.uniform(0, 5)
            r2 = random.uniform(0, 5)
            r3 = random.uniform(0, 5)
        if rule == "CJT":
            return {"C": r1, "J": r2, "T": r3}
        else:
            return {"J": r1, "C": r2, "T": r3}
    elif rule == "TCJ" or rule == "TJC":
        r1, r2, r3 = 0, 0, 0
        while r1 < r2 or r2 < r3 or (r1 - (r2 + r3)) < 3:
            # r1 = int(round(random.random() * 5))
            # r2 = int(round(random.random() * 5))
            # r3 = int(round(random.random() * 5))
            r1 = random.uniform(0, 5)
            r2 = random.uniform(0, 5)
            r3 = random.uniform(0, 5)
        if rule == "TCJ":
            return {"T": r1, "C": r2, "J": r3}
        else:
            return {"T": r1, "J": r2, "C": r3}


def get_winner_overall():
    print("Thread started!")
    start = time.time()
    total_population = 0
    proxy = 1000
    json_data = open("votes.json").read()
    votes = json.loads(json_data)
    total_votes = dict()
    for state in votes:
        total_votes["CTJ"] = total_votes.get("CTJ", 0) + state.get("CTJ", 0)
        total_votes["CJT"] = total_votes.get("CJT", 0) + state.get("CJT", 0)
        total_votes["TJC"] = total_votes.get("TJC", 0) + state.get("TJC", 0)
        total_votes["TCJ"] = total_votes.get("TCJ", 0) + state.get("TCJ", 0)
        total_votes["JCT"] = total_votes.get("JCT", 0) + state.get("JCT", 0)
        total_votes["JTC"] = total_votes.get("JTC", 0) + state.get("JTC", 0)
        total_population += state.get("population", 0)

    total_stars = {"T": 0, "C": 0, "J": 0}
    for k, v in total_votes.items():
        for x in range(0, int(v / proxy)):
            stars = give_stars(k)
            total_stars["T"] = total_stars["T"] + stars["T"]
            total_stars["C"] = total_stars["C"] + stars["C"]
            total_stars["J"] = total_stars["J"] + stars["J"]

    average_stars = dict()
    for k, v in total_stars.items():
        average_stars[k] = float(v) * proxy / total_population

    print(average_stars)
    print(time.time() - start)


def get_winner_states():
    print("Thread started!")
    start = time.time()
    proxy = 1000
    json_data = open("votes.json").read()
    votes = json.loads(json_data)
    total_seats = dict()
    for state in votes:
        state_votes = {"CTJ": state.get("CTJ", 0), "CJT": state.get("CJT", 0), "TJC": state.get("TJC", 0),
                       "TCJ": state.get("TCJ", 0), "JCT": state.get("JCT", 0), "JTC": state.get("JTC", 0)}

        total_points = {"T": 0, "C": 0, "J": 0}
        for k, v in state_votes.items():
            for x in range(0, int(v / proxy)):
                stars = give_stars(k)
                total_points["T"] = total_points["T"] + stars["T"]
                total_points["C"] = total_points["C"] + stars["C"]
                total_points["J"] = total_points["J"] + stars["J"]

        average_stars = dict()
        # for k, v in total_points.items():
        #     average_stars[k] = float(v) * proxy / state.get("population",0)
        max = -sys.maxsize - 1
        winner = ""
        for k,v in average_stars.items():
            if v > max:
                winner = k
                max = v
        total_seats[winner] = total_seats.get(winner,0) + state.get("seats",0)

    print(total_seats)
    print(time.time() - start)

for i in range(5):
    get_winner_states()
