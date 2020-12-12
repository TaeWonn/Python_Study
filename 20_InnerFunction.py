# all
"""
반복가능한 자료형 x를 인수로 받으면
이 x의 요소가 모두 참이면 True,
하나라도 거짓이면 False를 반환한다.
"""
print(all([1,2,3]))
print(all([1,2,3,0]))
print(all([]))


# any
"""
any는 반복가능한 자료형 x를 입력인수로 받으며
이 x의 요소 중 하나라도 참이면 True
모두 거짓일때 에만 False를 반환한다.
"""
print(any([1,2,3,0]))
print(any([0,""]))
print(any([]))

# chr
"""
아스키 코드 값을 입력받아 문자로 출력하는 함수
"""
print(chr(97))
print(chr(48))

# dir
"""
객체가 자체적으로 가지고 있는 변수나 함수를 보여준다.
"""
print(dir([1,2,3]))
print(dir({'1':'a'}))

# divmod
"""
2개의 숫자를 인자로 받는다
그리고 a를 b로 나누몫과 나머지를 튜플 형태로 반환한다.
"""
print(divmod(7,3) )

# enumerate
"""
이 함수는 자료형을 입력으로 받아 인덱스 값을 포하하는
enumerate 객체를 돌려준다.
"""
for i, name in enumerate(['body','foo','bar']):
    print(i,name)

# evel
"""
eval(expression )은 실행 가능한 문자열(1+2, 'hi' + 'a' 같은 것)
을 입력으로 받아 문자열을 실행한 결괏값을 돌려주는 함수이다.
"""
eval('1+2')
eval("'hi'+'a'")

# filter
def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result

print(positive([1,-3,2,0,-5,6]))

def positive2(x):
    return x > 0

print(list(filter(positive2, [1,-3,2,0,-5,6])))

# hex
"""
정수 값을 입력받아 16진수로 변환한다
"""

# id
"""
객체를 입력받아 객체의 고유 주소 값을 돌려받는 함수다
"""

# int
"""
문자열 형태의 숫자나 소수점이 있는 숫자 등을 
정수형태로 돌려주는 함수이다
"""

# isinstance
"""
첫 번째 인수로 인스턴스, 두번 째 인수로 클래스 이름을 받는다.
입력으로 받은 인스턴스가 그 클래스의 인스턴스인지 판단하여
True, False로 반환
"""
class Person: pass
a = Person()
isinstance(a,Person)

# list
"""
반복 가능한 자료형 s를 입력받아 리스트로 만들어 돌려주는 함수이다.
"""

# map
"""
map(f, iterable)은 함수(f)와 반복 가능한(iterable) 
자료형을 입력으로 받는다. 
map은 입력받은 자료형의 각 요소를 함수 f가 
수행한 결과를 묶어서 돌려주는 함수이다.
"""
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1,2,3,4])
print(result)

def two_times2(x):
    return x*2

list(map(two_times2, [1,2,3,4]))

# ord
"""
문자의 아스키 코드값을 돌려주는 함수이다
"""
ord('a') # 97

# pow
"""
x의 y 제곱한 결괏값을 돌려주는 함수이다.
"""
pow(2,4) # 16

# zip
"""
zip(*iterable)은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수이다.
"""
list(zip([1,2,3],[4,5,6]))
#[(1,4), (2,5), (3,6)]