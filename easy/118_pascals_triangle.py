# def getSum(key, a, subArray):
#   for d in range(1, a[key-2].__len__()):
#     for l in range(0, d):
#       a[key-1][d] = a[key-2][l] + a[key-2][l+1]  
  
# def generate(numRows):
#   a = []
#   for i in range(1, numRows+1):
#     a.append([1]*i)
#     if i > 2:
#       getSum(i, a, a[i-1])
#   print(a)


# generate(6)
# generate(5)
# generate(7)
# generate(2)

# def generate(self, numRows: int) -> List[List[int]]:
#     a = []
#     for i in range(1, numRows+1):
#         a.append([1]*i)
#         if i > 2:
#             for d in range(1, a[i-2].__len__()):
#                 for l in range(0, d):
#                     a[i-1][d] = a[i-2][l] + a[i-2][l+1]
#     return a

def generate(numRows)
    triangle = []
        for row_n in range(numRows):
            row = [1 for _ in range(row_n+1)]
            for i in range(1, len(row)-1):
                row[i] = triangle[row_n-1][i-1] + triangle[row_n-1][i]
            triangle.append(row)
        return triangle

generate(5)