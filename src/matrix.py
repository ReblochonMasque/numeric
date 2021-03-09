"""
from nompy
a matrix module that implements Matrix objects and associated operations

"""

import math

from fractions import Fraction
from typing import List, NamedTuple, Tuple, Union


Number = Union[float, int, complex, Fraction]


class IncompatibleMatrixShapes(Exception):
    pass


class MatrixIndexError(Exception):
    pass


class Shape(NamedTuple):
    """represents the shape of a matrix in terms of
    number of rows, number of columns

    Attention: __init__ and factories should always make a deepcopy of the sequences passed
    """
    rows: int
    cols: int


class Matrix:
    """
    Represents a matrix
    """

    @classmethod
    def zeros(cls, shape: Union[Shape, tuple]) -> 'Matrix':
        """makes and returns a new matrix of shape.rows x shape.cols
        containing only zeros
        :param shape: a Shape NamedTuple of the number of rows and columns of the matrix
        :return:  new Matrix of shape.rows x shape.cols containing only zeros
        """
        rows, cols = shape
        return cls([[0 for col in range(cols)] for row in range(rows)])

    @classmethod
    def identity(cls, shape: Shape) -> 'Matrix':
        """makes and returns a new matrix of shape.rows x shape.cols
        containing only zeros
        :param shape: a Shape NamedTuple of the number of rows and columns of the matrix
        :return:  new Matrix of shape.rows x shape.cols containing only zeros
        """
        rows, cols = shape
        if rows != cols:
            raise IncompatibleMatrixShapes('Identity Matrix must be square')
        return cls([[1 if col == row else 0 for col in range(cols)] for row in range(rows)])

    def __init__(self, data: List[List[Number]]) -> None:
        """
        :param data: sequence of sequences of numbers of identical length

        Attention: must make a deepcopy of the sequence passed
        """
        assert len(data) > 0, 'Matrix data cannot be empty'
        assert len(data[0]) > 0, 'Matrix rows cannot be empty'
        assert all([len(seq) == len(data[0]) for seq in data]), \
            'all inners must have the same length'
        self._data = [row[:] for row in data]
        self._rows = len(self._data)
        self._cols = len(self._data[0])

    @property
    def rows(self) -> int:
        """
        :return: int, the number of rows of the matrix
        """
        return self._rows

    @property
    def cols(self) -> int:
        """
        :return: int, the number of columns of the matrix
        """
        return self._cols

    @property
    def shape(self) -> 'Shape[int, int]':
        """
        :return: a Shape, a NamedTuple of the number of rows, number of cols of the matrix
        """
        return Shape(rows=self.rows, cols=self.cols)

    def __setitem__(self, row_col: Tuple[int, int], value: Number) -> None:
        """sets the matrix element at row, col to value

        :param row_col: tuple[int, int], containing the row of and column of
                        the element in the Matrix
        :param value: Number, the value to set the element of the Matrix to
        :return: None
        """
        row, col = row_col
        try:
            self._data[row][col] = value
        except IndexError:
            raise MatrixIndexError('Matrix indices row or col out of range')

    def __getitem__(self, row_col: Tuple[int, int]) -> Number:
        """returns the matrix element value at row, col

        :param row_col: tuple[int, int], containing the row of and column of
                        the element in the Matrix
        :return: Number, the element's value at location (row, col) in the Matrix
        """
        row, col = row_col
        try:
            return self._data[row][col]
        except IndexError:
            raise MatrixIndexError('Matrix indices row or col out of range')

    def __eq__(self, other: 'Matrix') -> bool:
        """test for equality, based on type, shape, and element to element equality
        :param other: a Matrix of identical Shape as self
        :return: True if self == other, False otherwise
        """
        if not isinstance(other, type(self)):
            raise TypeError('a Matrix must be compared to a Matrix')
        if self.shape != other.shape:
            raise IncompatibleMatrixShapes('Matrices must have identical shapes to be compared')
        for selfrow, otherrow in zip(self._data, other._data):
            for selfelt, otherelt in zip(selfrow, otherrow):
                if not math.isclose(selfelt, otherelt):
                    return False
        return True

    def transpose(self):
        """
        :return: a new Matrix, transpose of self
        """
        return Matrix(list(map(list, zip(*self._data))))
    T = transpose

    def __neg__(self):
        """
        inverses the sign of each element in self
        mutates self
        :return: self, with each elements'sign inverted
        """
        self._data = [[-elt for elt in row] for row in self._data]
        return self

    def __mul__(self, scalar: Number) -> 'Matrix':
        """
        Matrix multiplication by a scalar
        :param scalar: a Number
        :return: a new Matrix of identical shape as self, whose elements
                 have been multiplied by the scalar
        """
        return Matrix([[elt * scalar for elt in row] for row in self._data])

    def __rmul__(self, scalar: Number) -> 'Matrix':
        """
        Matrix multiplication by a scalar
        :param scalar: a Number
        :return: a new Matrix of identical shape as self, whose elements
                 have been multiplied by the scalar
        """
        return self * scalar

    def __imul__(self, scalar) -> 'Matrix':
        """
        override operator *=  ->  self multiplication by a scalar
        :param scalar: a Number
        :return: self, whose elements have been multiplied by the scalar
        """
        self._data = [[elt * scalar for elt in row] for row in self._data]
        return self

    def __truediv__(self, scalar: Number) -> 'Matrix':
        """
        Matrix multiplication by a scalar
        :param scalar: a Number, must be non zero
        :return: a new Matrix of identical shape as self, whose elements
                 have been multiplied by the scalar
        """
        if scalar == 0:
            raise ZeroDivisionError('the divisor must be non zero')
        return Matrix([[elt / scalar for elt in row] for row in self._data])
    # division of a scalar by a matrix does not make sense.

    def __itruediv__(self, scalar: Number) -> 'Matrix':
        """
        Matrix multiplication by a scalar
        :param scalar: a Number, must be non zero
        :return: a new Matrix of identical shape as self, whose elements
                 have been multiplied by the scalar
        """
        if scalar == 0:
            raise ZeroDivisionError('the divisor must be non zero')
        self._data = [[elt / scalar for elt in row] for row in self._data]
        return self

    def __add__(self, other: "Matrix") -> 'Matrix':
        """
        :param other: a Matrix of Shape identical to self
        :return: a new Matrix with the each element of self added
                 to each element of other
        """
        if self.shape != other.shape:
            raise IncompatibleMatrixShapes('Matrices must have identical shapes to be added')
        return Matrix([[self_e + other_e for self_e, other_e in zip(self_row, other_row)]
                       for self_row, other_row in zip(self._data, other._data)])
    __radd__ = __add__

    def __iadd__(self, other: "Matrix") -> 'Matrix':
        """
        :param other: a Matrix of Shape identical to self
        :return: self with each element of other added to each element of self
        """
        if self.shape != other.shape:
            raise IncompatibleMatrixShapes('Matrices must have identical shapes to be added')
        self._data = [[self_e + other_e for self_e, other_e in zip(self_row, other_row)]
                      for self_row, other_row in zip(self._data, other._data)]
        return self

    def __sub__(self, other: "Matrix") -> 'Matrix':
        """
        :param other: a Matrix of Shape identical to self
        :return: a new Matrix with the each element of self added
                 to each element of other
        """
        if self.shape != other.shape:
            raise IncompatibleMatrixShapes('Matrices must have identical shapes to be subtracted')
        return Matrix([[self_e - other_e for self_e, other_e in zip(self_row, other_row)]
                       for self_row, other_row in zip(self._data, other._data)])
    __rsub__ = __sub__

    def __isub__(self, other: "Matrix") -> 'Matrix':
        """
        :param other: a Matrix of Shape identical to self
        :return: self with each element of other added to each element of self
        """
        if self.shape != other.shape:
            raise IncompatibleMatrixShapes('Matrices must have identical shapes to be subtracted')
        self._data = [[self_e - other_e for self_e, other_e in zip(self_row, other_row)]
                      for self_row, other_row in zip(self._data, other._data)]
        return self

    def __matmul__(self, other: 'Matrix') -> 'Matrix':
        """
        :param other: a Matrix of compatible size
        :return: A Matrix of Shape(self.rows, other.cols), the result of the multiplication of self with other
        """
        if not isinstance(other, type(self)):
            raise TypeError('Matrix multiplication must multiply two Matrices')
        if self.cols != other.rows:
            raise IncompatibleMatrixShapes('Matrix A number of columns must equal Matrix B number of rows')

        rows, cols, ndxs = self.rows, other.cols, self.cols
        _data = [[0 for col in range(cols)] for row in range(rows)]
        for row in range(rows):
            for col in range(cols):
                for ndx in range(ndxs):
                    _data[row][col] += self._data[row][ndx] * other._data[ndx][col]
        return Matrix(_data)

    def __str__(self):
        """
        :return: a string representing the Matrix self
        """
        return '\n'.join(', '.join([str(elt) for elt in mrow]) for mrow in self._data)

    def get_row(self, row: int) -> 'Matrix':
        """returns the row of the Matrix as a 1 x self.cols Matrix

        :param row: int, the row of the matrix to be returned
        :return: a Matrix of shape (1, self.cols) containing the values in the row specified
        """
        try:
            return Matrix([self._data[row]])
        except IndexError:
            raise MatrixIndexError('Matrix row out of range')

    def get_col(self, col: int) -> 'Matrix':
        """returns the col of the Matrix as a 1 x self.rows Matrix

        :param col: int, the col of the matrix to be returned
        :return: a Matrix of shape (1, self.rows) containing the values in the col specified
        """
        try:
            return Matrix([self.T()._data[col]])
        except IndexError:
            raise MatrixIndexError('Matrix row out of range')

    def clone(self) -> 'Matrix':
        """clones self to a new Matrix

        Attention relies on __init__ making a deepcopy of the sequence passed

        :return: a Matrix, deep-copy of self
        """
        return Matrix(self._data)


if __name__ == '__main__':

    a = Matrix([[1, 2], [3, 4]])
    # b = Matrix([[1], [3, 4]])
    c = Matrix([[42]])
    # res = a == c
    print(-a)

    # print(a @ c)

    f = Matrix([[Fraction(1, 2), Fraction(2, 3), Fraction(-3, 4)],
                [Fraction(13, 12), Fraction(2, 3), Fraction(-3, 4)],
                [Fraction(1, 2), Fraction(2, 3), Fraction(-3, 4)]])
    print(f)

    g = Matrix([[1, Fraction(1, 2)], [0, 1]])
    print(g@g)

    print('\n')
    h = Matrix([[1, Fraction(1, 2)], [0, 1]])
    print(h @ h)

    print('\n')
    print(g @ h)

    print('\n')
    print(h @ g)
