#내장함수
#itertools : 반복 형태(순열, 조합) > 완전탐색
#heapq : 힙 자료구조, 우선순위 큐
#bisect : 이진 탐색 기능
#collections : 덱, 카운터 등
#math : 수학기능 (팩토리얼, 제곱근, 최대공약수, 삼각함수 ..)

#내장함수
result = sum([1,2,3,4,5])
print(result)

min_v = min(7,5,33,2)
max_v = max(4,3,2,5)
print(min_v, max_v)

result = eval("(3+5)*7")
print(result)

result = sorted([7,55,2,3,1,2,3])
reverse_result = sorted([7,55,2,3,1,2,3], reverse = True)

print(result)
print(reverse_result)

array = [('a', 1), ('b', 2), ('c', 3)]

result = sorted(array, key = lambda x : x[1], reverse =True)

print(result)

#순열과 조합
#순열 : 서로다른 n개에서 서로 다른 r개 선택해 일렬로 나열하는것
#조합 : 순서 상관없이 서로다른 n개에서 서로 다른 r개 선택
from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']

result = list(permutations(data,3))
print('순열 ', result)
print()

data = ['A', 'B', 'C']
#2개씩 뽑는 모든 조합 구하기
result = list(combinations(data,2))
print('조합 ', result)
print()

#2개씩 뽑는 모든 순열 (중복순열)
result = list(product(data, repeat = 2))
print('중복순열 ', result)
print()

#2개씩 뽑는 모든 조합 (중복 조합)
result = list(combinations_with_replacement(data,2))
print('중복 조합 ', result)

#counter : 등장 횟수
from collections import Counter

counter = Counter(['r', 'b', 'r', 'g', 'b', 'b'])

print(counter['b'])
print(counter['g'])

print(dict(counter))

import math

def lcm(a,b):
    return a * b // math.gcd(a,b)

a = 21
b = 14

print(math.gcd(21, 14)) # 최대 공약수
print(lcm(21,14)) # 최소 공배수

