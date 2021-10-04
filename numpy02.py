# numpy에서 제공하는 함수

# zeros((x, y)) : 해당 (x, y)배열을 0으로 초기화
# ones((x, y)) : 해당 (x, y)배열을 1로 초기화
# full((x, y), 값) : 해당 배열을 사용자가 지정한 값으로 초기화
# eye(x) : x * x 단위행렬을 생성한다
# reshape((x, y)) : 다차원으로 변형시키는 함수

# =====================================================================================
import numpy as np

# numpy 슬라이싱

list = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        ]

arr = np.array(list)
# --> 같은 의미 arr = np.array(range(1, 10)).reshape(3, 3)

a = arr[0:2, 0:2] # arr[행, 열]
print("슬라이싱 :\n", a, "\n") # 1~2행, 1~2열 출력 --> 2행 2열

b = arr[1:, 1:] # arr[행, 열]
print("슬라이싱2 :\n", b,"\n") # 2~3행, 2~3열 출력 --> 2행 2열



# numpy 정수 인덱싱(integer indexing)

# numpy 배열 a에 대해서 a[[row1, row2], [col1, col2]]
# a[row, col1] 과 a[row2, col2]의 두개의 배열 요소 집합을 의미한다

list2 = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
        ]

b = np.array(list2)

# 정수 인덱싱
res = b[[0, 2], [1, 3]] # --> a[1, 1], a[2, 3]과 같다. (0부터 1행, 1열 시작 리스트랑 똑같음)
print("정수 인덱싱 :\n", res, "\n") # [2 12] 로 출력


# 불린 인덱싱(boolean indexing) : 요소가 선택 되었는지 안되었는지 보여주는 것

list3 = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        ]

aa = np.array(list3)

b_arr = np.array([
    [False, True, False],
    [True, False, True],
    [False, True, False]
])

n = aa[b_arr] # aa 배열에 b_arr을 넣기
print("불린 인덱싱 :\n", n, "\n")



# 불린 배열을 생성할 때 표현식을 이용하여 생성하기

# 배열 a에 대해서 짝수인 배열 요소만 True로 지정하는 경우
# 배열 aa에 대해 짝수면 True, 홀수면 False
c_arr = (aa % 2 == 0) # 불린 배열 생성

print("표현식을 통해 불린 배열 생성하기 :\n", c_arr, "\n") # b_arr과 같은 값이 나옴

print("불린 인덱싱2 :\n", aa[c_arr], "\n")

print("배열에 조건을 넣어 불린 인덱싱 사용하기 :\n", aa[aa % 2 == 0], "\n")
