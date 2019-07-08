a = [1,2,7]
b = [9,9,9]

def plus_one(digits):
  # a = int("".join(str(nu) for nu in digits)) + 1
  # return [int(ni) for ni in str(a)]
  digits[-1] += 1
  for i in range(len(digits)-1, 0, -1):
      if digits[i] != 10:
          break
      digits[i] = 0
      digits[i-1] += 1

  if digits[0] == 10:
      digits[0] = 0
      return [1] + digits
  return digits

print(plus_one(a))
print(plus_one(b))