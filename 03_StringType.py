#문자열이란?
#문자열(String)이란 문자, 단어 등으로 구성된 문자들의 집합을 의미한다.

#1. 큰따옴표(")로 양쪽 둘러싸기
"Hello World"

#2. 작은따옴표(')로 양쪽 둘러싸기
'Python is fun'

#3. 큰따옴표 3개를 연속(""")으로 써서 양쪽 둘러싸기
"""Life is too short, You need python"""

#4. 작은따옴표 3개를 연속(''')으로 써서 양쪽 둘러싸기
'''Life is too short, You need python'''


# 여러 줄인 문자열을 변수에 대입하고 싶을 때
multiline = "Life is too short\nYou need python"
print(multiline)


#[이스케이프 코드란?]

#문자열 예제에서 여러 줄의 문장을 처리할 때 백슬래시 문자와 소문자 n을 조합한 \n 이스케이프 코드를 사용했다. 이스케이프 코드란 프로그래밍할 때 사용할 수 있도록 미리 정의해 둔 "문자 조합"이다. 주로 출력물을 보기 좋게 정렬하는 용도로 사용한다. 몇 가지 이스케이프 코드를 정리하면 다음과 같다.

#   코드	설명
#   \n	    문자열 안에서 줄을 바꿀 때 사용
#   \t	    문자열 사이에 탭 간격을 줄 때 사용
#   \\	    문자 \를 그대로 표현할 때 사용
#   \'	    작은따옴표(')를 그대로 표현할 때 사용
#   \"	    큰따옴표(")를 그대로 표현할 때 사용
#   \r	    캐리지 리턴(줄 바꿈 문자, 현재 커서를 가장 앞으로 이동)
#   \f	    폼 피드(줄 바꿈 문자, 현재 커서를 다음 줄로 이동)
#   \a	    벨 소리(출력할 때 PC 스피커에서 '삑' 소리가 난다)
#   \b	    백 스페이스
#   \000	널 문자


#문자열 연산하기
head = "Python"
tail = " is fun!"
print(head + tail)

# 문자열 곱하기
a = "python"
a = a * 2
print(a)

# 문자열 길이 구하기
a = "Life is too short"
b = len(a)
print(b)

# 문자열 인덱싱과 슬라이싱
a = "Life is too short, You need Python"
print(a[3]) # 파이썬은 0부터 숫자를 센다.
print(a[-1]) # 끝자리 부터 인덱싱

# 문자열 슬라이싱
a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
print(b)
print(a[0:3])
print(a[:15])
print(a[19:-7])

# 슬라이싱으로 문자열 나누기
a = "20010331Rainy"
date = a[:8]
weather = a[8:]
print(date)
print(weather)

a = "20010331Rainy"
year = a[:4]
day = a[4:8]
weather = a[8:]
print(year)
print(day)
print(weather)

# 문자열 포매팅
a = "I eat %d apples." % 3
print(a)

a = "I eat %s apples." % "five"
print(a)

number = 3
a = "I eat %d apples." % number
print(a)

number = 10
day = "three"
a = "I ate %d apples. so I was sick for %s days." % (number, day)
print(a)


#    코드	설명
#    %s	문자열(String)
#    %c	문자 1개(character)
#    %d	정수(Integer)
#    %f	부동소수(floating-point)
#    %o	8진수
#    %x	16진수
#    %%	Literal % (문자 % 자체)


a = "I have %s apples" % 3
print(a)

a = "rate is %s" % 3.234
print(a)
## 3을 문자열 안에 삽입하려면 %d를 사용하고, 3.234를 삽입하려면 %f를 사용해야 한다. 하지만 %s를 사용하면 이런 것을 생각하지 않아도 된다. 
## 왜냐하면 %s는 자동으로 % 뒤에 있는 값을 문자열로 바꾸기 때문이다.

# f 문자열 포매팅
name = "홍길동"
age = 30
print( f"나의 이름으 {name}입니다. 나이는 {age}입니다" )

age = 30
print( f"나는 내년이면 {age+1} 살이 된다" )

d = {'name':'hong', 'age':30}
print( f'나의 이름은 {d["name"]} 입니다. 나이는 {d["age"]}입니다.' )

"""
정렬은 다음과 같이 할 수 있다.

>>> f'{"hi":<10}'  # 왼쪽 정렬
'hi        '
>>> f'{"hi":>10}'  # 오른쪽 정렬
'        hi'
>>> f'{"hi":^10}'  # 가운데 정렬
'    hi    '
공백 채우기는 다음과 같이 할 수 있다.

>>> f'{"hi":=^10}'  # 가운데 정렬하고 '=' 문자로 공백 채우기
'====hi===='
>>> f'{"hi":!<10}'  # 왼쪽 정렬하고 '!' 문자로 공백 채우기
'hi!!!!!!!!'

소수점은 다음과 같이 표현할 수 있다.

>>> y = 3.42134234
>>> f'{y:0.4f}'  # 소수점 4자리까지만 표현
'3.4213'
>>> f'{y:10.4f}'  # 소수점 4자리까지 표현하고 총 자리수를 10으로 맞춤
'    3.4213'
f 문자열에서 { } 문자를 표시하려면 다음과 같이 두 개를 동시에 사용해야 한다.

>>> f'{{ and }}'
'{ and }'
"""

# 문자열 관련 함수들

## 문자 개수 세기
a = "hobby"
print( a.count('b') )

## 위치 알려주기 (find)
a = "Pythone is the best choice"
print( a.find('b') )
print( a.find('k') )

## 위치 알려주기 (index)
a = "Life is too short"
print( a.index('t') )
#print( a.index('k') ) # index는 문자열 없을 시 error 발생

# 문자열 삽입 
a = ",".join("abcd")
print(a)

# 소문자 <-> 대문자로 바꾸기
a = "hi"
print(a.upper())
print(a.lower())


# 공백 제거
a = " hi "
print(a.lstrip()) #왼쪽 공백 지우기
print(a.rstrip()) #오른쪽 공백 지우기
a = " hi "
print(a.strip())

# 문자열 바꾸기
a = "Life is too short"
print(a.replace("Life", "Your leg"))

# 문자열 나누기
a = "List is too short"
print(a.split())
b = "a:b:c:d"
print(b.split(":"))


