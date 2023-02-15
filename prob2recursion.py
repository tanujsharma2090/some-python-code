def fib(n):

    F = [[1, 1],
         [1, 0]]
    if (n == 0):
        return 0
    power(F, n - 1)

    return F[0][0]


def multiply(F, M):

    x = (F[0][0] * M[0][0] +
         F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] +
         F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] +
         F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] +
         F[1][1] * M[1][1])

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w

# Optimized version of
# power() in method 4


def power(F, n):

    if(n == 0 or n == 1):
        return 0

    power(F, n // 2)
    multiply(F, F)
    M = [[1, 1], [1, 0]]
    if (n % 2 != 0):
        multiply(F, M)


print(fib(int(input("Enter a number:"))))
