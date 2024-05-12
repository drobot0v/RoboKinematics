from collections import defaultdict, Counter
import math

class AlgebraicException(Exception):
    pass


class InitializationException(Exception):
    pass


class Vector:

    def __init__(self, dim: int, vals = None, copy = True):
        if dim <= 0:
            raise InitializationException
        self._d = dim
        if vals:
            if isinstance(vals, dict):
                self._vals = vals.copy() if copy else vals
            else:
                if len(vals) >= self._d:
                    raise InitializationException
                for _ in range(self._d):
                    self._vals = defaultdict(lambda: 0.0)
                    self._vals[_] = vals[_]
        else:
            self._vals = defaultdict(lambda: 0.0)

    def iszero(self) -> bool:
       return len(self._vals.keys()) == 0

    def __getitem__(self, index: int) -> float:
        if index >= 0 and index < self._d:
            return self._vals[index]
        else:
            raise IndexError

    def __setitem__(self, index: int, value: float):
        if index >= 0 and index < self._d:
            self._vals[index] = value
        else:
            raise IndexError

    def removeByIndex(self, index, create_new=True):
        if create_new:
            vals_ = self._vals.copy()
            del vals_[index]
            return Vector(self._d - 1, vals_, False)
        else:
            del self._vals[index]
            self._d -= 1

    def copy(self) -> 'Vector':
        return Vector(self._d, self._vals)

    def __repr__(self) -> str:
        return str([self._vals[_] for _ in range(self._d)])

    def __add__(self, other: 'Vector') -> 'Vector':
        return self.sum(other)

    def sum(self, other: 'Vector') -> 'Vector':
        if self._d == other._d:
            # return Vector(self._d, defaultdict(Counter(self._vals).update(Counter(other._vals))), False)
            if not bool(self._vals):
                return other
            elif not bool(other._vals):
                return self
            else:
                vals_ = defaultdict(float, 
                                    {k: self._vals[k] + other._vals[k] for k in set(self._vals.keys()) | set(other._vals.keys())})
                vals_.default_factory = lambda: 0.0
                return Vector(self._d, vals_, False)

        else:
            raise AlgebraicException

    def __neg__(self) -> 'Vector':
        return self * (-1)
    
    def __sub__(self, other: 'Vector') -> 'Vector':
        return self + (-other)

    def __mul__(self, other) -> 'Vector':
        if isinstance(other, (int, float)):
            return self.mul(other)
        elif isinstance(other, Vector):
            return self.dot(other)
        else:
            raise AlgebraicException
    
    def __rmul__(self, scalar: int | float) -> 'Vector':
        return self.__mul__(scalar)

    def mul(self, other: int | float, sensitivity = 0.0) -> float:
        if self.iszero() or math.abs(other) <= sensitivity: #TODO: May be too sophisticated
            return Vector(self._d)
        else:
            vals_ = self._vals.copy()
            for _ in vals_.keys():
                vals_[_] *= other
        return Vector(vals_, False)

    def dot(self, other: 'Vector') -> float:
        if self._d == other._d:
            if bool(self._vals) and bool(other._vals): # Instead of invoking 'keys()'
                res_ = 0.0
                for _ in range(self._d): # set(self._vals.keys()).join(set(self._vals.keys())):
                    res_ += self._vals[_] * other._vals[_]
                return res_
            else:
                return 0.0
        else: 
            raise AlgebraicException
        
    # Of less performance:
    def dot2(self, other: 'Vector') -> float:
        if self._d == other._d:
            return sum([x * y for (x, y) in zip(self._vals, other._vals)])
        return None