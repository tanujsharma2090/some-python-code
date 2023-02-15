def fibonacci(N):

    matrix1 = [[0, 1], [1, 1]]
    if N == 0 or N == 1:
        return 0
    else:
        raisepower(matrix1, N-1)

    return matrix1[1][1]


def raisepower(matrix, power):

    if power == 1:
        return matrix

    raisepower(matrix, power//2)
    multiply(matrix, matrix)
    matrix2 = [[0, 1], [1, 1]]

    a = (matrix1[0][0]*matrix2[0][0] + matrix1[0][1] * matrix2[1][0])
    b = (matrix1[0][0]*matrix2[0][1] + matrix1[0][1] * matrix2[1][1])
    c = (matrix1[1][0]*matrix2[0][0] + matrix1[1][1] * matrix2[1][0])
    d = (matrix1[1][0]*matrix2[0][1] + matrix1[1][1] * matrix2[1][1])

    matrix1[0][0] = a
    matrix1[0][1] = b
    matrix1[1][0] = c
    matrix1[1][1] = d

    if (power % 2 != 0):
        a = (matrix1[0][0]*matrix2[0][0] + matrix1[0][1] * matrix2[1][0])
        b = (matrix1[0][0]*matrix2[0][1] + matrix1[0][1] * matrix2[1][1])
        c = (matrix1[1][0]*matrix2[0][0] + matrix1[1][1] * matrix2[1][0])
        d = (matrix1[1][0]*matrix2[0][1] + matrix1[1][1] * matrix2[1][1])

        matrix1[0][0] = a
        matrix1[0][1] = b
        matrix1[1][0] = c
        matrix1[1][1] = d

print(fibonacci(int(input("Enter a number:"))))
