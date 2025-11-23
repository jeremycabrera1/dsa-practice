# Problem:
# Given an array of integers numbers and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Return the answer in any order.


def two_sum(numbers: list, target: int) -> list:
    # Create a container for the indeces
    container = {}
    # loop through the numbers using enumerate to get the indexes of the values
    for i, num in enumerate(numbers):
        # Create a complement to check if the pair already exists in the container
        complement = target - num
        # if the pair exists return the index of the complement and the current index we are looping through
        if complement in container:
            return [container[complement], i]
        # if the complement is not in the container add the current index and value to the container to run against in future loops in. key=num and value=i
        container[num] = i
    #if nothing is found return an empty list
    return []