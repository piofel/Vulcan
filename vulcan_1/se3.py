from sympy import *

class HomogeneousTransform:
    def __init__(self):
        self.bottom = Matrix([[0,0,0,1]])

    def translation(self,q1,q2,q3):
        e = eye(3)
        t = Matrix([q1,q2,q3])
        e = e.col_insert(3,t)
        e = e.row_insert(3,self.bottom)
        return e

    def rotation_x(self,a):
        r = Matrix([[1,0,0,0],[0,cos(a),-sin(a),0],[0,sin(a),cos(a),0]])
        r = r.row_insert(3,self.bottom)
        return r

    def rotation_z(self,a):
        r = Matrix([[cos(a),-sin(a),0,0],[sin(a),cos(a),0,0],[0,0,1,0]])
        r = r.row_insert(3,self.bottom)
        return r

    @staticmethod
    def get_rotation_matrix(homogeneous_transform):
        return homogeneous_transform[0:3,0:3]

    @staticmethod
    def get_position_vector(homogeneous_transform):
        return homogeneous_transform[0:3,3]

    @staticmethod
    def get_xyz_fixed_angles_from_rotation_matrix(rotation_matrix):
        r11 = rotation_matrix[0,0]
        r21 = rotation_matrix[1,0]
        r31 = rotation_matrix[2,0]
        r32 = rotation_matrix[2,1]
        r33 = rotation_matrix[2,2]
        y = atan2(-r31,sqrt(r11**2+r21**2))
        z = atan2(r21/cos(y),r11/cos(y))
        x = atan2(r32/cos(y),r33/cos(y))
        return Matrix([x,y,z])

    def get_xyz_fixed_angles(self,homogeneous_transform):
        r = self.get_rotation_matrix(homogeneous_transform)
        a = self.get_xyz_fixed_angles_from_rotation_matrix(r)
        return a

