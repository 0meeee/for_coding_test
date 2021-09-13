data = input()
int_Result =0
result = []

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        int_Result += int(x)

result.sort()

if int_Result != 0:
    result.append(str(int_Result))

print(result)
print(''.join(result))