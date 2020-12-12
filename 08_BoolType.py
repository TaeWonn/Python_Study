a = True
b = False

print(type(a))

print(1 == 1 )

"""
값	        참 or 거짓
"python"	참
""	        거짓
[1, 2, 3]	참
[]	        거짓
()	        거짓
{}	        거짓
1	        참
0	        거짓
None	    거짓
"""

a = [1,2,3,4]
while a:
    print(a.pop())

if [1,2,3]:
    print("참")
else:
    print("거짓")


# 불 연산
print( bool('python'))
print( bool(''))
print( bool(0))