def fibonacciN(number):
    matrix1 = [[0, 1], [1, 1]]
    if number == 0:  # if power given is zero then zero will be returned
        return 0  # if value of N is 1 return the input itself
    elif a % 2 == 0:
        y = npower(e, a/2)  # divide in recursion till smallest value i.e 1
        return y*y
    else:
        return e*npower(e, a-1)
