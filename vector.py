from collections import deque
import math


class Vector:

    def __init__(self, dim: int):
        self._d = math.abs(dim)
        self._vals = [None] * self._d

    def __init__(self, vals, copy = True):
        self._d = len(vals)
        self._vals = vals.copy() if copy else vals

    def __iter__(self):
        for _ in self._vals:
            yield _

    def __getitem__(self, index: int):
        try:
            return self._vals[index]
        except:
            return None

    def __setitem__(self, index: int, value: float):
        try:
            self._vals.insert(index, value)
        except:
            pass

    def remove(self, index):
        _ = self._vals.copy()
        del _[index]
        return Vector(_, False)

    def __repr__(self) -> str:
        return str(self._vals)

    def __add__(self, other: 'Vector') -> 'Vector':
        if self._d == other._d:
            return Vector([x + y for (x, y) in zip(self._vals, other._vals)], False)
        return None

    def __neg__(self) -> 'Vector':
        return self * (-1)
    
    def __sub__(self, other: 'Vector') -> 'Vector':
        return self + (-other)

    def __mul__(self, other) -> 'Vector':
        if isinstance(other, (int, float)):
            return Vector([_ * other for _ in self._vals], False)
        elif isinstance(other, Vector):
            return self.dot(other)
        else:
            return None
    
    def __rmul__(self, scalar: int | float) -> 'Vector':
        return self.__mul__(scalar)
     
    def dot(self, vector: 'Vector') -> float:
        if self._d == vector._d:
            res_ = 0.0
            for i in range(self._d):
                res_ += self._vals[i] * vector._vals[i]
            return res_
        else: 
            return None
        
    # Of less performance:
    def dot2(self, other: 'Vector') -> float:
        if self._d == other._d:
            return sum([x * y for (x, y) in zip(self._vals, other._vals)])
        return None