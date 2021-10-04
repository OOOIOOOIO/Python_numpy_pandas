import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# DataFrame : 2차원배열 같은 자료구조
# R언어의 data.frame과 비슷하다.

a = pd.DataFrame([
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
])

print(a, "\n")

data = { # coulum으로 들어감
"city" : ["서울", "부산", "광주", "대구"],
"year" : [2000, 2001, 2002, 2003],
"population" : [4000, 2000, 1000, 1000]
}

df = DataFrame(data) # coloum으로 넣어진다.
print(df, "\n")

# column 위치 재설정하기
df = DataFrame(data, columns = ["population", "year", "city"])
print(df, "\n")

# 없는 칼럼 넣어보기
df2 = DataFrame(data, columns = ["population", "year", "city", "newnew"])
print(df, "\n") # NAN으로 추가됨

# 인덱스 넣어보기
df2 = DataFrame(data, columns = ["population", "year", "city", "newnew"], index = ['one', 'two', 'three', 'four'])
print(df, "\n")


# 데이터 추출해보기
print(df['city'], "\n")
print(df['population'], "\n")

print(df.columns, "\n") # column만 가져오기
print(df.index, "\n") # index(row)만 가져오기

# DataFrame.loc : 색인(index 행)를 label이나 조건표현으로 추출하는 법
# DataFrame.iloc : 색인(index 행)를 인덱스번호로 추출하는 법(슬라이싱도 가능)
print(df2.loc["three"], "\n") # 3행 출력
print(df2.iloc[0 : 3], "\n") # 1~ 3행 출력(0 ~ 2)


# newnew column 초기화
df2["newnew"] = [1000, 2000, 3000, 4000] # 그냥 = 1000 처럼 스칼라 값도 넣을 수 있음
print(df2, "\n")

 # 넘파이 사용해서 넣기
df2["newnew"] = np.arange(4)
print(df2, "\n")


# Series를 이용해보기

 # 인덱스가 0, 1, 2, ...정해져 있기 때문에 인덱스가 일치하지 않아 NaN이 들어가진다
 # 따라서 인덱스를 맞게 맞춰줘야한다. 인덱스를 맞춰주는 곳에 값이 들어간다.
 # 인덱스를 통해 넣고자 하는 곳에 값을 할당시킬 수 있다.
val = Series([4000, 3000, 2000, 1000], index = ["four", "one", "three", "two"])

df2["newnew"] = val # val.values 하면 값이 들어감


# 불린 칼럼 넣어보기
df2["aaa"] = df2.city == "서울"
print(df2, "\n")

# 칼럼 삭제하기
del(df2["aaa"])
print(df2, "\n")


data2 = {
"seoul" : {2001 : 20, 2002 : 30},
"busan" : {2003 : 30, 2004 : 40, 2005 : 50}
} # --> 바깥쪽 key는 column으로 안에 있는 딕셔너리의 key는 index(row)로 간다.

df3 = DataFrame(data2)
print(df3, "\n")
