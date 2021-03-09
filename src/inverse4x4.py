#!/Users/fredericdupont/anaconda3/envs/py38/bin/python3

"""
inverse4x4.py

https://stackoverflow.com/questions/983999/simple-3x3-matrix-inverse-code-c
https://stackoverflow.com/questions/1148309/inverting-a-4x4-matrix/44446912#44446912
https://github.com/willnode/N-Matrix-Programmer

"""


def inverse4x4(mat):

    # double inv[16], det;
    # int i;

    m = []
    for row in mat:
        m += row

    inv = [0] * 16

    inv[0]  =  m[5]  * m[10] * m[15] -\
               m[5]  * m[11] * m[14] -\
               m[9]  * m[6]  * m[15] +\
               m[9]  * m[7]  * m[14] +\
               m[13] * m[6]  * m[11] -\
               m[13] * m[7]  * m[10]

    inv[4]  = -m[4]  * m[10] * m[15] +\
               m[4]  * m[11] * m[14] +\
               m[8]  * m[6]  * m[15] -\
               m[8]  * m[7]  * m[14] -\
               m[12] * m[6]  * m[11] +\
               m[12] * m[7]  * m[10]

    inv[8]  =  m[4]  * m[9]  * m[15] -\
               m[4]  * m[11] * m[13] -\
               m[8]  * m[5]  * m[15] +\
               m[8]  * m[7]  * m[13] +\
               m[12] * m[5]  * m[11] -\
               m[12] * m[7]  * m[9]

    inv[12] = -m[4]  * m[9]  * m[14] +\
               m[4]  * m[10] * m[13] +\
               m[8]  * m[5]  * m[14] -\
               m[8]  * m[6]  * m[13] -\
               m[12] * m[5]  * m[10] +\
               m[12] * m[6]  * m[9]

    det = m[0] * inv[0] + m[1] * inv[4] + m[2] * inv[8] + m[3] * inv[12]
    if det == 0:
        return False

    inv[1]  = -m[1]  * m[10] * m[15] +\
               m[1]  * m[11] * m[14] +\
               m[9]  * m[2]  * m[15] -\
               m[9]  * m[3]  * m[14] -\
               m[13] * m[2]  * m[11] +\
               m[13] * m[3]  * m[10]

    inv[5]  =  m[0]  * m[10] * m[15] -\
               m[0]  * m[11] * m[14] -\
               m[8]  * m[2]  * m[15] +\
               m[8]  * m[3]  * m[14] +\
               m[12] * m[2]  * m[11] -\
               m[12] * m[3]  * m[10]

    inv[9]  = -m[0]  * m[9]  * m[15] +\
               m[0]  * m[11] * m[13] +\
               m[8]  * m[1]  * m[15] -\
               m[8]  * m[3]  * m[13] -\
               m[12] * m[1]  * m[11] +\
               m[12] * m[3]  * m[9]

    inv[13] =  m[0]  * m[9]  * m[14] -\
               m[0]  * m[10] * m[13] -\
               m[8]  * m[1]  * m[14] +\
               m[8]  * m[2]  * m[13] +\
               m[12] * m[1]  * m[10] -\
               m[12] * m[2]  * m[9]

    inv[2]  =  m[1]  * m[6] * m[15] -\
               m[1]  * m[7] * m[14] -\
               m[5]  * m[2] * m[15] +\
               m[5]  * m[3] * m[14] +\
               m[13] * m[2] * m[7]  -\
               m[13] * m[3] * m[6]

    inv[6]  = -m[0]  * m[6] * m[15] +\
               m[0]  * m[7] * m[14] +\
               m[4]  * m[2] * m[15] -\
               m[4]  * m[3] * m[14] -\
               m[12] * m[2] * m[7]  +\
               m[12] * m[3] * m[6]

    inv[10] =  m[0]  * m[5] * m[15] -\
               m[0]  * m[7] * m[13] -\
               m[4]  * m[1] * m[15] +\
               m[4]  * m[3] * m[13] +\
               m[12] * m[1] * m[7]  -\
               m[12] * m[3] * m[5]

    inv[14] = -m[0]  * m[5] * m[14] +\
               m[0]  * m[6] * m[13] +\
               m[4]  * m[1] * m[14] -\
               m[4]  * m[2] * m[13] -\
               m[12] * m[1] * m[6]  +\
               m[12] * m[2] * m[5]

    inv[3]  = -m[1] * m[6] * m[11] +\
               m[1] * m[7] * m[10] +\
               m[5] * m[2] * m[11] -\
               m[5] * m[3] * m[10] -\
               m[9] * m[2] * m[7]  +\
               m[9] * m[3] * m[6]

    inv[7]  =  m[0] * m[6] * m[11] -\
               m[0] * m[7] * m[10] -\
               m[4] * m[2] * m[11] +\
               m[4] * m[3] * m[10] +\
               m[8] * m[2] * m[7]  -\
               m[8] * m[3] * m[6]

    inv[11] = -m[0] * m[5] * m[11] +\
               m[0] * m[7] * m[9]  +\
               m[4] * m[1] * m[11] -\
               m[4] * m[3] * m[9]  -\
               m[8] * m[1] * m[7]  +\
               m[8] * m[3] * m[5]

    inv[15] =  m[0] * m[5] * m[10] -\
               m[0] * m[6] * m[9]  -\
               m[4] * m[1] * m[10] +\
               m[4] * m[2] * m[9]  +\
               m[8] * m[1] * m[6]  -\
               m[8] * m[2] * m[5]

    invdet = 1 / det
    invOut = [0] * 16

    for i in range(16):
        invOut[i] = inv[i] * invdet

    return unflatten(invOut, n=4)


def unflatten(iter, n=2):
    """Group iter into tuples of length n. Raise an error if
    the length of iter is not a multiple of n.
    """
    if n < 1 or len(iter) % n:
        raise ValueError(f'iter length is not a multiple of {n}')

    return [list(row) for row in zip(*(iter[i::n] for i in range(n)))]


if __name__ == '__main__':


    A = [[1, 1, 1, -1],
         [1, 1, -1, 1],
         [1, -1, 1, 1],
         [-1, 1, 1, 1]]

    print(inverse4x4(A))


    B = [[1, 2, 2, 2],
         [2, 1, 1, 1],
         [1, 1, 2, 2],
         [2, 1, 2, 1]]

    print(inverse4x4(B))






























