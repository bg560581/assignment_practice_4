# from functools import reduce

myList = 1,2,3,4,5,6,7,8,9,10
myList2 = [1,2,3,4,5,6,7,8,9,10]
myRange = range(0, 10, 1)


def max_num(myList): 
    return max(myList)

# Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(myList2):
    product = 1
    for i in myList2:
        product = product * i
    return product

# Write a Python function called rev_string() to reverse a string.

x = 'this is a string'
def rev_string(x):
    return x[::-1]

# Write a Python function called num_within() to check whether a number falls in a given range.

def numWithin(a,b,c):
    return a in range(b, c+1)

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.

n = 5
def pascal(n):
   for i in range(n+1):
      for j in range(n-i):
         print(' ', end='')

      C = 1
      for j in range(1, i+1):
         print(C, ' ', sep='', end='')
         C = C * (i - j) // j
      print()



print(mult_list(myList2))
print(max_num(myList))
print(rev_string(x))
print(numWithin(2,4,6))
pascal(n)













