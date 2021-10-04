# numpy 자료형(data Type)

# int float, bool(True, False)

# 정수형
# int 8(-127 ~ 127), 16(-32768 ~ -32767), 32, 64 bit(부호가 있는 정수형)
# uint(unsigned intger) 8(0 ~ 255), 16(65535), 32, 64 bit(양수만 있는 정수형)

# 실수형
# float 16, 32, 64

# 복소수형(complex)
# complex 64 : 두개의 32 bit 부동소수점으로 표시되는 복소수
# complex 128 : 두개의 64 bit 부동소수점으로 표시되는 복소수

# 데이터의 type을 알아보기 위한 dtype 속성 사용

import numpy as np

X = np.float32(1.0)
print(X, X.dtype,"\n")

z = np.arange(5, dtype = 'f') # range()와 쓰는 법 비슷 , array와 range를 합친 느낌
print(z,"\n")

zz = np.array(range(5), dtype = 'f')
print(zz,"\n")

aa = np.arange(2, 3, 0.1) # 2부터 0.1씩 3까지 늘어남 신기~~~~
print(aa,"\n")

zz = np.int8(zz) # 형변환 해주기
print(zz,"\n")
