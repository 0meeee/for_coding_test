def recursive_func(i):
    if i == 100:
        return
    print(i, "번째 재귀함수에서", i+1, "번째 재귀함수를 호출한다.")
    recursive_func(i+1)
    print(i, "번째 재귀함수를 종료한다.")

#반복문 이용해 구현
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

#재귀적으로 구현
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

print('반복적 : ', factorial_iterative(5))
print('재귀적 : ', factorial_recursive(5))
#recursive_func(1)