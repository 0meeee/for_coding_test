# #각 행마다 가장 작은 수를 고르고, 그 중 큰 수를 고른다.

# N, M = map(int, input().split());

# result =0;

# # for i in range(N):
# #   data = list(map(int, input().split()));
# #   min_value = min(data);

# #   result = max(result, min_value);

# # print(result);


# for i in range(N):
#   data = list(map(int, input().split()));

#   min_value = 10001;

#   for d in data:
#     min_value = min(d, min_value);
  
#   result = max(min_value, result);

# print(result);

# N X M : N 행 M 열
# 각 행에서 가장 낮은 수 고름 
# # (1)
# n, m = map(int, input().split());
# result = 0;
# for i in range(n):
#   numbers = list(map(int, input().split()));

#   min_value = min(numbers);

#   result = max(min_value, result);

# print(result);
