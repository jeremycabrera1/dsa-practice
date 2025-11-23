def removeElement(nums, val):
    slow = 0

    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
        slow += 1

    return slow

nums = [0,1,2,2,3,0,4,2]
val = 2

print(removeElement(nums, val))