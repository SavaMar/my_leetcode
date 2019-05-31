# Given an integer, write a function to determine if it is a power of three.

# Example 1:

# Input: 27
# Output: true
# Example 2:

# Input: 0
# Output: false
# Example 3:

# Input: 9
# Output: true
# Example 4:

# Input: 45
# Output: false
# Follow up:
# Could you do it without using any loop / recursion?

# my solution #1
def isPowerOfThree(n):
    i = 3
    while i < n:
        i *= 3
    if i == n or n == 1:
        return True
    return False

# my solution #2 (not allowed import math in LeetCode)
# if math.log(n,3) % 1 == 0
import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 0 : return False
        return int(math.log(n,3)) == float(math.log(n,3))

math.log10(n) / math.log10(3)
#
# biggest number 32bit system and only positive
# 2**32/2 - 1 
# 3**19 % n == 0