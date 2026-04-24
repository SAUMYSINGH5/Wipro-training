Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s1='hello'
type(s1)
<class 'str'>
id(s1)
2370624239296
s2='hi'
id(s2)
140704745207224
s3=s1
id(s3)
2370624239296
s1
'hello'
s1='hi'
id(s1)
140704745207224
s3
'hello'
s1='india'
id(s1)
2370627245552

list1=[10,20,30,40]
list1
[10, 20, 30, 40]
type(list1)
<class 'list'>
list[0]
list[0]
list[3]
list[3]
list[-1]
list[-1]
list1[-1]
40
list1[3]
40
list1[:3]
[10, 20, 30]
list[::2]
list[slice(None, None, 2)]
list1[::2]
[10, 30]
list2=list('hi','hello')
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    list2=list('hi','hello')
TypeError: list expected at most 1 argument, got 2
s1
'india'
list2=list(s1)
list2
['i', 'n', 'd', 'i', 'a']
list3=list1
list3
[10, 20, 30, 40]
id
<built-in function id>
id(list1)
2370627077312
id(list3)
2370627077312
list4=[100,'hi',100,True,69.36]
list4
[100, 'hi', 100, True, 69.36]
list4[2] = 23
list4
[100, 'hi', 23, True, 69.36]
list4[5]='hey'
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    list4[5]='hey'
IndexError: list assignment index out of range
list1.append('hey')
list1
[10, 20, 30, 40, 'hey']
list1.remove('hey')
list1
[10, 20, 30, 40]
list4.append(20000)
list4
[100, 'hi', 23, True, 69.36, 20000]
list4.remove(5)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    list4.remove(5)
ValueError: list.remove(x): x not in list
list4.count(23)
1
list1.insert(2, 200)
list1
[10, 20, 200, 30, 40]
id(list1)
2370627077312
list1.pop()
40
list1
[10, 20, 200, 30]
list1.pop(2)
200
list1
[10, 20, 30]
list2
['i', 'n', 'd', 'i', 'a']
list2.clear()
list2
[]
del(list2)
list2
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    list2
NameError: name 'list2' is not defined. Did you mean: 'list1'?
list2=list1
list1
[10, 20, 30]
list2
[10, 20, 30]
id(list1)
2370627077312
id(list2)
2370627077312
list1[1]=200
list1
[10, 200, 30]
list2
[10, 200, 30]
list2=list(list1)
list1
[10, 200, 30]
list2
[10, 200, 30]
list1(id)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    list1(id)
TypeError: 'list' object is not callable
id(list1)
2370627077312
id(list2)
2370625303616
list1[1] = 20
list1
[10, 20, 30]
list2
[10, 200, 30]
tuple1=(11,22,33,44,55)
tuple1
(11, 22, 33, 44, 55)
tuple1[3]
44
tuple1[30]
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    tuple1[30]
IndexError: tuple index out of range
tuple1[3]=55
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    tuple1[3]=55
TypeError: 'tuple' object does not support item assignment
tuple1[:]
(11, 22, 33, 44, 55)
tuple1[:4:2]
(11, 33)
tuple1.index(44)
3
tuple1.count()
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    tuple1.count()
TypeError: tuple.count() takes exactly one argument (0 given)
tuple1.count(22)
1
tuple2=tuple1
tuple2
(11, 22, 33, 44, 55)
tuple3=tuple(list1)
tuple3
(10, 20, 30)
list1
[10, 20, 30]
list1.append(tuple2)
list1
[10, 20, 30, (11, 22, 33, 44, 55)]
list1[0]
10
list1[2]
30
list1[3]
(11, 22, 33, 44, 55)
tuple4=tuple(list1)
tuple4
(10, 20, 30, (11, 22, 33, 44, 55))
list1[3:1]
[]
list1[3][2]
33
set1={10,20,30,40,50)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
set1={10,20,30,40,50}
set1
{50, 20, 40, 10, 30}
set1[2]
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    set1[2]
TypeError: 'set' object is not subscriptable
set1.add(25)
set1
{50, 20, 40, 25, 10, 30}
set1.add('25')
set1
{50, 20, '25', 40, 25, 10, 30}
set1.add(25)
set1
{50, 20, '25', 40, 25, 10, 30}
set2=set(set1)
set2
{50, 20, '25', 40, 25, 10, 30}
id(set1)
2370626906240
id(set2)
2370626904896
set2.remove('25')
set2
{50, 20, 40, 25, 10, 30}
set1
{50, 20, '25', 40, 25, 10, 30}
set1.union(set2)
{'25', 40, 10, 50, 20, 25, 30}
set1.intersection(set2)
{40, 10, 50, 20, 25, 30}
set3=set(list1)
set3
{10, (11, 22, 33, 44, 55), 20, 30}
set3.add(tuple1)
set3
{10, (11, 22, 33, 44, 55), 20, 30}
set3.add(list3)
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    set3.add(list3)
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
list6 =[1,2,3,6, 86]
list6
[1, 2, 3, 6, 86]
tuple8= tuple(list6)
tuple8
(1, 2, 3, 6, 86)
>>> dict1={1:10, 2:20, 3:30}
>>> dict1
{1: 10, 2: 20, 3: 30}
>>> dict1[2]
20
>>> dict2={'a':10, 'b':20, 'c':30}
>>> dict2['c']
30
>>> stud={'rno':101, 'name':'AAA', 'city':'BBB'}
>>> stud['name']
'AAA'
>>> stud['name']='XXX'
>>> stud
{'rno': 101, 'name': 'XXX', 'city': 'BBB'}
>>> stud['fname']='yyy'
>>> stud
{'rno': 101, 'name': 'XXX', 'city': 'BBB', 'fname': 'yyy'}
>>> stud.get('name')
'XXX'
>>> stud.keys()
dict_keys(['rno', 'name', 'city', 'fname'])
>>> stud.values()
dict_values([101, 'XXX', 'BBB', 'yyy'])
>>> stud.pop(fname)
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    stud.pop(fname)
NameError: name 'fname' is not defined
>>> stud.pop('fname')
'yyy'
>>> stud
{'rno': 101, 'name': 'XXX', 'city': 'BBB'}
