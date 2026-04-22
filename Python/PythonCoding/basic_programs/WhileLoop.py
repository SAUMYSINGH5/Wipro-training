

#      Naural Number Printing
'''
num = int(input("Enter a Number "))

value = 1
while value <= num:
    print(value)
    value += 1
'''

# Armstrong Number

num = input('Enter a Number ') #Taking input as string

count = len(num) #Return Length
ni = int(num)    #Typecast string into int
sum = 0
comp = ni
while ni > 0:
    rem = ni % 10
    sum = sum + rem ** count
    ni = ni // 10

if comp == sum:
    print('Armstrong Number')
else:
    print('Not a Armstrong Number ')


