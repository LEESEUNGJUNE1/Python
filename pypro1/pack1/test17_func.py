# 함수 장식자 (function decorator) : meta 기능이 있음
# 장식자는 또 다른 함수를 감싼 함수다.

def make2(fn):
    return lambda:'안녕 ' + fn()

def make1(fn):
    return lambda:'반가워 ' + fn()

def hello():
    return '홍길동'

hi = make2(make1(hello))    #주소 개념으로 이해하자!
print(hi())

print()

@make2              #장식자라 부른다.
@make1
def hello2():
    return '고길동'
print(hello2())

print()
hi2 = hello2()
print(hi2)

hi3 = hello2    #주소를 치환
print(hi3())

import time
print(time.localtime())