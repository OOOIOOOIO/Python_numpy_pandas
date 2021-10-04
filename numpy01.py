# Numpy : Numerical Python의 줄임말

# 고성능의 과학계산 컴퓨팅과 데이터 분석에 필요한 기본 패키지
# 빠르고 메모리를 효율적으로 사용하고, 벡터 산술연산과 브로드 캐스팅 기능을 제공함으로써 다차원 배열을 제공
# 반복문을 작성할 필요없이 전체 데이터 배열에 대해서 빠른 연산을 제공
# 배열 데이터를 디스크에 쓰거나, 읽을 수 있는 기능, 메모리에 올려진 파일을 사용
# C나 C++, 포트란으로 짜여진  코드를 통합
# NumPy 자체로는 고수준의 데이터 분석 기능을 제공하지 않기 때문에 pandas를 함께 사용하면 효율적인 작업을 가능


# NumPy의 주요기능
# 벡터 배열상에서 데이터 정제, 개조, 부분집합, 필터링, 변형, 다른 자료형과 연산
# 정렬, 유일한 원소 찾기, 집합 연산 같은 배열 처리 알고리즘, 다른 종류의 데이터 병합


# numpy 배열

# numpy에서 배열은 동일한 타입의 값들을 갖는다. 배열의 차원을 rank라고 한다.
# .shape --> 각 차원의 크기를 튜플로 표시한다
# 파이썬 리스트를 사용하는 방법 --> array() 함수의 인자로 리스트를 넣어 생성한다. ex) array([1, 2, 3])


# numpy에서 제공하는 함수

# zeros((x, y)) : 해당 (x, y)배열을 0으로 초기화
# ones((x, y)) : 해당 (x, y)배열을 1로 초기화
# full((x, y), 값) : 해당 배열을 사용자가 지정한 값으로 초기화
# eye(x) : x * x 단위행렬을 생성한다
# reshape((x, y)) : 다차원으로 변형시키는 함수



import numpy as np

data = np.random.randn(2, 3) # 랜덤으로 2행 3열의 배열을 만듬
print(data)
print()

# numpy.array([리스트]) :  넘파이가 사용하는 특수한 배열 numpy.ndarray로 리턴
x = np.array([1.0, 2.0, 3.0]) # 리스트를 넘겨주면 자동으로 ndarray로 바꿔줌
print("x = ", x)

print("타입 : ", type(x)) # numpy.ndarray 타입

y = np.array([2.0, 4.0, 6.0]) # 1차원 배열

print("y = ", y)

# 계산 --> x와 y의 원소의 수가 같아야 한다.
print("x + y = ", x + y)
print("x - y = ", x - y)
print("x * y = ", x * y)
print("x / y = ", x / y)
print("x * 2 = ", x * 2) # 이런식으로도 가능
print()

A = np.array([[1, 2], [3,4]]) # 2차원 배열
print("A = \n", A)

print("A의 행렬을 보여줌 : ", A.shape) # 2행 2열
print("A 원소의 자료형 : ", A.dtype)

B = np.array([[3, 0],[0, 6]])
print("A = \n", B)

# 다차원 배열의 계산
print("A + B = \n", A + B)
print("A * 10 = \n", A * 10)



# ===========================================================================================


# zeros((x, y))
aa = np.zeros((2, 2))
print("zeros((x, y)) : \n",aa)


# ones((x, y))
aa = np.ones((2, 3))
print("ones((x, y)) : \n",aa)

# full((x, y), 값)
aa = np.full((3, 3), 5)
print("full((x, y), 값) : \n",aa)

# eye(x)
aa = np.eye(4)
print("eye(x) : \n",aa)

# reshape((x, y))
aa = np.array(range(20)).reshape((4, 5)) # 1차원 배열을 4행 5열 이차원 배열로 바꾸기
print("reshape((x, y)) :\n", aa)

# 1차원 배열 : 백터(Vector)
# 2차원 배열 : 행렬 (Matrix)
# 다차원 배열
