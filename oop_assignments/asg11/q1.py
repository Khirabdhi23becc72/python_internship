def search_range(nums, target):
    # Helper function to find the boundary index of the target
    def find_bound(is_first):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                # Check if finding the first occurrence
                if is_first:
                    if mid == left or nums[mid - 1] != target:
                        return mid
                    right = mid - 1
                # Check if finding the last occurrence
                else:
                    if mid == right or nums[mid + 1] != target:
                        return mid
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    start = find_bound(True)  # Find the first occurrence
    if start == -1:
        return [-1, -1]  # Target not found
    end = find_bound(False)  # Find the last occurrence
    return [start, end]

# Example usage:
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(search_range(nums, target)) 
