class Solution(object):
    def func(self, nums):
         if(len(nums)!=len(set(nums))):
              return True
         else:
              return False




nums = [1,2,3,4,5,1]
sol = Solution()
print(sol.func(nums))








# O(n^2)
# class Solution(object):
#     def func(self, nums):
#          c = False
#          for num in nums:
#             if nums.count(num)>1:
#                 c = True
#                 break
#          return c




# nums = [1,2,3,4,5]
# sol = Solution()
# print(sol.func(nums))