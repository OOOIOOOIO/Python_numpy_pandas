# numpy 연산

# 연산자를 이용할 경우 : +, -, *, /

# 함수를 사용할 경우
# add(x, y)
# substract(x, y)
# multiply(x, y)
# divide(x, y)

# 배열 a와 배열 b가 있을 때, a + b --> a[0] + b[0]...각 요소가 더해지는 방식

import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("연산자 더하기 :\n", a + b, "\n")

c = np.add(a, b)

print("함수 더하기 :\n", c, "\n")

print("연산자 빼기 :\n", a - b, "\n")

c = np.subtract(a, b)

print("함수 빼기 :\n", c, "\n")

print("연산자 곱하기 :\n", a * b, "\n")

c = np.multiply(a, b)

print("함수 곱하기 :\n", c, "\n")

print("연산자 나누기 :\n", a / b, "\n")

c = np.divide(a, b)

print("함수 나누기 :\n", c, "\n")

print("======================================================================\n")

# Matrix

list1 = [
[1, 2],
[3, 4]
]

list2 = [
[5, 6],
[7, 8]
]

a = np.array(list1)
b = np.array(list2)

# numpy에서 vector와 matrix의 product(곱셈)를 구하기 위해서는 dot() 함수를 사용한다.
print("두 matrix에 대한 product 구하기\n")

product = np.dot(a, b) # 행렬의 곱셈
print(product)

# numpy에서는 배열간의 연산을 위한 여러 함수둘을 제공
# sum() : 각 배열의 요소를 더하는 함수
# prod() 배열의 요소들을 곱하는 함수
# --> axis 옵션을 사용한다. (add, multiply와 다른 점)
# axis = 0 --> col 끼리 더함 / axis = 1 --> row 끼리 더함

a = np.array([[1, 2],
            [3, 4]])

s = np.sum(a) # 모든 요소 더하기
print(s)

s = np.sum(a, axis = 0) # column 끼리 더하기
print(s)

s = np.sum(a, axis = 1) # row 끼리 더하기
print(s)

p = np.prod(a) # 모든 요소 곱하기
print(p)

p = np.prod(a, axis = 0) # column 끼리 곱하기
print(p)

p = np.prod(a, axis = 1) # row 끼리 곱하기
print(p)
