class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        if k == 0: return

        temp = nums[-k:]
        nums[k:] = nums[:-k]
        nums[:k] = temp