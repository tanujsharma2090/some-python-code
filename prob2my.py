def fibonacci(N):
    F = [[0, 1], [1, 1]]
    if N == 0:
        return 0
    else:
        power(F, N-1)

    return F[1][1]


def power(F, N):
    M = [[0, 1], [1, 1]]

    for i in range(1, N):
        multiply(F, M)
        i += 1


def multiply(F, M):

    x = (F[0][0] * M[0][0] + F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] + F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] + F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] + F[1][1] * M[1][1])

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w


print(fibonacci(int(input("Enter the value of N:"))))
