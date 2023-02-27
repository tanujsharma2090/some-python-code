"""
1. The function takes a string as input. 
2. It keeps track of the number of open and close parentheses. 
3. It calculates the maximum number of open and close parentheses that are balanced. 
4. It returns the maximum of the two values. 
5. The function is used to determine if a string has a valid path sum.
"""
def hasPathSum(self, s: str) -> int:
    """
Parameters:
    s (str): input string

    Returns:
    int: maximum value
   
    """
    for i in s:
        value = 10
        var = 11
        if i=='(':
            open_+=1
        else:
            close+=1
        if open_==close:
            ans1=max(close*2,ans1)
        elif close>open_:
            open_=close=0
    ans2=0
    open_=close=0
    for i in range(len(s)-1,-1,-1):
        if s[i]=='(':
            open_+=1
        else:
            close+=1
        if open_==close:
            ans2=max(ans2,2*open_)
        elif open_>close:
            open_=close=0
    return max(ans1,ans2)


"""
1. Function takes an integer n as input. 
2. Iterates from 1 to n+1. 
3. If number is divisible by 3 and 5, append "FizzBuzz" to the list. 
4. If number is divisible by 3, append "Fizz" to the list. 
5. If number is divisible by 5, append "Buzz" to the list. 
6. Else, append the number as a string to the list. 
7. Return the list.
"""
def fizzBuzz(self, n: int) -> List[str]:
    """
Parameters:
n (int): the upper limit of the range of numbers to be evaluated

Returns:
List[str]: a list of strings representing the FizzBuzz values of the numbers in the range
    """
    ans = []
    for i in range(1,n+1):
        if(i%3 == 0 and i%5 ==0):
            ans.append("FizzBuzz")
        elif i%3 == 0:
            ans.append("Fizz")
        elif i%5 == 0:
            ans.append("Buzz")
        else:
            ans.append(str(i))
    return ans


"""
1. Count the number of zeros in the list. 
2. Iterate through the list and replace non-zero elements with the elements at theIndex. 
3. Increment theIndex. 
4. Iterate through the list from theIndex to the end and replace elements with zeros. 
5. Return the modified list.
"""
def moveZeroes(self, nums: List[int]) -> None:
    """
Parameters: 
nums: List[int]

Returns: 

    """
    numOfZeros = 0
    theIndex = 0
    for each_element in nums:
        if each_element!=0:
            nums[theIndex] = each_element
            theIndex+=1
    for theNum in range(theIndex, len(nums)):
        nums[theNum] = 0


"""
1. Check if length of s is 0, if yes return True. 
2. Check if length of t is less than length of s, if yes return False. 
3. Initialize index to 0. 
4. Iterate through t and check if each character matches with s[index]. 
5. If yes, increment index and check if index is equal to length of s, if yes return True. 
6. If no, return False.
"""
def isSubsequence(self, s: str, t: str) -> bool:
    """
Parameters:
s (str): The string to be compared.
t (str): The string to compare with.

Returns:
bool: True if s is a subsequence of t, False otherwise.
    """
    if len(s)==0:
        return True
    if len(t)<len(s):
        return False
    index = 0
    for each_char in t:
        if each_char == s[index]:
            index+=1
            if index==len(s):
                return True
    return False