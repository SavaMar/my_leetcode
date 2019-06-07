class Solution:
    def fizzBuzz(self, n):
        list = []
        for i in range(1,n+1):
            buff_string = ""
            if i % 3 == 0:
                buff_string += "Fizz"
            if i % 5 == 0:
                buff_string += "Buzz"
            if buff_string == '':
                buff_string = str(i)
            list.append(buff_string)
        return list