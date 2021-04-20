import sys


# Function to find the maximum sum `k × k` submatrix
def findMaxSumSubMatrix(mat, k):
    # `M × N` matrix
    (M, N) = (len(mat), len(mat[0]))

    # preprocess the input matrix such that `sum[i][j]` stores
    # sum of elements in the matrix from `(0, 0)` to `(i, j)`
    sum = [[0 for x in range(N)] for y in range(M)]
    sum[0][0] = mat[0][0]

    # preprocess the first row
    for j in range(1, N):
        sum[0][j] = mat[0][j] + sum[0][j - 1]

    # preprocess the first column
    for i in range(1, M):
        sum[i][0] = mat[i][0] + sum[i - 1][0]

    # preprocess the rest of the matrix
    for i in range(1, M):
        for j in range(1, N):
            sum[i][j] = mat[i][j] + sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1]

    max = -sys.maxsize

    # find the maximum sum submatrix

    # start from cell `(k-1, k-1)` and consider each
    # submatrix of size `k × k`
    for i in range(k - 1, M):
        for j in range(k - 1, N):

            # Note that `(i, j)` is the bottom-right corner coordinates of the
            # square submatrix of size `k`

            total = sum[i][j]
            if i - k >= 0:
                total = total - sum[i - k][j]

            if j - k >= 0:
                total = total - sum[i][j - k]

            if i - k >= 0 and j - k >= 0:
                total = total + sum[i - k][j - k]

            if total > max:
                max = total
                p = (i, j)
    print(p)
    # returns coordinates of the bottom-right corner of the submatrix
    return p


if __name__ == '__main__':

    # 5 × 5 matrix
    mat = [
        [3, -4, 6, -5, 1],
        [1, -2, 8, -4, -2],
        [3, -8, 9, 3, 1],
        [-7, 3, 4, 2, 7],
        [-3, 7, -5, 7, -6]
    ]

    # submatrix size
    k = 3

    # `p` contains bottom-right corner coordinates of the submatrix
    (x, y) = findMaxSumSubMatrix(mat, k)

    # print maximum sum submatrix
    for i in range(k):
        for j in range(k):
            print(mat[i + x - k + 1][j + y - k + 1], end=' ')
        print()
