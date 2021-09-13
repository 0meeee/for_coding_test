#함수와 람다 표현식

# 내장함수, 사용자 정의함수
 
def add(a,b):
  return a + b;

print(add(10,2))

def add2(a,b):
  print("함수의 결과 ", a+b)

add2(3,1)

def subtract(a,b):
    return a-b;

print(subtract(3,6))

print(add(b =10, a =2))

#global 키워드

a = 0

def func():
    global a 
    a += 1

for i in range(10):
    func()

print(a)

array = [1,2,3,4,5]

def func():
    array = [3,4,5]
    array.append(6)
    print(array)

func()
print(array)

#람다 표현식
print((lambda a, b : a+b)(3,6))

array = [('a', 50), ('b', 30), ('c', 20)]

def my_key (x):
    return x[1]

print(sorted(array, key = my_key))
print(sorted(array, key = lambda x : x[1]))

list1 = [1,2,3,4,5]
list2 = [5,6,7,8,9]

result = map(lambda a,b, : a+b, list1, list2)

print(list(result))