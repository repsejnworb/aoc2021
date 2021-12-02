commands = None
horizontal, depth, aim = (0, 0, 0)

with open('./input.txt', 'r') as fio:
    commands = fio.readlines()

commands = [x.strip('\n') for x in commands]

for command in commands:
    match command.split():
        case ["forward", v]:
            horizontal += int(v)
            depth += aim * int(v)
        case ["down", v]:
            aim += int(v)
        case ["up", v]:
            aim -= int(v)

print(horizontal * depth)

