from pathlib import Path
from collections import deque


def parse_input():
    data = Path('input.txt').read_text().splitlines()
    return [[y for y in x] for x in data]


input_graph = parse_input()
grid = [[0] * len(input_graph[0]) for _ in range(len(input_graph))]


start = (-1, -1)

for i in range(len(input_graph)):
    for j in range(len(input_graph[i])):
        if (input_graph[i][j] == 'S'):
            start = (i, j)
            break
        else:
            continue
        break

seen = {start}
grid[start[0]][start[1]] = 0

q = deque([start])

maybe_s = {"|", "7", "J", "L", "F", "-"}


while q:
    r, c = q.popleft()
    ch = input_graph[r][c]
    if r > 0 and ch in "S|JL" and input_graph[r-1][c] in "|F7" and (r-1, c) not in seen:
        seen.add((r-1, c))
        q.append((r-1, c))
        grid[r-1][c] = grid[r][c] + 1
        if ch == "S":
            maybe_s &= {"|", "J", "L"}

    if r < len(input_graph)-1 and ch in "S|7F" and input_graph[r+1][c] in "|JL" and (r+1, c) not in seen:
        seen.add((r+1, c))
        q.append((r+1, c))
        grid[r+1][c] = grid[r][c] + 1
        if ch == "S":
            maybe_s &= {"|", "7", "F"}

    if c > 0 and ch in "S7J-" and input_graph[r][c-1] in "-LF" and (r, c-1) not in seen:
        seen.add((r, c-1))
        q.append((r, c-1))
        grid[r][c-1] = grid[r][c] + 1
        if ch == "S":
            maybe_s &= {"-", "J", "7"}

    if c < len(input_graph[r])-1 and ch in "S-LF" and input_graph[r][c+1] in "-7J" and (r, c+1) not in seen:
        seen.add((r, c+1))
        q.append((r, c+1))
        grid[r][c+1] = grid[r][c] + 1
        if ch == "S":
            maybe_s &= {"-", "L", "F"}
            print(maybe_s)


res = 0


for i in range(len(grid)):
    for j in range(len(grid[i])):
        res = max(res, grid[i][j])


print(res)

grid = []


for i in range(len(input_graph)):
    str = ""
    for j in range(len(input_graph[i])):
        if (i, j) in seen:
            if input_graph[i][j] == "S":
                str += maybe_s.pop()
            else:
                str += input_graph[i][j]
        else:
            str += "."
    grid.append(str)

count = 0


def count_inversions(i, j):
    line = grid[i]
    count = 0
    for k in range(j):
        if not (i, k) in seen:
            continue
        count += line[k] in {"7", "F", "|"}
    return count


ans = 0
for i, line in enumerate(grid):
    for j in range(len(line)):
        if not (i, j) in seen:
            invs = count_inversions(i, j)
            if invs % 2 == 1:
                ans += 1
print(ans)
