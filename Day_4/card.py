from pathlib import Path

data = Path('input.txt').read_text().splitlines()

sum = 0
solution = [1] * len(data)
for i, line in enumerate(data):
    card = line.split(":")[1]
    left, right = card.split(" | ")
    winning = left.split()
    on_hand = right.split()
    temp = 0
    count = 0

    # part 1
    for ele in winning:
        if ele in on_hand:
            count += 1
            temp = 1 if temp == 0 else temp*2
    sum += temp

    # part 2
    for j in range(count):
        solution[i+j+1] += solution[i]

print(sum)
sum2 = 0
for i in solution:
    sum2 += i
print(sum2)
