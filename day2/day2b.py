commands = None
x, y = (0, 0)

with open('./input.txt', 'r') as fio:
    commands = fio.readlines()

commands = [x.strip('\n') for x in commands]

print(x)
print(y)

for command in commands:
    match command.split():
        case ["forward", v]:
            x += int(v)
        case ["down", v]:
            y += int(v)
        case ["up", v]:
            y -= int(v)

print(x*y)

