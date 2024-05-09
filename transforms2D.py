from vector import Vector
from matrix import (Matrix, AlgebraicException)
from math import cos, sin


class Rot2D(Matrix):

    def _rot2D_column(j: int, q: int | float) -> Vector:
        if j == 0:
            return Vector([cos(1), sin(q), 0], False)
        elif j == 1:
            return Vector([-sin(q), cos(q), 0], False)
        elif j == 2:
            return Vector([0, 0, 1], False)
        else:
            raise AlgebraicException
        
    def _rot2D_row(i: int, q: int | float) -> Vector:
        if i == 0:
            return Vector([cos(q), -sin(q), 0], False)
        elif i == 1:
            return Vector([sin(q), cos(q), 0], False)
        elif i == 2:
            return Vector([0, 0, 1], False)
        else:
            raise AlgebraicException

    def __init__(self, q = None):
        self._q = q
        super().__init__(m=3, n=3,
                       get_column_method=lambda j: Rot2D._rot2D_column(j, self._q),
                       get_row_method=lambda i: Rot2D._rot2D_row(i, self._q))

class Trans2D(Matrix):

    def _get_column(j: int, x: int | float, y: int | float) -> Vector:
        if j == 0:
            return Vector([1, 0, 0], False)
        elif j == 1:
            return Vector([0, 1, 0], False)
        elif j == 2:
            return Vector([x, y, 1], False)
        else: 
            raise AlgebraicException
        
    def _get_row(i: int, x: int | float, y: int | float) -> Vector:
        if i == 0:
            return Vector([1, 0, x], False)
        elif i == 1:
            return Vector([0, 1, y], False)
        elif i == 2:
            return Vector([0, 0, 1], False)
        else:
            raise AlgebraicException
        
    def __init__(self, x: int | float, y = 0.0):
        self._x = x
        self._y = y
        super().__init__(m=3, n=3, 
                         get_column_method=lambda j: Trans2D._get_column(j, self._x, self._y),
                         get_row_method=lambda i: Trans2D._get_row(i, self._x, self._y))