# variant: maxmize the smallest sum among m subarrays

def splitArray(nums, m):
    upper = sum(nums)
    lower = min(nums)
    while lower < upper:
        mid = (lower + upper + 1) // 2
        if isSplitValid(nums, m, mid):
            lower = mid
        else:
            upper = mid - 1
                
    return lower
        
def isSplitValid(nums, m, limit):
    count = 1
    curr_sum = 0
        
    for num in nums:
        curr_sum += num
        if curr_sum >= limit:
            curr_sum = 0
            count += 1
            if count > m:
                return True
                
    return False

if __name__ == "__main__":
    l = [7, 2, 5, 10, 8]
    m = 4
    print(splitArray(l, m))
