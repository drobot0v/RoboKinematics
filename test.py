import cProfile
from vector import Vector
from matrix import Matrix
from transforms2D import (Rot2D, Trans2D)
from math import pi

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