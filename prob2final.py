def fibonacciN(number):

    # Matrix from which we start our calculation, matrix[1][1] element is the F(n+1) element
    matrix1 = [[0, 1], [1, 1]]
    if number == 0:  # if power given is zero then zero will be returned
        return 0
    else:
        # power reduced by 1 , for the odd power case
        raisepower(matrix1, number-1)

    return matrix1[1][1]


def raisepower(matrix, power):

    # if power was 2, then we get here power = 1 , in that case also F(n) = 1
    if power == 0 or power == 1:
        return matrix

    # Divide by 2, and recursion to be done till we get power = 1
    raisepower(matrix, power//2)
    multiply(matrix, matrix)  # start multiplying with itself
    matrix2 = [[0, 1], [1, 1]]

    if power % 2 != 0:  # for the odd case, have to multiply one more time also
        multiply(matrix, matrix2)


def multiply(matrix1, matrix2):

    a = (matrix1[0][0]*matrix2[0][0] + matrix1[0][1] * matrix2[1][0])  # multiply matrice by itself
    b = (matrix1[0][0]*matrix2[0][1] + matrix1[0][1] * matrix2[1][1])
    c = (matrix1[1][0]*matrix2[0][0] + matrix1[1][1] * matrix2[1][0])
    d = (matrix1[1][0]*matrix2[0][1] + matrix1[1][1] * matrix2[1][1])

    matrix1[0][0] = a  # updating the values of matrix as from calculated above
    matrix1[0][1] = b
    matrix1[1][0] = c
    matrix1[1][1] = d


# Input the number whose Fibonacci value to be found
b = int(input("Enter the number whose Fibonacci value to found:"))
a = fibonacciN(b)
print("The value at", b, "position is", a)  # Output
