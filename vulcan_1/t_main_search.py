import problem_definition
import tree_search

p = problem_definition.Problem()
searcher = tree_search.Searcher()

a = searcher.depth_first_search(p)

while a != [] and a != None:
    s = a.pop()
    print(s.state)

if a == None:
    print('No solution')
    
