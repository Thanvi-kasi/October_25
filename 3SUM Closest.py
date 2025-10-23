class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Sort the array to use two pointers technique
        nums.sort()
        
        # Variable to store the closest sum
        closest_sum = float('inf')
        
        # Iterate through the array
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            
            # Use two-pointer technique
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Update closest_sum if the current sum is closer to the target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # If we find the exact target sum, return it
                if current_sum == target:
                    return current_sum
                
                # Move the pointers
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return closest_sum
