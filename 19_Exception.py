try:
    f = open("없는파일", "r")
except:
    print("없는파일")

try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

try:
    4/0
except ZeroDivisionError:
    print("error")
finally:
    print("end")

# 오류 회피하기
try:
    f = open("없는파일","r")
except FileNotFoundError:
    pass

# 오류 일부러 발생시키기
class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    pass

eagle = Eagle()
eagle.fly()

class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)


