# 문자열 
# 초기화 : "", ''

data = 'Hello World'
print(data)

data = "Don't you know \"Python\"?"
print(data)

#문자열 연산
# +(연결, concatenate) *

a = 'Hello'
b = 'World'
print(a + " "+b)

a = "string"
print(a * 3)

a = "ABCDE"
print(a[2:4])

#오류
# a[2] = 'C'
# print(a)

# 튜플 자료형
# 한번 선언되면 변경 불가, 소괄호 사용 ()
# 리스트에 비해 적은 메모리 사용 > 공간 효율적
#서로다른 성질의 데이터를 묶어서 관리해야할 때 사용 (최단 경로 알고리즘에서 (비용, 노드번호) 의 형태 )
# 데이터의 나열을 해싱의 키값으로 사용해야할 때 
a = (1,2,3,4,5,6,7,8)

print(a[3])
print(a[1:4])

#오류
# a[2] = 7

# 사전 자료형 
# 키와 값의 쌍을 데이터로 가지는 자료형
# 변경불가능한 자료형을 키로 사용
# 해시 테이블 이용 > 데이터 조회/수정 O(1)의 시간에 처리 가능

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
  print('사과 존재 ')

#키 : keys(), 값 : values()

key_list = data.keys()
value_list = data.values()

print(key_list)
print(value_list)

for key in key_list:
  print(data[key])


a = dict()
a['홍길동'] = 98
a['이순신'] = 120

print(a)

b = {'홍길동' : 97, '이순신' : 192}

print(b)

key_list = list(b.keys())
print(key_list)

#집합 {}  > 중복 허용 x, 순서 없음
#set() , 존재여부 확인에 유용
#데이터 조회/수정 O(1)의 시간에 처리 가능
data = set([1,2,3,4,5,5,5,6])
print(data)

data = {1,1,2,3,4,5,6,6,6}
print(data)

#합집합, 교집합, 차집합
a = set([1,2,3,4,5])
b = set([3,4,5,6,8])

#합, 교, 차
print(a|b)
print(a&b)
print(a-b)

data = set([1,2,3])

data.add(4)

data.update([5,6])

data.remove(3)

print(data)

#리스트, 튜플 : 순서 o > 인덱싱가능
#사전, 집합 : 순서 x > 인덱싱 x, 사전의 Key, 집합의 원소 O(1) 의 시간 복잡도 조회
