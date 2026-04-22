Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s1 ='Hello'
s1
'Hello'
type(s1)
<class 'str'>
s1.capitalize()
'Hello'
s1.upper()
'HELLO'
s1.lower()
'hello'
s1='hE
SyntaxError: unterminated string literal (detected at line 1)
s1='hEllO'
s1.casefold()
'hello'
s1='HeLLo'
s1.casefold()
'hello'
s1.count('L')
2
s1.count('l')
0
s1.count('H')
1
s1.endswith('O')
False
s1.endswith('o')
True
s1.find('L')
2
s1.find('e')
1
s1.find('o')
4
s1.find('0')
-1
s1.index('o')
4
s1.index('m')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    s1.index('m')
ValueError: substring not found
s1.isalpha()
True
s1.isdigit()
False
s1.join(' there')
' HeLLotHeLLohHeLLoeHeLLorHeLLoe'
s1.replace('L','l')
'Hello'
s1
'HeLLo'
s1='hello there how are you'
s1
'hello there how are you'
s1.split(' ')
['hello', 'there', 'how', 'are', 'you']
s1='Hellow there - how are you'
s1.split('-')
['Hellow there ', ' how are you']
s1.zwapcase()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    s1.zwapcase()
AttributeError: 'str' object has no attribute 'zwapcase'. Did you mean: 'swapcase'?
s1.swapcase()
'hELLOW THERE - HOW ARE YOU'
s1='hello there !!!'
len(s1)
15
s1[1]
'e'
s1[10]
'e'
s1[14]
'!'
s1[-3]
'!'
s1[-4]
' '
s1[-15]
'h'
s1[-16]
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    s1[-16]
IndexError: string index out of range
s1[16]
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    s1[16]
IndexError: string index out of range
s1[0:5]
'hello'
s1[0:10]
'hello ther'
s1[0:]
'hello there !!!'
s1[:]
'hello there !!!'
s1[2:12:2]
'lotee'
s1[::2]
'hlotee!!'
s1[::3]
'hltr!'
s1[-15:-10]
'hello'
s1[-10:-15]
''
s1[-15::-2]
'h'
s1[-15:-2]
'hello there !'
s1[-10::-2]
' le'
s1[-10::-2]
' le'
s1[::-2]
'!!eetolh'
s1[::2]
'hlotee!!'
s1[-15::-2]
'h'

===================================================== RESTART: C:/Wipro Training/Python/str1ex.py =====================================================
h
e
l
l
o
 
t
h
e
r
e
 
!
!
!
>>> 
===================================================== RESTART: C:/Wipro Training/Python/str1ex.py =====================================================
h
e
l
l
o
>>> 
===================================================== RESTART: C:/Wipro Training/Python/str1ex.py =====================================================
h
e
l
l
o
 
t
