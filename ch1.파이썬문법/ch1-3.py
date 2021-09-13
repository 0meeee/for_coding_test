#기본 입출력

#input () : 한줄의 문자열 입력받는 함수
#map () : 리스트의 모든 원소에 각각 특정한 함수 적용할 때

# n = int(input())

# data = list(map(int, input().split()))

# data.sort(reverse = True)
# print(data)

# #입력 최대한 빠르게 받아야하는 경우 : sys.stdin.readline()
# #rstrip() : 엔터, 줄바꿈 기호 제거

# import sys

# data = sys.stdin.readline().rstrip()

# print(data)

a = 1
b = 1
print(a,b)

print(7, end = " ")
print(8, end = " ")

answer =7
print("정답은" + str(answer) +"입니다.")

# f string
answer =7
print(f"정답은 {answer}입니다.")