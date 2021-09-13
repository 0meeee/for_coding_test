#조건문
x = 15
if x >= 10 :
  print("x >= 10")
if x >= 0:
  print("x >= 0")
if x>=30:
  print("x>=30")

#코드의 블록을 들여쓰기(indent)로 지정

a = -15

if a >=0:
    print("a>=0")
elif a >= -10:
    print("0>a >= -10")
else :
    print("-10 > a")

score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")

# 비교 연산자
# ==, !=, >, <, >=, <=

# 논리 연산자
# and, or, not 

a = 15

if a<= 20 and a>0:
    print("Y")

#in, not in 연산자
#리스트, 튜플, 문자열, 딕셔너리 모두 사용가능

#pass 키워드
#디버깅에서 ..
score = 86

if score > 80:
    pass
else:
    print("a<=80")

# 조건문 간소화
score = 85

if score >= 80: result = "success"
else : result = "fail"

print(result)

result1 = "success" if score > 80 else "fail"

print(result1)

#반복문
i =1
result =0

while i <= 9:
    if i%2 == 1:
      result += i
    i += 1

print(result)

# # 무한루프
# x = 10

# while x > 5:
#     print(x)

# for 문
array = (9, 8,7,6,5)

for x in array:
    print(x)

result =0

for i in range(1, 31):
    result += i
print(result)

#continue 키워드
result = 0
for i in range(1,10):
    if i %2 == 0:
        continue
    result += i
print(result) 

#break
i = 1
while True:
    print("현재 i " , i)
    if i == 5:
        break
    i += 1

score = [90, 85, 77, 65, 97]

# # i = 0 ~ 4
# for i in range(5):
#     if score[i] >= 80:
#         print(i + 1, "번 학생 합격")

cheating_student_list= {2,4}

for i in range(5):
    if i+1 in cheating_student_list:
        continue
    if score[i] >= 80:
        print(i +1, "번 학생 합격")

#이중 for 문
for i in range(2, 10):
    for j in range(1, 10):
        print(i, "X", j , "= ", i*j)
    print()


