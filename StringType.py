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
