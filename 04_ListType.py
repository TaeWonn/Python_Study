#리스트는 어떻게 만들고 사용할까?
odd = [1, 3, 5, 7, 9]

a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]

#리스트의 인덱싱
a = [1, 2, 3]
print(a)
print(a[0])
print(a[0] + a[2]) # 배열 요소 연산
print(a[-1]) # 끝 인데스 부터 카운트


# 리스트의 슬라이싱
a = [1, 2 ,3 ,4 ,5]
print(a[0:2])


# 리스트 연산
a = [1, 2, 3]
b = [4, 5, 6]
print( a + b )
print( a * 3 )
print( len(a) )

print( str(a[2]) + "hi" )


# 리스트의 수정과 삭제
a = [1, 2, 3]
a[2] = 4
print(a)

del a[1]
print(a)

#리스트 관련 함수들
a = [1, 2, 3]
a.append(4)
print(a)

a.append([5,6])
print(a)

##정렬
a = [1, 4, 3, 2]
a.sort()
print(a)

a.reverse()
print(a)

## 삽입
a.insert(3,5)
print(a)

## 삭제
a.remove(3)
print(a)

# pop
a.pop()
print(a)
a.pop(1)
print(a)

## count
a = [1,2,3,1]
print( a.count(1) )

## 확장
a = [1,2,3]
a.extend([4,5])
print(a)