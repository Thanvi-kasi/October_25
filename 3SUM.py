class Solution:
    def threeSum(self, nums):
        # Sort the array to make two-pointer approach work
        nums.sort()
        result = []
        
        # Iterate through the array
        for i in range(len(nums) - 2):
            # Skip duplicates to ensure we don't get the same triplet multiple times
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Set the two pointers
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1  # We need a larger sum, so move the left pointer to the right
                elif total > 0:
                    right -= 1  # We need a smaller sum, so move the right pointer to the left
                else:
                    # Found a triplet that sums to zero
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1
        
        return result
