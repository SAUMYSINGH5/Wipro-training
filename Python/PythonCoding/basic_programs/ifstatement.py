"""
Date: 22-4-2026
Desc: Learning Various If Statement Formats

"""

# Biggest of 2 nos
'''
num1 = int(input("Enter 1st number "))
num2 = int(input("Enter 2nd number "))

if num1 > num2:
    print(num1, 'is bigger')
if num1 == num2 :
    print("Both are Equal")
else:
    print(num2, 'is bigger')
'''


# Biggest of 3 Number
'''
num1 = int(input("Enter 1st number "))
num2 = int(input("Enter 2nd number "))
num3 = int(input("Enter 3rd number "))

if num1 == num2 and num2 == num3:
    print("All numbers are Equal")
if num1 == num2 or num2 == num3 or num1 == num3:
    print("2 numbers are Equal")
elif num1 > num2 and num1 > num3:
    print(num1, "num1 is Biggest")
elif num2 > num1 and num2 > num3:
    print(num2, "num2 is Biggest")
elif num3 > num2 and num3 > num1:
    print(num3, "num3 is Biggest")
'''

# WeekDay
'''
ch = int(input("Enter a number between 1 to 7 "))

match(ch):
    case 1:
        print('Mon')
    case 2:
        print('Tue')
    case 3:
        print('Wed')
    case 4:
        print('Thu')
    case 5:
        print('Fri')
    case 6:
        print('Sat')
    case 7:
        print('Sun')
    case _:
        print('Invalid Input')
'''













































































































