import sys, math

def get_modulo(monkeys):
    return math.lcm(*map(lambda m: m['test'], monkeys))

def run_rounds(monkeys, rounds, worry_divisor):
    inspected = [0]*len(monkeys)
    modulo = get_modulo(monkeys)
    monkey_items = [monkey['items'][:] for monkey in monkeys]
    for _ in range(rounds):
        for i, monkey in enumerate(monkeys):
            while monkey_items[i]:
                item = monkey_items[i].pop(0)
                operation = monkey['operation'].replace('old', str(item))
                value = eval(operation) // worry_divisor
                target_monkey = monkey['true'] if value % monkey['test'] == 0 else monkey['false']
                monkey_items[target_monkey].append(value if worry_divisor != 1 else value % modulo)
                inspected[i] += 1
    inspected.sort()
    return inspected[-1] * inspected[-2]

input_monkeys = sys.stdin.read().splitlines()
monkeys = []
for i in range(0, len(input_monkeys), 7):
    starting_items = input_monkeys[i+1].split(':')[1]
    monkeys.append({
        'items': list(map(int, starting_items.split(','))),
        'operation': input_monkeys[i+2].split('=')[1].strip(),
        'test': int(input_monkeys[i+3].split()[-1]),
        'true': int(input_monkeys[i+4].split()[-1]),
        'false': int(input_monkeys[i+5].split()[-1])
    })

part1 = run_rounds(monkeys, 20, 3)
part2 = run_rounds(monkeys, 10000, 1)

print(f'Part 1: {part1}, Part 2: {part2}')