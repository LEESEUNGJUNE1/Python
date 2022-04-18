# numpy

import numpy as np
from sqlalchemy.sql.expression import false

aa = np.eye(3)
print(aa)

bb = np.c_[aa, aa[2]]  # 2열(세번째 열)과 동일한 열 추가
print(bb)

cc = np.r_[aa, [aa[2]]]  # 행 추가
print(cc)

print('--- append, insert, delete')
a = [1, 2, 3]
b = np.append(a, [4, 5])        # 표적 배열, 값
print(b)

c = np.insert(a, 2, [6, 7])     # 표적 배열, index, 값
print(c)

d = np.delete(a, 1)             # 표적 배열, 삭제할 index
print(d)


print('--------------------')
aa = np.arange(1, 10).reshape(3, 3)
print(aa)
bb = np.arange(10, 19).reshape(3, 3)  # 2차원
print(bb)
print()
cc = np.append(aa, bb)        # 표적 배열, 값
print(cc)  # [10 11 12 13 14 15 16 17 18  1  2  3  4  5  6  7  8  9] 
cc = np.append(aa, bb, axis = 0)   # 행방향으로 벡터추가 
print(cc)
cc = np.append(aa, bb, axis = 1)   # 열방향으로 벡터추가
print(cc)
print()
print(np.delete(aa, 1))  # [1 3 4 5 6 7 8 9]
print(np.delete(aa, 1, axis = 0))  # 행기준
print(np.delete(aa, 1, axis = 1))  # 열기준

print('--- 조건연산 where(조건, 참, 거짓) ---')
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
condData = np.array([True, False, True])
result = np.where(condData, x, y)
print(result) #[1 5 3]

print()
aa = np.where(x >= 2)
print(x[aa])  # 직접 조건 넣기

print()
kbs = np.concatenate([x, y])
print(kbs)  # 배열 결합
v1, v2 = np.split(kbs, 2)  # 배열 분할 
print(v1)
print(v2)
print()
a = np.arange(1, 17).reshape(4, 4)
print(a)
x1, x2 = np.hsplit(a, 2)  # 세로축 분할
print(x1)
print(x2)

print()
x1, x2 = np.vsplit(a, 2)  # 가로축 분할
print(x1)
print(x2)

print()
# 복원 / 비복원 추출 (default는 비복원 추출)
li = np.array([1, 2, 3, 4, 5, 6, 7])

# 복원 추출
for _ in range(5):
    print(li[np.random.randint(0, len(li) - 1)], end = ' ')

print()
# 비복원 추출
import random
print(random.sample(list(li), k = 5))
print(random.sample(range(1,46), k = 6))

print()
print(list(np.random.choice(range(1, 46), 6)))
print(list(np.random.choice(range(1, 46), 6, replace = True)))  # 복원

print()
arr = 'air book cat d e f god'
arr = arr.split(' ')
print(arr)
print(np.random.choice(arr, 3, p = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.4]))  # 선택 확률 