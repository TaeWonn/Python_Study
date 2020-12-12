# 모듈 불러오기
import mod1

print(mod1.add(3,4))

from mod1 import add, sub
add(3,4)

# if_name__ == "__main__": 의 의미
"""
if __name__ == "__main__"을 사용하면 
C:\doit>python mod1.py처럼 
직접 이 파일을 실행했을 때는 
__name__ == "__main__"이 참이 되어 
if문 다음 문장이 수행된다. 
반대로 대화형 인터프리터나 다른 파일에서 
이 모듈을 불러서 사용할 때는 
__name__ == "__main__"이 거짓이 되어 
if문 다음 문장이 수행되지 않는다.
"""

import mod2
print(mod2.PI)
print(mod2.add(mod2.PI, 4.4))
