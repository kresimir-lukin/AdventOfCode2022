import sys

def parse_commands(commands):
    directory_stack, index = [{}], 0
    while index < len(commands):
        command = commands[index].split()
        if command[1] == 'cd' and command[2] == '..':
            directory_stack.pop()
        elif command[1] == 'cd':
            subdirectory = command[2]
            if subdirectory not in directory_stack[-1]:
                directory_stack[-1][subdirectory] = {}
            directory_stack.append(directory_stack[-1][subdirectory])
        elif command[1] == 'ls':
            while index + 1 < len(commands) and commands[index + 1][0] != '$':
                size, name = commands[index + 1].split()
                directory_stack[-1][name] = {} if size == 'dir' else int(size)
                index += 1
        index += 1
    return directory_stack[0]

def get_directory_sizes(directory_tree):
    sizes = []
    def _traverse_sizes(directory):
        size = 0
        for _, data in directory.items():
            size += _traverse_sizes(data) if type(data) is dict else data
        sizes.append(size)
        return size
    _traverse_sizes(directory_tree)
    return sizes

commands = sys.stdin.read().splitlines()
directory_tree = parse_commands(commands)
sizes = sorted(get_directory_sizes(directory_tree))

part1 = sum(size for size in sizes if size <= 100000)
part2 = next(size for size in sizes if 70000000 - sizes[-1] + size >= 30000000)

print(f'Part 1: {part1}, Part 2: {part2}')