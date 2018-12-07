from multiprocessing import Pool, cpu_count
from sympy import *

class MatrixUtils:

    def simplify_matrix(self,a_matrix):
        l = self.convert_to_me_list(a_matrix)
        pool = Pool(processes=cpu_count())
        l = pool.map(self.simplify_matrix_element,l)
        m = self.convert_to_matrix(l)
        return m

    @staticmethod
    def convert_to_me_list(a_matrix):
        (r,c) = a_matrix.shape
        l = []
        for i in range(0,r):
            for j in range(0,c):
                l.append((a_matrix[i,j],(i,j)))
        l.append(('shape',(r,c)))
        return l

    @staticmethod
    def convert_to_matrix(me_list):
        (r,c) = me_list.pop()[1]
        m = zeros(r,c)
        l = me_list.copy()
        while l!=[]:
            (e,(i,j)) = l.pop()
            m[i,j] = e
        return m

    @staticmethod
    def simplify_matrix_element(element):
        if element[0] == 'shape':
            return element
        else:
            (me,(i,j)) = element
            me = simplify(me)
            return (me,(i,j))

