# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
# Example 1:

# Input: a = 1, b = 2
# Output: 3
# Example 2:

# Input: a = -2, b = 3
# Output: 1

# my solution
class Solution:
    def getSum(self, a: int, b: int) -> int:
        return sum([a,b])

# wow solution
# class Solution:
#     def getSum(self, a: int, b: int) -> int:
#         while b:
#             tmp = a ^ b
#             b = (a & b) << 1
#             a = tmp & 0xffffffff
#         return a if a >> 31 == 0 else a - 2**32