import re

'''
# beg and end 
txt = input('Enter a text ')
bpat = input('Enter beginning pattern ')
epat = input('Enter ending pattern ')
bpat = '^' + bpat  #^India
epat = epat + '$'  #try$

if re.search(pattern=bpat, string=txt):
    print('Beginning Pattern not Available')
else:
    print('Beginning Pattern Available')
'''

'''
#Digit Matching
mbno = input('Enter a Text ')
#pat = '[0-9]'
pat = r"\d"

if re.search(pattern = pat, string=mbno):
    print('Only digits')
else:
    print('Other chars Available')
'''



'''
mbno = input('Enter a Text ')
pat = r"[0-9]"

if re.fullmatch(pattern = pat, string=mbno):
    print('Only digits')
else:
    print('Other chars Available')
'''
'''
# Username
un = input('Enter UN ')
pat = r"^[a-z_]{8,}$"

if re.match(pattern=pat, string=un):
    print('Valid')
else:
    print('Invalid')
'''

#Email
'''
email = input('Email ')
pat = r"^[a-zA-Z0-9_]+@[a-z]+\.[a-z]+$"

if re.match(pattern=pat, string=email):
    print('Valid')
else:
    print('Invalid')
'''

#Password
'''
pwdtxt = input('pwd : ')
pat = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@_-]).{8,}$"

if re.match(pattern=pat, string=pwdtxt):
    print('Valid')
else:
    print('Invalid')
'''

'''
txt = input('Text ')
pat = r"\s+"

#print(re.sub(pattern=pat, string=txt,repl=' '))
print(re.split(pattern=pat, string=txt))
'''

























































































