def twoSum(nums, target):
    # Map to remember the indices of the numbers we have seen/visted so far
    # Key: number, Value: index
    num_to_index = {}

    # Iterate through the array once, tracking the index and value of each number
    for index, num in enumerate(nums):
        # The value we need to find to reach the target sum
        complement = target - num

        # If the complement is in our map, we have found the two numbers that sum to the target
        if complement in num_to_index:
            return [num_to_index[complement], index]

        # Complement not found yet, so store the current number and its
        # index for future iterations to check against.
        num_to_index[num] = index

    return []

if __name__ == "__main__":
    # Example usage
    nums = [2, 7, 11, 15]
    target = 9
    result = twoSum(nums, target)
    print(f"Indices of the two numbers that add up to {target}: {result}")