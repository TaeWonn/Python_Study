"""
딕셔너리란?
사람은 누구든지 "이름" = "홍길동", "생일" = "몇 월 며칠" 등으로 구별할 수 있다. 
파이썬은 영리하게도 이러한 대응 관계를 나타낼 수 있는 자료형을 가지고 있다. 
요즘 사용하는 대부분의 언어도 이러한 대응 관계를 나타내는 자료형을 갖고 있는데, 
이를 연관 배열(Associative array) 또는 해시(Hash)라고 한다.

파이썬에서는 이러한 자료형을 딕셔너리(Dictionary)라고 하는데, 
단어 그대로 해석하면 사전이라는 뜻이다. 
즉 "people"이라는 단어에 "사람", "baseball"이라는 단어에 "야구"라는 뜻이 부합되듯이 
딕셔너리는 Key와 Value를 한 쌍으로 갖는 자료형이다. 
예컨대 Key가 "baseball"이라면 Value는 "야구"가 될 것이다.

딕셔너리는 리스트나 튜플처럼 순차적으로(sequential) 해당 요솟값을 구하지 않고 
Key를 통해 Value를 얻는다. 이것이 바로 딕셔너리의 가장 큰 특징이다. 
baseball이라는 단어의 뜻을 찾기 위해 사전의 내용을 순차적으로 
모두 검색하는 것이 아니라 baseball이라는 단어가 있는 곳만 펼쳐 보는 것이다.
"""

dic = {'name':'pey', 'phone':'01012341234', 'birth': '1118'}

#딕셔너리 쌍 추가
a = {1: 'a'}
a[2] = 'b'
print(a)

#딕셔너리 제거
del a[1]
print(a)

grade = {'pey': 10, "julliet":99}
print(grade['pey'])

# 딕셔너리 관련 함수
a = {'name':'pey', 'phone': '01012341234', 'birth':'1118'}
print(list(a.keys()))

# key List
for k in a.keys():
    print(k)

print("-" * 40)

# value List
print(a.values())

# key, value 쌍 얻기
print(a.items())

# clear
a.clear()
print(a)

a = {'name':'pey', 'phone': '01012341234', 'birth':'1118'}
print(a.get('name'))

## default 값 가져오기
print(a.get('foo','bar') )

## key가 있는지 조사
print('name' in a)
print('email' in a)