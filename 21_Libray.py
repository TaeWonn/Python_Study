"""
sys.path는 파이썬 모듈들이 저장되어 있는 위치를 나타낸다. 
즉 이 위치에 있는 파이썬 모듈은 경로에 상관없이 
어디에서나 불러올 수 있다.
"""
import sys
print(sys.path)

## 강제 종료
## sys.exit()

# pickle
"""
pickle은 객체의 형태를 그대로 유지하면서 파일에
저장하고 불러올 수 있게 하는 모듈이다.
다음 예는 pickle 모듈의 dump 함수를 사용하여
딕셔너리 객체인 data를 그대로 파일에 젖아하는 방법을 보여준다.
"""
import pickle
f = open("test.txt", "wb")
data = {1: 'python', 2:'you need'}
pickle.dump(data,f)
f.close()

f = open("test.txt", 'rb')
data = pickle.load(f)
print(data)
f.close()

# os
"""
OS 모듈은 환경 변수나 디렉터리, 파일 등의 
OS 자원을 제어할 수 있게 해주는 모듈이다.

내 시스템의 환경 변수 값을 알고 싶을 때 - os.environ

os.mkdir 디렉토리생성
os.rmdir 디렉토리 삭제, 단 비어있어야 삭제 가능
os.unlink 파일을 지운다.
os.renmae(src, dst) src라는 이름의 파일을 dst라는 이름으로 바꾼다.
"""

# shutil
"""
파일을 복사해주는 파이썬 모듈이다.
"""
import shutil
shutil.cop("src.txt","dst.txt")

# glob
"""
디렉토리에 있는 파일을 리스트로 반환
"""
import glob
glob.glob("c:/dit/mark**")

# tempfile
"""
파일을 임시로 만들어서 사용할 때 유용한 모듈이다.
tempfile.mkstemp()는 중복되지 않는 
임시 파일의 이름을 무작위로 만들어서 돌려준다.
"""
import tempfile
f = tempfile.TemporaryFile()
f.close()

# time
"""
시간과 관련된 time 모듈에는 함수가 굉장히 많다. 
그중 가장 유용한 몇 가지만 알아보자.

time.time
현재 시간을 실수 형태로 돌려주는 함수이다.

time.localtime
time()이 돌려준 실수 값을 사용해서 
연도, 월, 일, 시, 분 ,초 형태로 바꾸어 주는 함수이다.

time.asctime
위 localtime에 의해서 반환된 튜플 형태의 값을
인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로
돌려주는 함수이다.

time.ctime
위 함수를 보다 간편하게 표시할 수 있다.
asctime과 다른 점은 ctime은 항상 현재 시간만 돌려준다는 점이다.

time.strftime
포맷형태로 출력한다.

포맷코드	설명	예
%a	요일 줄임말	Mon
%A	요일	Monday
%b	달 줄임말	Jan
%B	달	January
%c	날짜와 시간을 출력함	06/01/01 17:22:21
%d	날(day)	[01,31]
%H	시간(hour)-24시간 출력 형태	[00,23]
%I	시간(hour)-12시간 출력 형태	[01,12]
%j	1년 중 누적 날짜	[001,366]
%m	달	[01,12]
%M	분	[01,59]
%p	AM or PM	AM
%S	초	[00,59]
%U	1년 중 누적 주-일요일을 시작으로	[00,53]
%w	숫자로 된 요일	[0(일요일),6]
%W	1년 중 누적 주-월요일을 시작으로	[00,53]
%x	현재 설정된 로케일에 기반한 날짜 출력	06/01/01
%X	현재 설정된 로케일에 기반한 시간 출력	17:22:21
%Y	년도 출력	2001
%Z	시간대 출력	대한민국 표준시
%%	문자	%
%y	세기부분을 제외한 년도 출력	01
"""
import time
time.time()

time.localtime(time.time())

time.asctime(time.localtime(time.time()))

time.ctime()

time.strftime("yyyyMMdd", time.localtime(time.time()))

# calendar
import calendar
"""
calendar.calendar(연도)로 사용하면 그해의 전체 달력을 볼 수 있다.
결괏값은 달력이 너무 길어 생략하겠다.


"""
print(calendar.calendar(2015))

## 위와 똑같은 결괏값을 얻을 수 있다.
calendar.prcal(2015)

calendar.prmonth(2015, 12)

calendar.weekday(2015, 12, 31)

calendar.monthrange(2015, 12)

# random
import random
random.random()

random.randint(1, 10) # 1~ 10 사이의 난수 값 반환


def random_pop (data):
    number = random.randint(0, len(data) -1)
    return data.pop(number)

if __name__ == '__main__':
    data = [1,2,3,4]
    while data:
        print(random_pop(data))

import webbrowser
webbrowser.open("https://google.com")
webbrowser.open_new("https://google.com")


import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working %s\n" % i)

print("Start")

threads = []
for i range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)

for t in threads:
    t.start()

print("End")

