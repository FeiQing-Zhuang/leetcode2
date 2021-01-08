class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a=nums[0:len(nums)-k]
        b=nums[len(nums)-k:len(nums)]
        nums[0:k-1]=b
        nums[k:len(nums)]=a