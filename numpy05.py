# numpy 브로드캐스트
import numpy as np
a = np.array([[1, 2,], [3, 4]])

b = 10

c = a * b #c = np.multiply(a, b) 값이 같음
print(c,"\n") #10, 20, 30 ,40 -->  10이 각 요소에 곱해짐

x = np.array([[1, 2], [3, 4]])
y = np.array([10, 20]) # [[10], [20]]


z = x * y # 행렬의 곱과는 다름
print(z,"\n") #10, 40, 30, 80 --> 10, 20이 각 행의 위치에 곱해짐(열도 마찬가지)


x = np.array([[11, 21],
             [34, 44],
             [0, 9]])

print(x, "\n")
# for row in x :
    # print(row)


# 2차원 배열을 1차원 배열로 변환(평탄화) : flatten()
x = x.flatten()
print(x, "\n")

print(x[np.array([1, 3, 5])], "\n") # [np.array([1, 3 , 5])] -->  1, 3, 5 인덱싱

print(x[x > 25], "\n") # [x > 25] --> 조건이   참인 경우만 출력
print(x > 25, "\n") # 넘파이 배열에 부등호 연산자를 쓸 경우 boolean 형으로 출력 됨
