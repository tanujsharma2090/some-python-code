"""
1. Sort the words by length
2. Iterate over the words
3. For each word, check if it is a substring of any other word
4. If it is, add it to the output list
5. Return the set of all the words that are substrings of other words

"""
def fib(self, words):
    words.sort(key = len) 
    print(words)
    
    out = []
    
    for i in range(0, len(words)):
        for j in range(i+1, len(words)):
            if words[i] in words[j]:
                out.append(words[i])
    
    return set(out)


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