# 박서원 202101391 컴퓨터공학부
# 부계정 repository 수정문
# 3-1-1 첫번째 수정 요청 - merge 하지 않은 채로 두 번째 수정 요청
# 3-1-2 수정요청
# 부계 3-2-3 수정
# numpy 설치 바람
import numpy as np # np라는 이름으로 축약하여 numpy를 실행하겠다.

a = np.array([1, 2.5, 4, 5.5, 7.0])
a[3:]
"""
세 함수 한 번에 출력 안 됨 - 마지막 함수만 출력되는 것 같음
"""
#a.sum() # np.array로 생성한 변수 a의 합을 출력
#a.std() # np.array로 생성한 변수 a의 표준편차를 출력
#a.cumsum() # np.array로 생성한 변수 a의 누적 합을 출력

"""
print
"""
print(a, sep = "")
print(a*2, sep = "")
print(a**2, sep = "")
print(np.sqrt(a), sep = "")
