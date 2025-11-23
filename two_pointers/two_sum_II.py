def twoSum(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        elif current_sum > target:
            right -= 1
        

        


numbers = [2,7,11,15]
target = 9

print(twoSum(numbers, target))