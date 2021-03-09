#!/Users/fredericdupont/anaconda3/envs/py38/bin/python3

"""
inverse3x3.py

https://stackoverflow.com/questions/983999/simple-3x3-matrix-inverse-code-c
https://stackoverflow.com/questions/1148309/inverting-a-4x4-matrix/44446912#44446912
https://github.com/willnode/N-Matrix-Programmer

"""


def inverse2x2(mat):

    a, b, c, d = mat[0][0], mat[0][1], mat[1][0], mat[1][1]
    det = a*d - b*c

    if det == 0:
        return False

    invdet = 1/ det
    return [[d*invdet, -b*invdet],
            [-c*invdet, a*invdet]]


def inverse3x3(mat):

    m = []
    for row in mat:
        m += row

    inv = [0] * 9

    inv[0] =  (m[4] * m[8] - m[5] * m[7])
    inv[3] = -(m[3] * m[8] - m[5] * m[6])
    inv[6] =  (m[3] * m[7] - m[4] * m[6])

    det = m[0] * inv[0] + m[1] * inv[3] + m[2] * inv[6]
    print(f'determinant: {det}')
    if det == 0:
        return False

    inv[1] = -(m[1] * m[8] - m[2] * m[7])
    inv[4] =  (m[0] * m[8] - m[2] * m[6])
    inv[7] = -(m[0] * m[7] - m[1] * m[6])
    inv[2] =  (m[1] * m[5] - m[2] * m[4])
    inv[5] = -(m[0] * m[5] - m[2] * m[3])
    inv[8] =  (m[0] * m[4] - m[1] * m[3])


    det2 = (m[0]*m[4]*m[8] + m[1]*m[5]*m[6] + m[2]*m[3]*m[7]) -\
          (m[2]*m[4]*m[6] + m[1]*m[3]*m[8] + m[0]*m[5]*m[7])
    assert det == det2, "determinants not equals"

    invdet = 1 / det
    invOut = [0] * 9

    for i in range(9):
        invOut[i] = inv[i] * invdet

    return unflatten(invOut, n=3)


def unflatten(iter, n=2):
    """Group iter into tuples of length n. Raise an error if
    the length of iter is not a multiple of n.
    """
    if n < 1 or len(iter) % n:
        raise ValueError(f'iter length is not a multiple of {n}')

    return [list(row) for row in zip(*(iter[i::n] for i in range(n)))]


if __name__ == '__main__':


    A = [[1, 2], [3, 4]]
    print(inverse2x2(A))

    A = [[1, -2], [-3, 4]]
    print(inverse2x2(A))


    A = [[1, 2, 3],
         [0, 4, 5],
         [1, 0, 6]]
    print(inverse3x3(A))

    B = [[1, 2, 3],
         [0, 1, 4],
         [5, 6, 0]]
    print(inverse3x3(B))

    C = [[1, -3, 9],
         [1, 1, -5],
         [-1, 1, -1]]
    print(inverse3x3(C))






























