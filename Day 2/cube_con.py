lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()

ans = 0

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

limit_dict = {'red': 12, 'green': 13, 'blue': 14}


def findPower(draws):
    my_dict = {'red': 0, 'green': 0, 'blue': 0}
    for draw in draws:
        cubes = draw.split(",")
        for cube in cubes:
            cube = cube.strip()
            counts = cube.split(" ")
            my_dict[counts[1]] = max(my_dict[counts[1]], int(counts[0]))

    prod = 1
    for item in my_dict:
        prod *= my_dict[item]
    return prod


def isPossible(draws):
    for draw in draws:
        cubes = draw.split(",")
        for cube in cubes:
            cube = cube.strip()
            counts = cube.split(" ")
            if limit_dict[counts[1]] < int(counts[0]):
                return False
    return True


power = 0
sum = 0
for line in lines:
    game = line.split(":")
    id = game[0].split(" ")[1]
    draws = game[1].split(";")
    sum += findPower(draws)
    if (isPossible(draws)):
        ans += int(id)

print(ans)
print(sum)
