import json
import random
import math
import time
from threading import Thread

#  Trump is a sort of polarizing alternative.
#  CTJ: C-J <= 3 don't really care
#  CJT: (C+J)-T > 7
#  TCJ: T-(C+J) >= 3
#  TJC: T-(J+C) >= 3
#  JCT: (C+J)-T > 7
#  JTC:  J-C <= 3 don't really care


def give_stars(rule):
    if rule == "CTJ" or rule == "JTC":
        r1, r2, r3 = 0, 0, 0
        while r1 <= r2 or r2 <= r3 or (r1 - r3) > 3:
            r1 = random.uniform(0,5)
            r2 = random.uniform(0,5)
            r3 = random.uniform(0,5)
        if rule == "CTJ":
            return {"C": r1, "T": r2, "J": r3}
        else:
            return {"J": r1, "T": r2, "C": r3}
    elif rule == "CJT" or rule == "JCT":
        r1, r2, r3 = 0, 0, 0
        while r1 <= r2 or r2 <= r3 or ((r1+r2) - r3) <= 7:
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

def get_winner():
    start = time.time()
    total_population = 0
    proxy = 100
    json_data = open("votes.json").read()
    votes = json.loads(json_data)
    total_votes = dict()
    for state in votes:
        total_votes["CTJ"] = total_votes.get("CTJ", 0) + state.get("CTJ", 0)
        total_votes["CJC"] = total_votes.get("CJC", 0) + state.get("CJC", 0)
        total_votes["TJC"] = total_votes.get("TJC", 0) + state.get("TJC", 0)
        total_votes["TCJ"] = total_votes.get("TCJ", 0) + state.get("TCJ", 0)
        total_votes["JCT"] = total_votes.get("JCT", 0) + state.get("JCT", 0)
        total_votes["JTC"] = total_votes.get("JTC", 0) + state.get("JTC", 0)
        total_population += state.get("population", 0)

    total_stars = dict()
    for k, v in total_votes.items():
        for x in range(0, int(v / proxy)):
            stars = give_stars(k)
            total_stars["T"] = total_stars.get("T", 0) + stars.get("T", 0)
            total_stars["C"] = total_stars.get("C", 0) + stars.get("C", 0)
            total_stars["J"] = total_stars.get("J", 0) + stars.get("J", 0)

    average_stars = dict()
    for k, v in total_stars.items():
        average_stars[k] = float(v) * proxy / total_population

    # max = 0
    # winner = ""
    # for k,v in average_stars.items():
    #     if v > max:
    #         winner = k
    #         max = v
    print( average_stars)
thread1 = Thread(target=get_winner())
thread2 = Thread(target=get_winner())
thread3 = Thread(target=get_winner())
thread4 = Thread(target=get_winner())
thread5 = Thread(target=get_winner())
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()
