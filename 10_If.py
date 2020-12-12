money = True
if money:
    print("taxi")
else:
    print("walk")

"""
들여쓰기
if문을 만들 때는 if 조건문: 
바로 아래 문장부터 if문에 속하는 모든 문장에 들여쓰기(indentation)를 해주어야 한다. 
오른쪽에서 보는 것과 같이 조건문이 참일 경우 "수행할 문장1"을 들여쓰기했고 
"수행할 문장2"와 "수행할 문장3"도 들여쓰기 해 주었다. 
다른 프로그래밍 언어를 사용해 온 사람들은 파이썬에서 
"수행할 문장"을 들여쓰기하는 것을 무시하는 경우가 많으니 더 주의해야 한다.
"""

x = 3
y = 2
print(x > y)

money = 2000
if money >= 3000:
    print("taxi")
else:
    print("walk")


money = 2000
card = True
if money >= 3000 or card:
    print("taxi")
else:
    print("walk")

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass 
else:
    print("카드를 꺼내라")

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
     print("택시를 타고가라")
elif card: 
     print("택시를 타고가라")
else:
     print("걸어가라")

score = 60
# 조건부 표현식
if score >= 60:
    message = "succes"
else:
    message = "failure"

message = "success" if score >= 60 else "failure"