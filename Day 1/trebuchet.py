with open('input.txt') as f:
    lines = f.readlines()

ans = 0
for line in lines:
    temp = []
    for c in line:
        if c >= '0' and c <= '9':
            temp.append(c)
    number = temp[0]+temp[-1]
    ans += int(number)

print(ans)
