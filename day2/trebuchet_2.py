with open('input.txt') as f:
    lines = f.readlines()


def calculate(line=str):
    temp = []
    for c in line:
        if c >= '1' and c <= '9':
            temp.append(c)
    number = temp[0]+temp[-1]
    return int(number)


ans = 0
for line in lines:
    line = line.replace('one', 'o1e')
    line = line.replace('two', 't2o')
    line = line.replace('three', 't3e')
    line = line.replace('four', 'f4r')
    line = line.replace('five', 'f5e')
    line = line.replace('six', 's6x')
    line = line.replace('seven', 's7n')
    line = line.replace('eight', 'e8t')
    line = line.replace('nine', 'n9e')
    number = calculate(line)

    with open('output.txt', 'a') as f:
        f.write(str(line)+"\n")
        f.close()
    ans += number

print(ans)
