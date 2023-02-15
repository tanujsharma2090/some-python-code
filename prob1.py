def npower(e, a):
    if a == 1:
        return(e)  # if value of N is 1 return the input itself
    elif a % 2 == 0:
        y = npower(e, a/2)  # divide in recursion till smallest value i.e 1
        return y*y
    else:
        return e*npower(e, a-1)  # for the odd case


e = float(input("Enter value of e between 0 and 0.1: "))  # Enter value of e
if e >= -0.1 and e <=0.1: # e should be between -0.1 and +0.1 only
    e = e + 1
    exp = input("Enter value of N: ")  # Enter value of N
    a = int(exp)
    value = npower(e, a)
    c = "The result is {:.11f}"  # Limiting decimal to 11 place
    print(c.format(value))
else:
    print("Please enter value of e between 0 and 0.1 only")

