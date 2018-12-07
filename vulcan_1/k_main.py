import manipulator as mp
from sympy import symbols, Function, pi, pprint
from math import degrees, radians
import time

t = symbols('t')
l2,l3,l5 = symbols('l2,l3,l5')
d3,d4 = symbols('d3,d4')
t1 = Function('t1')
t2 = Function('t2')
t3 = Function('t3')
t4 = Function('t4')
t5 = Function('t5')
t6 = Function('t6')

l2 = 0.8
l3 = 0.7
l5 = 0
d3 = 0.2
d4 = 0.5

j1 = mp.Joint(0,0,t1(t),0,'revolute')
j2 = mp.Joint(-pi/2,0,t2(t),0,'revolute')
j3 = mp.Joint(0,l2,t3(t),d3,'revolute')
j4 = mp.Joint(-pi/2,l3,t4(t),d4,'revolute')
j5 = mp.Joint(pi/2,0,t5(t),0,'revolute')
j6 = mp.Joint(-pi/2,0,t6(t),0,'revolute')
ee = mp.Joint(0,l5,0,0,'end_effector')
m = mp.Manipulator([j1,j2,j3,j4,j5,j6,ee])

start = time.time()

j = m.jacobian()
x = j.det()

pprint(x)
print('Time: ' + str(time.time() - start))
