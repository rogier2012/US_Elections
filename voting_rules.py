from current_system import current_system
from plurality_total_us import get_plurality_total_winner
from plurality_with_runoff_us import overall_plurality_runoff
from plurality_runoff_state import state_plurality_runoff
from borda_runoff import borda_runoff
from borda_runoff_state import borda_with_runoff_state
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
    elif voting_rule == 5:
        return borda_runoff(votes)
    elif voting_rule == 6:
        return borda_with_runoff_state(votes,3,1,0)


print(get_winner(5))
print(get_winner(6))