"""
 Pandas : 데이터 분석 기능을 제공하는 라이브러리

 예를 들면, CSV 파일 등의 데이터를 읽고 원하는 데이터 형식으로 변환해줌

 pandas 자료구조 : Series, DataFrame

 Series : 일차원 배열 같은 자료구조, 파이썬의 딕셔너리와 비슷하다 {"index" : value} 느낌
        enumurate와 비슷 (인덱스번호 = 색인)
"""

import pandas as pd
from pandas import Series, DataFrame

obj = Series([11, 22, 33, 44]) # 객체 생성,
print(obj, "\n")

print(obj.values, "\n") # 배열의 값만 출력

print(obj[1], "\n") # 인덱싱

print(obj.index, "\n") # index를 보여줌 range()와 비슷



obj2 = Series([1, 2, 3, 4], index = ['a', 'b', 'c', 'd']) # index를 내가 설정할 수 있음
print(obj2, "\n")

print(obj2['c'], "\n") # 인덱스로 출력하기

print(obj2[['a', 'b']], "\n") # arr[[0, 1, 3]] 이런 식으로 []하나를 더 써줘서 멀티인덱싱 가능

print(obj2 * 2, "\n") # 연산도 가능

print("b" in obj2, "\n") # obj2의 "인덱스"가 있는지 검사


# 딕셔너리
data = {"kim" : 3400,
        "hong" : 2200,
        "kang" : 2000,
        "lee" : 2400}

obj3 = Series(data) # 키 --> 인덱스, 밸류 --> 배열

print(obj3, "\n")


# 누락된 데이터 확인
name = ['woo', 'hong', 'kang', 'lee']

obj4 = Series(data, index = name)

print(obj4, "\n") # woo가 없기 때문에 NaN이 나옴 Not a Number


# 누락된 데이터를 찾을 때 사용하는 함수 isnull, notnull
# boolean형으로 나옴 numpy boolean 인덱싱같은 느낌
print(pd.isnull(obj4), "\n") # null이면 True

print(pd.notnull(obj4), "\n") # null이 아니면 False



# Series 연습
data = { # index에 들어감(row) // DataFrame은 column에 들어감
    "Seoul" : 4000,
    "Busan" : 2000,
    "Incheon" : 1500,
    "Bucheon" : 1000,
}

obj = Series(data) # 객체 생성
print(obj, "\n")


city = ["Seoul", "Daegu", "Incheon", "Bucheon"]

obj2 = Series(data, index = city) # 인덱스 넣기
# obj2.index = ["Daejeon", "Busan", "Jaeju", "Jeonju"] # index 넣는 법
print(obj2, "\n")


print(obj + obj2, "\n") # 겹치지 않으면 NAN 뜸

# Series 객체와 SEries의 색인(index)은 모두 name이라는 속성이 있다.
obj.name = "인구수" # 객체의 속성 지정
obj.index.name = "지역" # 색인의 속성 지정
print(obj)
