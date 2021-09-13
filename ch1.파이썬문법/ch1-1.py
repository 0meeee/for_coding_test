#1.자료형
#정수형
a = 5
print(a)

#실수형
a = 158.93
print(a)

a = -1.2
print(a)

a = 5.
print(a)

a = -.7
print(a)

#지수형 > 실수형
a = int(1e9)
print(a)

a = 75.25e1
print(a)

a = 3954e-3
print(a)

a = 0.3 + 0.6
print(a)

if a == 0.9:
  print(True)
else:
  print(False)

# 반올림  round()

a = 0.3 + 0.6
print(round(a,1))

if round(a,1) == 0.9:
  print(True)
else:
  print(False)

# 나머지 % : 파이썬에서는 결과 실수형으로 반환
# 몫 // , 거듭제곱 **
a = 7
b = 3

print(a/b) 
print(a//b)
print(a%b)
print(a**b)

#리스트 [] = 배열, 테이블
# list(), []

a = [1,2,3,4,5,6,7,8,9]
print(a)

#인덱스 0 부터 시작
print(a[3])
print(a[-1])

#슬라이싱 : 끝인덱스는 실제보다 1 크게함
print(a[1:4])

n = 10
a = [0] * n
print(a)

#리스트 컴프리핸션
array = [i for i in range(10)]

print(array)

#0~19 까지의 수 중 홀수만 포함하는 리스트
value = [i for i in range(20) if i%2 == 1]
print(value)

#1~9까지의 수들의 제곱값을 포함하는 리스트
value = [i**2 for i in range(1,10)]
print(value)

#n X m 크기의 2차원 리스트 
n = 4
m = 3
array = [[0]*m for _ in range(n)]
array[1][1] = 5
print(array)

#잘못된 방법
array = [[0]*m] * n
print(array)
array[1][1] = 5
print(array) 

#언더바 _ : 반복수행할때 반복을 위한 변수의 값 무시할 때
for _ in range(5):
  print("Hello World!")

#append, sort, reverse, insert, count, remove

a =[1,2,3,4,5,5,5,5]

remove_set = {3,5}

result = [i for i in a if i not in remove_set]
print(result)