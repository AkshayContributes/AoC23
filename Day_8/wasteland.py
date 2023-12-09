from pathlib import Path
from math import gcd


def create_map(data):
    map_nodes = {}
    for line in data:
        line = line.split(" = ")
        map_nodes[line[0]] = (line[1].split(", ")[0][1:],
                              line[1].split(", ")[1][:-1])
    return map_nodes


def count_steps(q_inst, map_nodes):
    steps = 0
    curr_loc = 'AAA'
    while q_inst:
        if curr_loc == 'ZZZ':
            return steps
        curr_inst = q_inst.pop(0)
        steps += 1
        if curr_inst == 'L':
            curr_loc = map_nodes[curr_loc][0]
        else:
            curr_loc = map_nodes[curr_loc][1]
        q_inst.append(curr_inst)
    return


def parse_input():
    data = Path("input.txt").read_text().splitlines()
    instructions = data.pop(0)
    data.pop(0)
    return instructions, data


inst, data = parse_input()

map_nodes = create_map(data)

print(count_steps(list(inst), map_nodes))

positions = [key for key in map_nodes.keys() if key.endswith('A')]

cycles = []


def find_cycles(positions, q_inst, map_nodes):

    for pos in positions:
        cycle = []
        current_steps = q_inst
        first_z = None
        steps_count = 0
        while True:
            while steps_count == 0 or not pos.endswith('Z'):
                steps_count += 1
                pos = map_nodes[pos][0 if current_steps[0] == 'L' else 1]
                current_steps = current_steps[1:] + current_steps[0]

            cycle.append(steps_count)
            if first_z == None:
                first_z = pos
                steps_count = 0
            elif pos == first_z:
                break

            cycles.append(cycle)


def find_lcm(cycles):
    lcm = cycles.pop(0)[0]
    for i in cycles:
        lcm = lcm * i[0] // gcd(lcm, i[0])
    return lcm


find_cycles(positions, inst, map_nodes)

print(find_lcm(cycles))
