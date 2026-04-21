Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = 5
b = str(a)
b
'5'
c = float(b)
c
5.0
d=str(c)
d
'5.0'
b
'5'
e = int(b)
e
5
x = 'hi'
y=int(x)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    y=int(x)
ValueError: invalid literal for int() with base 10: 'hi'
x='i'
y=int(x)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    y=int(x)
ValueError: invalid literal for int() with base 10: 'i'
y=bool(x)
y
True









x =i
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    x =i
NameError: name 'i' is not defined. Did you mean: 'id'?
x='i'
y=ord(x)
y
105
                                                        y
                                                        
SyntaxError: unexpected indent

y
105
x=''
y=bool(x)
y
False
>>> yprint('ans:', 6+3)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    yprint('ans:', 6+3)
NameError: name 'yprint' is not defined. Did you mean: 'print'?
>>> print('ans:',6+3)
ans: 9
>>> print("  )
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print('my brother's house)
...       
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("my brother's house")
...       
my brother's house
>>> input()
...       
697448
'697448'
>>> p=input()
...       
p
>>> p=input('type some thing : ')
...       
type some thing : p
>>> p=int(input('type some thing: '))
...       
type some thing: p
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    p=int(input('type some thing: '))
ValueError: invalid literal for int() with base 10: 'p'
>>> p=int(input('type some thing: '))
...       
type some thing: 414
p
      
414
