import manipulator as mp
from sympy import symbols, Function, pprint, lambdify, Derivative, Matrix
from math import radians
import time

t = symbols('t')
l1,l2 = symbols('l1,l2')
l1 = 1.2
l2 = 0.3

joint_variables_symbols = ['t1','t2']
t1 = Function(joint_variables_symbols[0])
t2 = Function(joint_variables_symbols[1])
joint_velocities_symbols = ['d'+s for s in joint_variables_symbols]
dt1 = Function(joint_velocities_symbols[0])
dt2 = Function(joint_velocities_symbols[1])

j1 = mp.Joint(0,0,t1(t),0,'revolute')
j2 = mp.Joint(0,l1,t2(t),0,'revolute')
ee = mp.Joint(0,l2,0,0,'end_effector')
m = mp.Manipulator([j1,j2,ee])

start = time.time()

j = m.joint_vector_with_derivative()
v = m.differential_kinematics()
v = v.subs(Derivative(t1(t),t),dt1(t))
v = v.subs(Derivative(t2(t),t),dt2(t))

f = lambdify(tuple(j),v)
x = f(radians(135),radians(-25.7),radians(12.4),radians(-5.7))

jac = m.jacobian()
vec = m.joint_vector()

g = lambdify(tuple(vec),jac)
y = g(radians(135),radians(-25.7)) * Matrix([radians(12.4),radians(-5.7)])

print('Difference:')
pprint(x-y)
print('Time: ' + str(time.time() - start))
