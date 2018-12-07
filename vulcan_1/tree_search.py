# Tree search algorithm

import problem_definition as pd

class Searcher:
    def __init__(self):
        self.nonexist = None
        self.done = False

    def depth_first_search(self,problem):
        fringe = []
        init_node = Node(problem.init_state,self.nonexist,self.nonexist,0.0,0)
        fringe.append(init_node)
        while not self.done:
            if fringe == []:
                self.done = True 
                solution = None
            else:
                node = fringe.pop()
                if problem.goal_test(node.state):
                    solution = []
                    solution.append(node)
                    parent = node.parent_node
                    while parent != self.nonexist:
                        solution.append(parent)
                        parent = parent.parent_node
                    self.done = True
                else:
                    successors = self.expand(node,problem)
                    if successors != []:
                        fringe.extend(successors)
        return solution

    def expand(self,node,problem):
        successors = []
        sfv = problem.successor_function(node.state)
        while sfv != []:
            x = sfv.pop()
            result = x.pop()
            action = x.pop()
            cost = node.path_cost + problem.step_cost(node.state,action,result)
            d = node.depth + 1
            s = Node(result,node,action,cost,d)
            successors.append(s)
        return successors

class Node:
    def __init__(self,state_arg,parent_node_arg,action_arg,path_cost_arg,depth_arg):
            self.state = state_arg
            self.parent_node = parent_node_arg
            self.action = action_arg
            self.path_cost = path_cost_arg
            self.depth = depth_arg
