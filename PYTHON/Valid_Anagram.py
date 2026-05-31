class Solution(object):
    def func(self, s, t):
        a = sorted(s)
        b = sorted(t)
        return a==b


s = 'abcd'
t = 'dcba'
sol = Solution()
print(sol.func(s,t))
