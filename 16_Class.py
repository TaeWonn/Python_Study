result = 0

def add(num):
    global result
    result += num
    return result

print(add(3))
print(add(4))

class Calc:
    def __init__(self):
        self.result = 0
    
    def add(self, num):
        self.result += num
        return self.result

cal1 = Calc()
cal2 = Calc()

print(cal1.add(3))
print(cal2.add(4))


class Cookie:
    pass

"""
[객체와 인스턴스의 차이]

클래스로 만든 객체를 인스턴스라고도 한다.
 그렇다면 객체와 인스턴스의 차이는 무엇일까?
 이렇게 생각해 보자. a = Cookie() 이렇게 만든 a는 객체이다.
 그리고 a 객체는 Cookie의 인스턴스이다.
 즉 인스턴스라는 말은 특정 객체(a)가 어떤 클래스(Cookie)의 
 객체인지를 관계 위주로 설명할 때 사용한다. 
 "a는 인스턴스"보다는 "a는 객체"라는 표현이 어울리며 
 "a는 Cookie의 객체"보다는 "a는 Cookie의 인스턴스"라는 
 표현이 훨씬 잘 어울린다.
"""

class FourCal:
    def __init__(self):
        pass
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        return self.first + self.second
    def mul(self):
        return self.first * self.second
    def sub(self):
        return self.first - self.second
    def div(self):
        return self.first / self.second

a = FourCal(4,2)
a.setdata(4,2)
print(a)

FourCal.setdata(a, 4, 2)

# a = FourCal()
# b = FourCal()

a.setdata(4,3)
print(a.first)

print(a.add())

# 클래스의 상속
class MoreFourCal(FourCal):
    def pow(self):
        return self.first ** self.second

a = MoreFourCal(4,2)

print(a.add())
print(a.div())
print(a.pow())

# 메소드 오버라이딩
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4,0)
a.div()

# 클래스 변수
class Family:
    lastName = "kim"

print(Family.lastName)

a = Family()
b = Family()
Family.lastName ="park"
print(a.lastName)
print(b.lastName)

print(id(a.lastName))
print(id(b.lastName))