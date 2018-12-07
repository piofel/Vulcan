# Problem definition

class Problem:
    def __init__(self):
        self.init_state = 'a'

    def successor_function(self,state):
        if state == 'a':
            val = [['go_l','b'],['go_r','c']]
        if state == 'b':
            val = [['go_l','d'],['go_r','e']]
        if state == 'c':
            val = [['go_l','f'],['go_r','g']]
        if state == 'd':
            val = [['go_l','h'],['go_r','i']]
        if state == 'e':
            val = [['go_l','j'],['go_r','k']]
        if state == 'f':
            val = [['go_l','l'],['go_r','m']]
        if state == 'g':
            val = [['go_l','n'],['go_r','o']]
        if state in {'h','i','j','k','l','m','n','o'}:
            val = []
        return val

    def goal_test(self,state):
        if state == 'h':
            return True
        else:
            return False

    def step_cost(self,state,action,result):
        return 1.0

    def heuristics(self,state):
        return 'heur'

