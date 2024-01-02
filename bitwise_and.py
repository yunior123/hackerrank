# let arr= [10,7,2,8,3 ]
# there are 6 unordered pairs of its elements that have 
# a bitwise AND that is a power of 2:
# 10 & 7 = 2 is power of 2
# 10 & 2 = 2    is power of 2
# 10 & 8 = 8    is power of 2
# 10 & 3 = 2    is power of 2
# 7 & 2 = 2 is power of 2
# 2  & 3 = 2 is power of 2
def countPairs(arr):
    # Write your code here
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] & arr[j] != 0 and (arr[i] & arr[j]) & ((arr[i] & arr[j])-1) == 0:
                count += 1
    return count

def countPairs1(arr):
    return sum([1 for i in range(len(arr)) for j in range(i+1, len(arr)) if arr[i] & arr[j] != 0 and (arr[i] & arr[j]) & ((arr[i] & arr[j])-1) == 0])

def countPairs2(arr):
    res = 0
    for i in range(1, 31):
        count = 0
        for j in range(len(arr)):
            if arr[j] & (1 << i):
                count += 1
        res += count * (count - 1) // 2
    return res

def countPairs3(arr):
    res = 0
    for i in range(1, 31):
        count = 0
        for j in range(len(arr)):
            if arr[j] & (1 << i):
                count += 1
        res += count * (count - 1) // 2
    return res