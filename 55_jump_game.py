class Solution:
    def canJump(self, nums: list[int]) -> bool:

        farthest = 0
        for i, n in enumerate(nums):
            if i > farthest: # Если текущий индекс недостижим
                return False
            farthest = max(farthest, i + n) # Обновляем дальность прыжка
            if farthest >= len(nums) - 1: # Если можем достичь последнего индекса
                return True
print(Solution().canJump([2,3,1,1,4]))
