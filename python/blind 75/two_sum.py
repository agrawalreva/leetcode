class Solution:
  def twoSum(self, nums, target):
      # Create a dict to store the numbers and their indices
      num_indices = {}
      for i, num in enumerate(nums):
          # Calculate the complement of the current number
          complement = target - num
          # If the complement is found in the dict, return the indices
          if complement in num_indices:
              return [num_indices[complement], i]
          # Otherwise, add the number and its index to the dict
          num_indices[num] = i


solution = Solution()
print("Output:", solution.twoSum([3, 2, 4], 6)) 
print("Output:", solution.twoSum([-1, -2, -3, -4, -5], -8)) 

# Time Complexity = O(n)
# Space Complexity = O(n)