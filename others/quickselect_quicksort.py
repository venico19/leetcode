def quickselect(nums, k):
    """
    return kth smallest number in the array
    k starts from 1 (smallest number is 1st)
    """
    assert(1 <= k <= len(nums))

    k -= 1 # k starts from 0

    def partition(start, end):
        # start is inclusive, end is exclusive
        pivot = nums[start]
        i = start
        for j in range(start + 1, end):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[start], nums[i] = nums[i], nums[start]

        if i == k:
            return nums[i]
        elif i < k:
            return partition(i+1, end)
        else:
            return partition(start, i) # note that end is exclusive, don't use i-1 here

    return partition(0, len(nums))


def quicksort(nums):
    def partition(start, end):

        # stop conditions: empty array or array with single number
        if start + 1 >= end:
            return

        pivot = nums[start]
        i = start
        for j in range(start + 1, end):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[start], nums[i] = nums[i], nums[start]

        partition(start, i)
        partition(i+1, end)
        return

    partition(0, len(nums))
    return nums

if __name__ == '__main__':
    nums = [5,-1,-1,2,4,1,0,7,8]
    print(quickselect(nums, 1))
    print(quickselect(nums, 2))
    print(quickselect(nums, 3))
    print(quickselect(nums, 9))
    print(quicksort(nums))