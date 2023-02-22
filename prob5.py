def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
    area = 0
    corners = set()
    a = lambda: (Y-y) * (X-x)
    
    for x, y, X, Y in rectangles:
        area += a()
        corners ^= {(x,y), (x,Y), (X,y), (X,Y)}

    if len(corners) != 4: return False
    x, y = min(corners, key=lambda x: x[0] + x[1])
    X, Y = max(corners, key=lambda x: x[0] + x[1])
    return a() == area


def nextPermutation(self, nums: List[int]) -> None:
    for curr in reversed(range(0, len(nums) - 1)):
        if nums[curr] >= nums[curr + 1]:
            continue
            
        next = curr + 1
        while next < len(nums) and nums[next] > nums[curr]:
            next += 1
        
        nums[curr], nums[next - 1] = nums[next - 1], nums[curr];
        
        nums[curr+1:] = reversed(nums[curr+1:])
            
        return nums
                
    return nums.sort()

def doDfs(grid,i,j):
    deq = []
    deq.append([i,j])
    while deq:
        x,y=deq.pop()
        grid[x][y]="v" #visited
        if x+1<len(grid) and grid[x+1][y]=="1":
            deq.append([x+1,y])
        if y+1<len(grid[0]) and grid[x][y+1]=="1":
            deq.append([x,y+1])
        if y-1>=0 and grid[x][y-1]=="1":
            deq.append([x,y-1])
        if x-1>=0 and grid[x-1][y]=="1":
            deq.append([x-1,y])
            
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count= 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    doDfs(grid,i,j)
                    count+=1
        return count
