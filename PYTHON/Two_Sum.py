nums = [3,0,0,8,0,4,0,7,2,3,3]
target = 6
prevMap={}
for i in range(0,len(nums)):
    diff = target - nums[i]
    if diff in prevMap :
         print([prevMap[diff],i])
    prevMap[nums[i]] = i











# Brute Force -> O(n^2)
# nums = [3,2,4]
# target = 6
# for i in range(0,len(nums)):
#     for j in range(i+1,len(nums)):
#         if(nums[i]+nums[j]==target):
#             print(i,j)