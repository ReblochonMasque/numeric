"""
Provides some of the basic operations of linear algebra.
For maths with two-dimensional matrices, when you
don't want to use numpy
Matrices are restricted to only contain numbers.
"""

import math

from numbers import Number  # int, float, complex, Fraction, Decimal, and bool
from typing import NamedTuple, Sequence, Tuple, Union


class MatrixShape(NamedTuple):
    num_rows: int
    num_cols: int


class Matrix:
    """
    represents a matrix used for linear algebra mathematical operations
    a Matrix consists of rows which all have the same number of columns
    Every element is a python number.Number; booleans are excluded.
    """

    def __init__(self, matrix: Sequence[Sequence[Number]])-> None:
        num_rows = len(matrix)
        assert num_rows > 0, 'matrix cannot be empty'
        num_cols = len(matrix[0])
        assert num_cols > 0, 'matrix rows cannot be empty'
        assert all(len(row) == num_cols for row in matrix), \
            'all rows must have the same length'

        self.shape = MatrixShape(num_rows=num_rows, num_cols=num_cols)
        self.matrix = [[0 for dummy_c in range(num_cols)]
                       for dummy_r in range(num_rows)]
        for row in range(num_rows):
            for col in range(num_cols):
                elt = matrix[row][col]
                try:
                    _ = elt + 1        # testing if elt is a number
                except TypeError:
                    raise(TypeError, 'all elements must be numbers')
                try:
                    assert elt is not True
                    assert elt is not False
                except AssertionError:
                    raise(TypeError, 'no boolean allowed')
                self.matrix[row][col] = elt

    def __getitem__(self, rowcol:
                    Tuple[Union[int, slice], Union[int, slice]])-> Number:
        row, col = rowcol
        return self.matrix[row][col]

    def __setitem__(self, rowcol:
                    Tuple[Union[int, slice], Union[int, slice]],
                    value: Number)-> None:
        row, col = rowcol
        self.matrix[row][col] = value

    def __eq__(self, other: 'Matrix')-> bool:
        """equality for floats tested to 9 decimal places
        :param other: Matrix
        :return: True if the two matrices are equal
        """
        assert isinstance(other, Matrix)
        if self.shape == other.shape:
            return all(all(math.isclose(selt, oelt)
                           for selt, oelt in zip(srow, orow))
                       for srow, orow in zip(self.matrix, other.matrix))
        return False

    def __add__(self, other: 'Matrix')-> 'Matrix':
        """adds two matrices of same shape
        :param other: a matrix of shape identical to self
        :return: a new matrix of same shape as self and other, for which
        each element is the sum of the corresponding elements in self and other
        """
        assert isinstance(other, Matrix)
        assert self.shape == other.shape, 'matrices must be of same shapes'
        matrix = [[selt + oelt for selt, oelt in zip(srow, orow)]
                  for srow, orow in zip(self.matrix, other.matrix)]
        return Matrix(matrix)

    def __sub__(self, other: 'Matrix')-> 'Matrix':
        """subtract other from self where the two matrices have the same shape
        :param other: a matrix of shape identical to self
        :return: a new matrix of same shape as self and other, for which
        each element is the subtraction of the element from other from
        the element from self
        """
        assert isinstance(other, Matrix)
        assert self.shape == other.shape, 'matrices must be of same shapes'
        matrix = [[selt - oelt for selt, oelt in zip(srow, orow)]
                  for srow, orow in zip(self.matrix, other.matrix)]
        return Matrix(matrix)

    def __matmul__(self, other: 'Matrix')-> 'Matrix':
        """
        multiplies self with another Matrix.
        self is m x k, other is k x n, resulting matrix is m x n [row x col]
        :param other: a (k x n) Matrix where k == self number of columns
        :return: an m x n Matrix
        """
        k = self.shape.num_cols
        assert k == other.shape.num_rows, 'the shapes do not fit multiplication'
        res_rows = self.shape.num_rows
        res_cols = other.shape.num_cols
        res = [[0 for dummy_c in range(res_cols)] for dummy_r in range(res_rows)]
        for row in range(res_rows):
            for col in range(res_cols):
                for kdx in range(k):
                    res[row][col] += self.matrix[row][kdx] * other.matrix[kdx][col]
        return Matrix(res)

    def transpose(self)-> 'Matrix':
        """returns a new matrix corresponding to the transpose of self
        """
        return Matrix(list(map(list, zip(*self.matrix))))

    T = transpose

    def __abs__(self)-> 'Matrix':
        """returns a new matrix of same shape where each element is equal
        to its absolute value
        """
        return Matrix([[abs(elt) for elt in row] for row in self.matrix])

    def scale(self, scalar: Number)-> 'Matrix':
        """scales (multiplies) each element of self by scalar
        :param scalar: a Number
        :return: a new matrix representing a scaled version of self
        """
        if math.isclose(scalar, 0.0):
            return zeros(self.shape)
        if math.isclose(scalar, 1.0):
            return self.clone()
        return Matrix([[elt * scalar for elt in row] for row in self.matrix])

    def clone(self)-> 'Matrix':
        """
        clones self (deepcopy)
        :return: a new Matrix, copy of self
        """
        return Matrix(self.matrix)

    def summation(self)-> 'Number':
        """
        Sums the Elements in Matrix and returns them
        -----------------------------
        ATTENTION: use instance.sum(), not sum(instance)
        -----------------------------
        :return: the sum of the elements of self, a Number
        """
        return sum(sum(row) for row in self.matrix)

    def __str__(self):
        width = max(len(str(elt)) for row in self.matrix for elt in row)
        res = ['[']
        for r, row in enumerate(self.matrix):
            row_res = ['[']
            for elt in row:
                row_res.append(f"{' ' * (width - len(str(elt)))}{str(elt)}")
                row_res.append(', ')
            row_res.pop()
            row_res.append(']')
            if r < self.shape.num_rows - 1:
                row_res.append(',\n ')
            res.append(''.join(row_res))
        res.append(']')
        return ''.join(res)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.matrix})"


def identity(shape: Union[Tuple, MatrixShape])-> Matrix:
    """factory that builds and returns an identity matrix of given shape
    :param shape: Tuple or MatrixShape (num_rows, num_cols)
    :return: identity matrix of shape num_rows, num_cols
    """
    num_rows, num_cols = shape
    assert num_rows == num_cols, 'identity matrix must be square'
    return Matrix([[1 if row == col else 0 for col in range(num_cols)]
                   for row in range(num_rows)])


def zeros(shape: Union[Tuple, MatrixShape])-> Matrix:
    """factory that builds and returns a matrix of zeros of given shape
    :param shape: Tuple or MatrixShape (num_rows, num_cols)
    :return: zero matrix of shape num_rows, num_cols
    """
    num_rows, num_cols = shape
    return Matrix([[0 for dummy_c in range(num_cols)]
                   for dummy_r in range(num_rows)])


class MatrixComplex(Matrix):
    """
    a class to deal with matrices of complex numbers.
    a specialization to avoid complicating the __eq__ tests in the base class
    """
    def __init__(self, matrix: Sequence[Sequence[Number]]) -> None:
        raise NotImplementedError


if __name__ == '__main__':

    E21 = Matrix([[1, 0, 0],
                  [-3, 1, 0],
                  [0, 0, 1]])

    E32 = Matrix([[1, 0, 0],
                  [0, 1, 0],
                  [0, -2, 1]])

    A = E32 @ E21
    print(A.matrix)

    B = Matrix([[1, 2, 1],
                [3, 8, 1],
                [0, 4, 1]])

    expectedU = Matrix([[1, 2, 1],
                        [0, 2, -2],
                        [0, 0, 5]])

    U = A @ B
    print(U.matrix)
    assert U == expectedU

    print('\n\n')

    # permutation rows --> left hand operation

    PR = Matrix([[0, 1],
                 [1, 0]])

    TPR = Matrix([[-2, 13],
                 [-4, 15]])

    expectedPermutatedR = Matrix([[-4, 15],
                                  [-2, 13]])

    actualPermutatedR = PR @ TPR
    print(actualPermutatedR.matrix)

    assert expectedPermutatedR == actualPermutatedR

    # --------------------------------------------
    # permutation columns --> right hand operation

    TP = Matrix([[-2, 13],
                 [-4, 15]])

    P = Matrix([[0, 1], [1, 0]])

    expectedPermutated = Matrix([[13, -2],
                                 [15, -4]])

    actualPermutated = TP @ P
    print(actualPermutated.matrix)

    assert expectedPermutated == actualPermutated



