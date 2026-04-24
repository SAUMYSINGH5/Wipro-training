"""
Date:23-4-2026
"""
'''
# Functions
def add(n1, n2):
    print(n1)
    print(n2)
    return n1 + n2
    #sum = n1 + n2
    #return sum
'''
'''
def sub(n1, n2):
    return n1 - n2
'''
'''
def div(n1, n2):
    return n1//n2
'''
'''
def mult(n1, n2):
    pass
'''

# Driver
'''
num1 = int(input('Enter 1st no '))
num2 = int(input('Enter 2nd no '))
res = add(num1,num2)
#res4 = add(num2, num1)
#res5 = add(n2 = num2, n1 = num2)
print('Sum of',num1,'and',num2,'=',res)
'''
'''
res2 = sub(num1, num2)
print('Sub', res2) '''
'''
res3 = (num1, num2)
print('Div', res3)
'''

'''
# ARBITARY
def add(nums):
    sum = 0
    for n in nums:
        sum += n
    return sum


numbers = list()
count = int(input('How many ? '))
for _ in range(1, count+1):
    numbers.append(int(input('No: ')))
#print(numbers)
print(add(numbers))

#print(add(*nums: 5,6,9))
'''
'''
# Optional

def add(n1, n2, n3=10):
    return n1+n2+n3

num1 = int(input('Enter 1st num '))
num2 = int(input('Enter 2nd num'))

#res = add(num1, num2)
res =add(num1, num2, 100)

print(res)
'''

# Lambda
'''
num1 = int(input('Enter 1st num '))
num2 = int(input('Enter 2nd num'))

add = lambda n1, n2 : n1+n2

print(add(num1, num2))
'''
'''
numbers = [1,2,3,4,5]
sq = lambda nums : [num * num for num in nums]
print(sq(numbers))
'''

numbers = [1,2,3,4,5,6,7,8,9,10]
sq = lambda nums : [num * num for num in nums if num%2==0]
print(sq(numbers))







