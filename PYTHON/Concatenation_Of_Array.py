class Solution(object):
    def getConcatenation(self, nums):
        new_nums = nums
        for i in range(0,len(nums),1):
            new_nums.append(nums[i])
        return new_nums


nums = [1, 2, 3, 4, 5]

sol = Solution()
print(sol.getConcatenation(nums))



# alternate solve:
# class Solution(object):
#     def getConcatenation(self, nums):
#         return nums + nums