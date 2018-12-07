from sympy import *
from se3 import *
from matrix_utils import *

class Manipulator:
    def __init__(self,joints_list):
        self.joints = joints_list

    def forward_kinematics(self):
        n = len(self.joints)
        j1 = self.joints[0]
        t = j1.transform()
        for i in range(1,n):
            nj = self.joints[i]
            njt = nj.transform()
            t *= njt
        return t

    # Jacobian in the symbolic form
    def jacobian(self):
        vel = self.differential_kinematics()
        (r,cv) = vel.shape
        sym = self.joint_vector_derivative()
        c = len(sym)
        jac = zeros(r,c)
        for i in range(0,r):
            expr = expand(vel[i])
            et = collect(expr,sym,evaluate=False)
            for j in range(0,c):
                key = sym[j]
                if key in et:
                    e = et[key]
                    jac[i,j] = e
        u = MatrixUtils()
        jac = u.simplify_matrix(jac)
        return jac

    def differential_kinematics(self):
        h = HomogeneousTransform()
        tr = self.forward_kinematics()
        p = h.get_position_vector(tr)
        r = h.get_rotation_matrix(tr)
        del h,tr
        t = symbols('t')
        p = simplify(p)
        lv = diff(p,t)
        u = MatrixUtils()
        r = u.simplify_matrix(r)
        dr = diff(r,t)
        rt = r.T
        vm = dr * rt
        av = Matrix([vm[2,1],vm[0,2],vm[1,0]])
        av = u.simplify_matrix(av)
        v = lv.col_join(av)
        return v

    def joint_vector(self):
        var = []
        for j in self.joints:
            if j.type != 'end_effector':
                if j.type == 'revolute':
                    v = j.angle
                if j.type == 'prismatic':
                    v = j.offset
                var.append(v)
        return var

    def joint_vector_with_derivative(self):
        v = self.joint_vector()
        n = len(v)
        t = symbols('t')
        for i in range(0,n):
            d = 'd'+ str(v[i])
            d = d.split('(')[0]
            d = Function(d)(t)
            v.append(d)
        return v

    def joint_vector_derivative(self):
        v = self.joint_vector()
        n = len(v)
        t = symbols('t')
        dv = []
        for i in range(0,n):
            d = diff(v[i],t)
            dv.append(d)
        return dv

class Joint:
    def __init__(self,twist_arg,length_arg,angle_arg,offset_arg,joint_type_arg):
        self.twist = twist_arg
        self.length = length_arg
        self.angle = angle_arg
        self.offset = offset_arg
        self.type = joint_type_arg

    def set(self,twist_arg,length_arg,angle_arg,offset_arg,joint_type_arg):
        self.twist = twist_arg
        self.length = length_arg
        self.angle = angle_arg
        self.offset = offset_arg
        self.type = joint_type_arg

    def transform(self):
        t = HomogeneousTransform()
        rt = t.rotation_x(self.twist)
        tl = t.translation(self.length,0,0)
        ra = t.rotation_z(self.angle)
        to = t.translation(0,0,self.offset)
        return rt*tl*ra*to

