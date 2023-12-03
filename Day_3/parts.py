from pathlib import Path
from collections import deque


def consume(data: list[str], x: int, y: int, visited: set[tuple[int, int]]):

    dq = deque()
    i, j = x, y
    while isData(i, j, data) and (c := data[i][j]).isdigit():
        dq.appendleft(c)
        visited.add((i, j))
        j -= 1

    j = y+1
    while isData(i, j, data) and (c := data[i][j]).isdigit():
        dq.append(c)
        visited.add((i, j))
        j += 1

    return int(''.join(dq)) if dq else 0


def isData(x: int, y: int, data: list[str]):
    return x >= 0 and x < len(data) and y >= 0 and y < len(data[x])


def dfs(data=list[str], visited=set[tuple[int, int]], i=int, j=int, part2=False) -> int:
    nums = []
    for dx, dy in [(0, -1), (-1, 0), (0, 1), (1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
        x, y = i+dx, j+dy
        if isData(x, y, data) and data[x][y].isdigit() and (x, y) not in visited:
            nums.append(consume(data, x, y, visited))
    if part2:
        if data[i][j] == '*' and len(nums) == 2:
            return nums[0] * nums[1]
        return 0
    return sum(nums)


def solutions():
    data = Path("input.txt").read_text().splitlines()
    visited1, visited2 = set(), set()
    sol1, sol2 = 0, 0
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if not char.isdigit() and char != '.':
                sol1 += dfs(data, visited1, i, j)
                sol2 += dfs(data, visited2, i, j, part2=True)

    return sol1, sol2


sol1 = solutions()
print(sol1)
