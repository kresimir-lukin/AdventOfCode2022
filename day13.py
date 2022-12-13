import sys

def cmp(x, y):
   return (x > y) - (x < y)

def compare(pair1, pair2):
    if type(pair1) is int and type(pair1) is int:
        return cmp(pair1, pair2)
    for el1, el2 in zip(pair1, pair2):
        if type(el1) != type(el2):
            el1 = [el1] if type(el1) is int else el1
            el2 = [el2] if type(el2) is int else el2
        cmp_result = compare(el1, el2)
        if cmp_result != 0:
            return cmp_result
    return cmp(len(pair1), len(pair2))

def count_lower(packets, divider):
    return sum(compare(packet, divider) < 0 for packet in packets)

input_packets = sys.stdin.read().splitlines()
packets = []
for i in range(0, len(input_packets), 3):
    packets.append(eval(input_packets[i]))
    packets.append(eval(input_packets[i+1]))

part1 = sum(i//2+1 for i in range(0, len(packets), 2) if compare(packets[i], packets[i+1]) < 0)
part2 = (count_lower(packets, [[2]]) + 1) * (count_lower(packets, [[6]]) + 2)

print(f'Part 1: {part1}, Part 2: {part2}')