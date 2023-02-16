"""
1. It is creating a 2x2 matrix F. 
2. It is raising the matrix to the (n-1)th power. 
3. It is returning the element at row 0 and column 0 of the resultant matrix. 

"""
def fib(n):
    F = [[1, 1], [1, 0]]
    if (n == 0):
        return 0
    else:
        power(F, n - 1)

    a = F[0][0]
    b = str(a)
    print(len(b))
    return F[0][0]


"""
1. It is multiplying the matrix F with itself. 
2. It is storing the result in the same matrix F. 
3. It is doing this in O(1) space. 
4. It is doing this in O(log n) time. 
5. It is doing this by using the fact that F^n = F^(n/2) * F^(n/2) if n is even. 

"""
def multiply(F, M):

    x = (F[0][0] * M[0][0] + F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] + F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] + F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] + F[1][1] * M[1][1])

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w


"""
1. The function is taking the nth fibonacci number as input. 
2. It is creating a matrix M = [[1, 1], [1, 0]]
3. It is multiplying the matrix M with itself n-1 times. 
4. It is returning the first element of the matrix M. 

"""
def power(F, n):

    M = [[1, 1], [1, 0]]

    # n - 1 times multiply the
    # matrix to {{1,0},{0,1}}
    for i in range(1, n):
        #    print("value of i", i)
        multiply(F, M)
        i += 1


print(fib(int(input("Enter a number:"))))
