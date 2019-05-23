'''
    Given a non-empty array of integers, every element appears twice except for one. Find that single one.

    Note:

    Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

    Example 1:

    Input: [2,2,1]
    Output: 1
    Example 2:

    Input: [4,1,2,1,2]
    Output: 4
'''

def singleNumber(nums):
    a = 0
    for i in nums:
        a ^= i
    return a
    # Time complexity : O(n)O(n). We only iterate through \text{nums}nums, so the time complexity is the number of elements in \text{nums}nums.
    # Space complexity : O(1)O(1).

    # or
    # return 2 * sum(set(nums)) - sum(nums)
    ''''
    2∗(a+b+c)−(a+a+b+b+c)=c
    Time complexity : O(n + n) = O(n)O(n+n)=O(n). sum will call next to iterate through \text{nums}nums. We can see it as sum(list(i, for i in nums)) which means the time complexity is O(n)O(n) because of the number of elements(nn) in \text{nums}nums.
    Space complexity : O(n + n) = O(n)O(n+n)=O(n). set needs space for the elements in nums 
    '''
