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
"""
