# 패키지(Packages)는 도트(.)를 사용하여 
# 파이썬 모듈을 계층적(디렉터리 구조)으로 관리할 수 있게 해준다. 
# 예를 들어 모듈 이름이 A.B인 경우에 A는 패키지 이름이 되고 B는 A 패키지의 B모듈이 된다.v

# 패키지 만들기
""" 
/game/__init__.py
/game/sound/__init__.py
/game/sound/echo.py
/game/graphic/__init__.py
/game/graphic/render.py
"""

# 패키지 안의 함수 실행하기
"""
자, 이제 패키지를 사용하여 echo.py 파일의 
echo_test 함수를 실행해 보자. 
패키지 안의 함수를 실행하는 방법은 다음 3가지가 있다. 
다음 예제는 import 예제이므로 하나의 예제를 실행하고 
나서 다음 예제를 실행할 때에는 반드시 인터프리터를 종료하고 
다시 실행해야 한다. 
인터프리터를 다시 시작하지 않을 경우 이전에 import한 
것들이 메모리에 남아 있어 엉뚱한 결과가 나올 수 있다
(윈도우의 경우 인터프리터 종료는 Ctrl+Z).
"""

# __init__.py 의 용도
"""
__init__.py 파일은 해당 디렉터리가 패키지의 일부임을 
알려주는 역할을 한다. 만약 game, sound, graphic 등 
패키지에 포함된 디렉터리에 __init__.py 파일이 없다면 
패키지로 인식되지 않는다.
"""

# relative 패키지
"""
만약 graphic 디렉터리의 render.py 모듈이 
sound 디렉터리의 echo.py 모듈을 사용하고 
싶다면 어떻게 해야 할까? 
다음과 같이 render.py를 수정하면 가능하다.
"""