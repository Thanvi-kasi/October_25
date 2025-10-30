class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Edge case: If the list is empty, return 0
        if not nums:
            return 0
        
        # Pointer for the position to insert the next unique element
        k = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        
        return k
