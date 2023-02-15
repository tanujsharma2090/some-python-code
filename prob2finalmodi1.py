def fibonacciN(number):
    matrix1 = [[0, 1], [1, 1]]
    if number == 0:  # if power given is zero then zero will be returned
        return 0
    
    fibonacciN(number//2)
    multiply(matrix1,matrix1)
    if number % 2 != 0:
        matrix2 = [[0, 1], [1, 1]]
        multiply(matrix1, matrix2)
    return matrix1[1][1]

def multiply(matrix1, matrix2):

    a = (matrix1[0][0]*matrix2[0][0] + matrix1[0][1] * matrix2[1][0])  # multiply matrice by itself
    b = (matrix1[0][0]*matrix2[0][1] + matrix1[0][1] * matrix2[1][1])
    c = (matrix1[1][0]*matrix2[0][0] + matrix1[1][1] * matrix2[1][0])
    d = (matrix1[1][0]*matrix2[0][1] + matrix1[1][1] * matrix2[1][1])

    matrix1[0][0] = a  # updating the values of matrix as from calculated above
    matrix1[0][1] = b
    matrix1[1][0] = c
    matrix1[1][1] = d

b = int(input("Enter the number whose Fibonacci value to found:"))
a = fibonacciN(b)
print("The value at", b, "position is", a)