from pathlib import Path


data = Path("input.txt").read_text().splitlines()


def find_first(levels):
    for i in range(len(levels)-2, -1, -1):
        levels[i].insert(0, levels[i][0]-levels[i+1][0])
    return levels[0][0]


def create_sim(levels):
    for i, level in enumerate(levels):
        level = [int(x) for x in level]
        if (sum(level) == 0):
            break
        next_level = []
        for j in range(1, len(level)):
            next_level.append(level[j] - level[j-1])
        levels.append(next_level)
    return levels


def find_last(line):
    levels = []
    levels.append(line)
    levels = create_sim(levels)

    levels[-1].append(0)
    for i in range(len(levels)-2, -1, -1):
        levels[i].append(levels[i+1][-1]+levels[i][-1])

    return levels[0][-1], find_first(levels)


sum_1, sum_2 = 0, 0

for (i, line) in enumerate(data):
    a, b = find_last([int(x) for x in line.split()])
    sum_1 += a
    sum_2 += b

print(sum_1, sum_2)
