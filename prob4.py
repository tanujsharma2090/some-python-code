"""
1. We are iterating through the string from left to right and keeping track of the number of open and close brackets. 
2. If the number of open and close brackets are equal, we update the answer with the maximum of the current answer and the number of open and close brackets. 
3. If the number of close brackets is greater than the number of open brackets, we reset the number of open and close brackets to 0. 
4. We do the same thing from right to left. 
5. We return the maximum of the two answers. 
"""
def hasPathSum(self, s: str) -> int:
    for i in s:
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
1. We are creating an empty list called ans. 
2. We are using a for loop to iterate through the range of 1 to n+1. 
3. We are using an if statement to check if the number is divisible by 3 and 5. 
4. If it is divisible by 3 and 5, we are appending the string "FizzBuzz" to the list ans. 
5. If it is divisible by 3, we are appending the string "Fizz" to the list ans. 
6. If it is divisible by 5, we are appending the string "Buzz" to the list ans. 
7. If it is not divisible by 3 or 5, we are appending the number itself to the list ans. 
8. Finally, we are returning the list ans. 

"""
def fizzBuzz(self, n: int) -> List[str]:
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
1. We are creating a variable called numOfZeros and initializing it to 0. 
2. We are creating a variable called theIndex and initializing it to 0. 
3. We are iterating through the list nums. 
4. If the element is not equal to 0, we are assigning the element to the index of the list. 
5. We are incrementing theIndex by 1. 
6. We are iterating through the list nums again. 
7. We are assigning the value 0 to the index of the list. 

"""
def moveZeroes(self, nums: List[int]) -> None:
    numOfZeros = 0
    theIndex = 0
    for each_element in nums:
        if each_element!=0:
            nums[theIndex] = each_element
            theIndex+=1
    for theNum in range(theIndex, len(nums)):
        nums[theNum] = 0


"""
1. If the length of s is 0, then it is a subsequence of t. 
2. If the length of t is less than the length of s, then it is not a subsequence of t. 
3. We iterate through each character in t. 
4. If the character in t is equal to the character in s at the index, then we increment the index. 
5. If the index is equal to the length of s, then we return True. 
6. If we iterate through the entire string t and the index is not equal to the length of s, then we return False. 

"""
def isSubsequence(self, s: str, t: str) -> bool:
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