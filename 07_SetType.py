s1 = set([1,2,3])
print(s1)

s2 = set("Hello")
print(s2)

"""
집합 자료형의 특징
자, 그런데 위에서 살펴본 set("Hello")의 결과가 좀 이상하지 않은가? 
분명 "Hello" 문자열로 set 자료형을 만들었는데 생성된 
자료형에는 l 문자가 하나 빠져 있고 순서도 뒤죽박죽이다. 
그 이유는 set에 다음과 같은 2가지 큰 특징이 있기 때문이다.

중복을 허용하지 않는다.
순서가 없다(Unordered).
리스트나 튜플은 순서가 있기(ordered) 때문에 인덱싱을 통해 
자료형의 값을 얻을 수 있지만 set 자료형은 순서가 없기(unordered) 때문에 
인덱싱으로 값을 얻을 수 없다. 
이는 마치 02-5에서 살펴본 딕셔너리와 비슷하다. 
딕셔너리 역시 순서가 없는 자료형이라 인덱싱을 지원하지 않는다.
"""

s1 = set([1,2,3])
l1 = list(s1)
print(l1)
print(l1[0])

t1 = tuple(s1)
print(t1)


# 교집합
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s1 & s2)
print(s1.intersection(s2))

# 합집합
print(s1 | s2)
print(s1.union(s2))

# 차집합
print(s1 - s2)
print(s1.difference(s2))


# 집합 자료형 관련 함수

## 값 1개 추가
s1 = set([1,2,3])
s1.add(4)
print(s1)

## 값 여러 개 추가
s1.update([4,5,6])
print(s1)

## 특정 값 제거
s1.remove(2)
print(s1)