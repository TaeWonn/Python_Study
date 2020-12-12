"""
변수란?
파이썬에서 사용하는 변수는 객체를 가리키는 것이라고도 말할 수 있다. 
객체란 우리가 지금껏 보아 온 자료형과 같은 것을 의미하는 말이다.
"""
a = [1, 2, 3]
print( id(a))

b = a

print(a is b) # a와 b가 가리키는 객체가 동일한가?

# [:] 이용
a = [1, 2, 3]
b = a[:]
a[1] = 4

print(a)
print(b)

# copy 모듈 이용
from copy import copy

b = copy(a)
print ( b is a)

# 변수를 만드는 여러 가지 방법
a, b = ('python', 'life')
(a, b) = 'python', 'life'
[a, b] = ['python', 'life']

a = b = 'python'

print(a, b)
