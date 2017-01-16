from current_system import current_system
from plurality_total_us import get_plurality_total_winner
from plurality_with_runoff_us import overall_plurality_runoff
from plurality_runoff_state import state_plurality_runoff
import json


def get_winner(voting_rule):
    json_data = open("votes.json").read()
    votes = json.loads(json_data)
    if voting_rule == 1:
        return current_system(votes)
    elif voting_rule == 2:
        return get_plurality_total_winner(votes)
    elif voting_rule == 3:
        return overall_plurality_runoff(votes)
    elif voting_rule == 4:
        return state_plurality_runoff(votes)

print(get_winner(4))