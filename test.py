import cProfile
import timeit
from collections import defaultdict

from vector import Vector
from matrix import Matrix
from transforms2D import (Rot2D, Trans2D)
from math import pi

import numpy as np
import random


v1 = Vector(100000)
v2 = Vector(100000)
print(len(v1._vals))
for i in range(v1._d):
    v1.set(i, random.uniform(10, 20))
    v2.set(i, random.uniform(1, 5))
# print(v1.sum(v2))

cProfile.run('v1.sum(v2)')
cProfile.run('v1.dot(v2)')

""" mat = Matrix(m=2, n=2)
print(mat.column(0))

def get_col(j, q):
    if q == 0:
        return Vector([1, 0], False)

e = Matrix(m=2, n=2, 
           get_column_method=lambda j: get_col(j, 0),
           get_row_method=lambda i: Vector([1, 1], False) if i == 0 
           else Vector([0, 0], False))
print(e.column(0))

cProfile.run('e.column(0)')
cProfile.run('Rot2D(pi / 6) * Trans2D(1) * Rot2D(pi / 3)')
cProfile.run('Rot2D(pi / 6).matmul(Trans2D(1)).matmul(Rot2D(pi / 3))')

e = Rot2D(pi / 6).matmul(Trans2D(1)).matmul(Rot2D(pi / 3))

print(e.cofactor(2, 2).det2())

rot2d = lambda q: np.matrix([ [ np.cos(q), -np.sin(q), 0 ], 
                              [ np.sin(q), np.cos(q), 0 ],
                              [ 0, 0, 1] ])
tr2d = lambda x, y: np.matrix([ [ 1, 0, x ], 
                                [ 0, 1, y ], 
                                [ 0, 0, 1 ] ])
cProfile.run('rot2d(np.pi / 6) * tr2d(1, 0) * rot2d(np.pi / 3)')

setup_1 = ''' 
from math import pi
from transforms2D import (Rot2D, Trans2D)
'''
code_1 = '''
Rot2D(pi / 6) * Trans2D(1) * Rot2D(pi / 3)
'''

print(timeit.timeit(setup=setup_1, stmt=code_1, number=10000))

setup_2 = '''
import numpy as np
'''
code_2 = '''
rot2d = lambda q: np.matrix([ [ np.cos(q), -np.sin(q), 0 ], 
                              [ np.sin(q), np.cos(q), 0 ],
                              [ 0, 0, 1] ])
tr2d = lambda x, y: np.matrix([ [ 1, 0, x ], 
                                [ 0, 1, y ], 
                                [ 0, 0, 1 ] ])
rot2d(np.pi / 6) * tr2d(1, 0) * rot2d(np.pi / 3)
'''

print(timeit.timeit(setup=setup_2, stmt=code_2, number=10000)) """