# 1이 될 때까지 
#25 5
# k-1, 
N, K = map(int, input().split());
count = 0;

# while N >= K:
#   if (N == 1):
#     break;

#   if(N%K == 0):
#     N /= K;
#     count += 1;
#   else:
#     N -= 1;
#     count += 1;

# print(count);


# while True:
#   target = (N//K) * K; #target = 4*4 = 16
#   print("t=",target);

#   count += (N - target); #count = 1
#   print("c=", count);

#   N = target; # N = 16
#   print("N=", N);
  
#   if N < K:
#     break;

#   count += 1;
#   N //= K;


# count += (N-1);
# print(count);

print((N//K)*K);