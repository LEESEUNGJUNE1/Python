# 배열 연산

import numpy as np
from matplotlib.pyplot import axis

x = np.array([[1, 2],[3, 4]], dtype = np.float64)
print(x, x.dtype)
y = np.arange(5, 9).reshape((2, 2))  # reshape : 차원 변경
y = y.astype(np.float64)  # astype : 형변환
print(y, y.dtype)


print('\n----------- 사칙연산 -----------')
print()
print(x + y)
print(np.add(x, y))

print()
print(x - y)
print(np.subtract(x, y))

print()
print(x * y)
print(np.multiply(x, y))

print()
print(x / y)
print(np.divide(x, y))

print()
v = np.array([9, 10])
w = np.array([11, 12])
print(v * w)  #[99  120]
print()
print(v.dot(w))  # v.dot() : 벡터 내적 연산 v[0] * w[0] + v[1] * w[1]
print(np.dot(v, w)) # 결과값은 scalar

print(x.dot(v))   # x[0,0]*v[0] + x[0,1]*v[1]   x[1,0]*v[0]+x[1,1]*v[1]
print(np.dot(x, v))

print(x.dot(y))
print(np.dot(x, y))

print()
print(np.sum(x))
print(np.sum(x, axis = 0))  # 열에 대한 합
print(np.sum(x, axis = 1))  # 행에 대한 합
print(np.argmax(x), np.argmin(x))  # 최대 최소값의 index를 반환

print()
print(x)
print(x.T)  # .T : 전치(대각의 값을 바꿈, 행과 열의 방향을 바꿔준다.)
print(x.transpose()) # 전치(대각의 값을 바꿈)
print(x.swapaxes(0,1)) # 전치(대각의 값을 바꿈)

print()
# Broadcasting 연산  : 크기가 다른 배열 간 연산을 하면 작은 배열이 큰 배열의 크기에 자동으로 맞춰져 연산
x = np.arange(1, 10).reshape(3, 3)
print(x)
y = np.array([1, 2, 3])
print(x + y)

# file io
datas = np.arange(0, 10, 2)
print(datas)
np.save('test1', datas)  # 파일 저장
np.savetxt('text2.txt', datas)

mydatas = np.loadtxt('text2.txt')  # 파일 읽기
print(mydatas)