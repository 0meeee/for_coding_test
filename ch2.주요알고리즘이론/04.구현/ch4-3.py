# 입력 : a1 > 열, 행 정보
# 출력 : 이동할 수 있는 경우의 수 

# 이동경로 : [(-2, -1), (-2,1), (2,1),(2,-1), (1,2),(-1,2), (1,-2),(1,2)]

input_data = input();

row = int(input_data[1]);
column = int(ord(input_data[0])) - int(ord('a')) +1;

# print(row, column);

steps = [(-2, -1), (-2,1), (2,1),(2,-1), (1,2),(-1,2), (1,-2),(1,-2)];

result = 0;

for step in steps:
  next_row = row+ step[0];
  next_column = column + step[1];

  if next_row >=1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
    result += 1;
    # print(next_row, next_column);

print(result);