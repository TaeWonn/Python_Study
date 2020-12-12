def solution(s, n):
    if n > 25:
        n = n % 26
        print(n)
        
    answer = move(list(s), n)

    return answer

def move(s, n):
    result = ''
    for i in s:
        if i == ' ' : 
            result += ' '
            continue
        elif (90 < ord(i)+n and ord(i)+n <97) or 122 < ord(i)+n:
            result += chr(ord(i) + n - 26)
        else:
            result += chr(ord(i) + n)
    return result




print(solution('AB',1))
print(solution('z',1))
print(solution('a B z',4))
print(solution('a B z',30))