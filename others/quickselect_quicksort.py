def quickselect(nums, k):
    """
    return kth largest number in the array
    k starts from 1 (smallest number is 1st)
    1 <= k <= len(nums)
    """

    k -= 1 # k starts from 0

    def partition(start, end):
        # index end is not included 
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
            return partition(start, i)

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
    print(quicksort(nums))
