#!/Users/fredericdupont/anaconda3/envs/py38/bin/python3

"""
hommat.py


Homogeneous Matrix
"""

from typing import List


class Hmat33:

    def __init__(self, rows: List[List[float]]) -> None:
        self._mat = [row[:] for row in rows]

    def __matmul__(self, other: 'Hmat33') -> 'Hmat33':
        a, b, c = self._mat[0]
        d, e, f = self._mat[1]
        g, h, i = self._mat[2]
        j, k, l = other._mat[0]
        m, n, o = other._mat[1]
        p, q, r = other._mat[2]
        r0 = [a*j+b*m+c*p, a*k+b*n+c*q, a*l+b*o+c*r]
        r1 = [d*j+e*m+f*p, d*k+e*n+f*q, d*l+e*o+f*r]
        r2 = [g*j+h*m+i*p, g*k+h*n+i*q, g*l+h*o+i*r]
        return Hmat33([r0, r1, r2])

    def __mul__(self, vec):
        """multiplies 3x3 matrix with 3x1 point or vector
        returns a point or vector
        """
        a, b, c = self._mat[0]
        d, e, f = self._mat[1]
        g, h, i = self._mat[2]
        x, y, z = vec
        return (a*x+b*y+c*z, d*x+e*y+f*z, g*x+h*y+i*z)

    def __eq__(self, other: 'Hmat33') -> bool:
        for row in range(3):
            for col in range(3):
                if self._mat[row][col] != other._mat[row][col]:
                    return False
        return True

    def __str__(self):
        return '\n'.join([' '.join([str(elt) for elt in row]) for row in self._mat]) + '\n'


if __name__ == '__main__':

    I = Hmat33([[1, 0, 0],
                [0, 1, 0],
                [0, 0, 1]])

    A = Hmat33([[1, 2, 3],
                [1, 2, 3],
                [1, 2, 3]])

    O = Hmat33([[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]])

    B = Hmat33([[10, 0, 200],
                [0, -10, 200],
                [0, 0, 1]])

    C = Hmat33([[1, 0, 200],
                [0, -1, 200],
                [0, 0, 1]])


    print(A@I)
    print(I@A)
    print(A@O)
    print(O@A)


    vecs = [(10, 20, 1), (0, 0, 1), (-50, -50, 1), (-50, 50, 1), (1.5, 2.5, 1)]

    for vec in vecs:
        print(vec, C * vec)

    print()

    for vec in vecs:
        print(vec, B * vec)


















