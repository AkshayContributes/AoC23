from pathlib import Path
from functools import reduce


def parse_input():
    data = Path("input.txt").read_text().splitlines()
    record = list(map(int, data.pop().split(": ")[1].strip().split()))
    time = list(map(int, data.pop().split(": ")[1].strip().split()))
    return record, time


def find_max(time, record, min_s):
    max_s = time
    ans = time
    while (min_s <= max_s):
        mid_s = (min_s + max_s) // 2
        dist = (mid_s * (time - mid_s))
        if dist > record:
            min_s = mid_s+1
        else:
            ans = mid_s
            max_s = mid_s-1
    return ans


def find_min(time, record):
    min_s = 0
    max_s = time
    ans = time
    while (min_s <= max_s):
        mid_s = (min_s + max_s)//2
        dist = mid_s * (time - mid_s)
        if dist <= record:
            min_s = mid_s + 1
        else:
            ans = mid_s
            max_s = mid_s-1
    return ans


def p1(times, records):
    prod = 1

    def find(time, record):

        min_speed = find_min(time, record)

        max_speed = find_max(time, record, min_speed)

        return (max_speed - min_speed)

    for i, time in enumerate(times):
        prod *= find(time, records[i])

    return prod


records, times = parse_input()
print(p1(times, records))
time = ""
record = ""
for item in times:
    time += str(item)

for item in records:
    record += str(item)


print(p1([int(time)], [int(record)]))
