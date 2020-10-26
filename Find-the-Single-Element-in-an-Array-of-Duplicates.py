class Solution(object):
    def findSingle(self, nums):
        result = set()
        repeated = set()
        for x in nums:
            if x in result:
                result.discard(x)
                repeated.add(x)
            elif x not in repeated: 
                result.add(x)
        return result.pop()








nums = [1, 1, 3, 4, 4, 5, 6, 5, 6]
print(Solution().findSingle(nums))
# 3