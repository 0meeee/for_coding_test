
# 가장 큰수 K번 더하고, 두번째로 큰수 한번 더하는 연산 반복 

#N : 배열의 크기, M : 숫자가 더해지는 총 횟수, K : 한 숫자당 더해질 수 있는 최대 횟수

N, M, K = map(int, input().split());
data = list(map(int, input().split()));

data.sort();

first = data[N-1];
second = data[N-2];

# result = 0;

# while True:
#   for i in range(K):
#     if M == 0:
#       break;
#     result += first;
#     M -= 1;
#   if M == 0:
#     break;
  
#   result += second;
#   M -= 1;

# print(result);

# count : 큰 수가 더해지는 횟수
# n, m, k : 5 8 3
# 2 4 5 4 6

#m/(k+1) : 8/4 > 2*3 = 6

count = int(M/(K+1)) * K;
count += M%(K+1);

result = 0;
result = count * first;
result += (M-count)* second;

print(result);



# #다양한 수로 이뤄진 배열이 있다.
# #M 번 더해 가장 큰 수 만들기
# #특정 인덱스의 수가 K번 초과해 더해질 수 없음

# # [2,4,5,4,6], K = 3, M =8

# # 6 6 6 5 6 6 6 5

# # n = 배열의 크기
# n, m, k  = map(int, input().split());
# numbers = list(map(int, input().split()));

# # print(n, m, k);
# # print(numbers);

# # 가장 큰수 k번, 두번째로 큰수 1번 > 총 M 번

# numbers = sorted(numbers)

# first = numbers[n-1];
# second = numbers[n-2];

# result = 0;

# while 1:
#   for i in range(k):
#     result += first;
#     m -= 1;
#     if(m <= 0):
#       break;

#   result += second;
#   m -= 1;

#   if m <= 0:
#     break;

# print(result);