a = [0,0,1,1,1,2,2,3,3,4,4,4,4,5]

def removeDuplicates(nums):
  nu = 0
  for i in range(1, len(nums)):
    if nums[nu] == nums[nu+1]:
      del a[nu+1]
    else:
      nu+=1
  return nums

print(removeDuplicates(a))
