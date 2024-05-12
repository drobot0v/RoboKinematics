from math import pow
from vector import (Vector, AlgebraicException, InitializationException)


class Matrix:
    def __init__(self, 
                 m: int, n: int,
                 get_column_method = None, 
                 get_row_method = None, 
                 data = None):
        self._m = m
        self._n = n
        self._get_column_method = get_column_method
        self._get_row_method = get_row_method
        if data:
            if len(data) == self._m and all(len(r) == self._n for r in data):
                self._data = data
            else:
                raise InitializationException 

    def column(self, j) -> Vector:
        if hasattr(self, '_data'):
            return Vector([self._data[i][j] for i in range(self._m)], False)
        try:
            self._get_column_method(j)
        except TypeError:
            return 
    
    def row(self, i) -> Vector:
        if self._data:
            return Vector([self._data[i]], False)
        return self._get_row_method(i)
    
    def __repr__(self):
        res = '[\n '
        for i in range(self._m):
            res += self.row(i).__repr__() + '\n'
        res += ' ]'
        return res

    def __getitem__(self, i: int, j: int):
        if self._data:
            return self._data[i][j]
        return self.column(j)[i]

    def __add__(self, other: 'Matrix') -> 'Matrix':
        if self._m == other._m and self._n == other._n:
            return Matrix(m=self._m, n=self._n, 
                          get_column_method=lambda j: self.column(j) + other.column(j),
                          get_row_method=lambda i: self.row(i) + other.row(i))
        else:
            raise AlgebraicException
        
    def __neg__(self) -> 'Matrix':
        return Matrix(m=self._m, n=self._n, 
                      get_column_method=lambda j: self.column(j).__neg__(),
                      get_row_method=lambda i: self.row(i).__neg__())
    
    def __sub__(self, other: 'Matrix') -> 'Matrix':
        return self.__sum__(other.__neg__())

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Matrix(m=self._m, n=self._n,
                          get_column_method=lambda j: self.column(j) * other,
                          get_row_method=lambda i: self.row(i) * other)
        elif isinstance(other, Vector):
            return self.vectmul(other)
        elif isinstance(other, Matrix):
            return self.matmul(other)
            
    def sum(self, other: 'Matrix', cache=False) -> 'Matrix':
        if self._m == other._m and self._n == other._n:
            if cache:
                pass
            pass
        else:
            raise AlgebraicException

    def vectmul(self, other: Vector) -> Vector:
        if self._n == other._d:
            return Vector([self.row(i).dot(other) for i in range(self._m)], False)
        else:
            raise AlgebraicException(f'self: {self}, other: {other}')
        
    def matmul(self, other: 'Matrix') -> 'Matrix':
        if self._n == other._m:
            return Matrix(m=self._m, n=other._n,
                          get_column_method=lambda j: self.vectmul(other.column(j)),
                          get_row_method=lambda i: Vector([self.row(i) * other.column(j) for j in range(other._n)], False))
        else:
            raise AlgebraicException
        
    def det2(self) -> float:
        c1_ = self.column(0)
        c2_ = self.column(1)
        print(f'c1: {c1_}, c2: {c2_}')
        return c1_[0] * c2_[1] - c1_[1] * c2_[0]
    
    def cofactor(self, i: int, j: int):
        rows_ = [_ for _ in range(self._m) if _ != i]
        cols_ = [_ for _ in range(self._n) if _ != j]
        return Matrix(m=self._m - 1, n=self._n - 1, 
                                    get_column_method=lambda j: self.column(cols_[j]).removeByIndex(i),
                                    get_row_method=lambda i: self.row(rows_[i]).removeByIndex(j))

    def spread(self, j: int):
        c_ = self.column(j)
        return [(pow(-1, i+j) * c_[j], 
                 self.cofactor(i, j)) for i in range(self._m)]

    def det3(self, j: int) -> float:
        res_ = 0.0
        for _ in self.spread(j):
            res_ += _[0] * _[1].det2()
        return res_

    def solCramer2D(self, rhs: Vector) -> Vector:
        root_matrix_ = lambda r: Matrix(m=self._m, n=self._n,
                                        get_column_method=lambda j: rhs if j == r else self.column(j))
                                        # get_row_method=lambda i: self.vect(i, r, rhs[r]))
        _ = self.det2()
        return [root_matrix_(r).det2() / _ for r in range(2)]


class DenseMatrix(Matrix):
    def __init__(self, data):
        self._data = data
        super().__init__(m=len(data), n=len(data(0)), 
                         get_column_method=lambda j: Vector([_[j] for _ in self._data], False),
                         get_row_method=lambda i: Vector(self._data[i]))


        
    