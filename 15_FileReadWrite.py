f = open("new.txt","w")
f.close()

"""
파일열기모드     설명

r               읽기모드 - 파일을 읽기만 할 때 사용
w               쓰기모드 - 파일에 내용을 쓸 때 사용
a               추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용

파일을 쓰기 모드로 열면 해당 파일이 이미 존재할 경우 원래 있던
 내용이 모두 사라지고, 
 해당 파일이 존재하지 않으면 새로운 파일이 생성된다. 
 위 예에서는 디렉터리에 파일이 없는 상태에서 새파일.txt를 
 쓰기 모드인 'w'로 열었기 때문에 새파일.txt라는 
 이름의 새로운 파일이 현재 디렉터리에 생성되는 것이다.
"""

f = open("new.txt","w")
for i in range(1,11):
    data = "%d 번째 줄입니다.\n" % i
    f.write(data)
f.close()

# 프로그램의 외부에 저장된 파일을 읽는 여러가지 방법
## readline() 함수

f = open("new.txt", 'r')
# line = f.readline()
# print(line)

while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

## readlines()
f = open("new.txt", "r")
lines = f.readlines()
for line in lines:
    print(line)
f.close()

# read()
f = open("new.txt","r")
data = f.read()
print(data)
f.close()

# 파일에 새로운 내용 추가하기
f = open("new.txt", "a")
for i in range(11,20):
    data = "%d 번째 줄입니다.\n"%i
    f.write(data)
f.close()

# with문과 함께 사용
with open("foo.txt", "w") as f:
    f.write("Life is too short")

import sys
args = sys.argv[1:]
for i in args:
    print(i)