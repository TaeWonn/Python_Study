# 매개변수 있는 함수
def add(a,b):
    return a + b

a = 3
b = 4
c = add(a,b)
print(c)

# 매개변수 없는 함수
def say():
    return 'hi'

a = say()
print(a)

# 리턴값이 없는 함수
def add(a, b):
    print("%d, %d의 합은 %d 입니다." % (a, b, a+b))


add(3,4)

# 매개변수 지정 호출
add(a =3, b = 7)

# 입력값이 몇개인지 모를 때
def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result

a = add_many(1,2,3,4,5,6,7,8,9)
print(a)

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result

a = add_mul("add", 1,2,3,4,5)
b = add_mul("mul", 1,2,3,4,5)
print(a)
print(b)

# 함수의 결괏값은 언제나 하나이다
def add_and_mul(a,b):
    return a+b, a*b

result = add_and_mul(3,4)
print(result)

result1, result2 = add_and_mul(3,4)
print ("%d, %d" % (result1, result2))


# 매개변수에 초깃값 미리 설정하기
def say_myself(name, old, man=True):
    print("my name is %s" % name)
    print("age %d" % old)
    if man:
        print("man")
    else:
        print("womman")

say_myself("hong", 2)
say_myself("hong", 2, False)

# 함수 안에서 선언한 변수의 효력 범위
a = 1
def vartest(a):
    a += 1

vartest(a)
print(a)


# 함수 안에서 함수 밖의 변수를 변경하는 방법
a = 1
def vartest2(a):
    a = a + 1
    return a

a = vartest2(a)
print(a)

## global 사용하기
a = 1
def vartest3():
    global a
    a += 1

vartest3()
print(a)

# lambda
add = lambda a, b: a+b
result = add(3,4)
print(result)