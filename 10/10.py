# https://adventofcode.com/2022/day/10
test = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

inp_list = test.split('\n')

global cycles
global x
global signal


def part_one():
    global cycles
    global x
    global signal

    check_cycles = [20, 60, 100, 140, 180, 220]

    signal = 0
    cycles = 0
    x = 1

    def increment_cycle():
        global cycles
        global signal
        cycles += 1
        if cycles in check_cycles:
            signal += cycles * x

    for line in inp_list:
        if ' ' in line:
            increment_cycle()
            increment_cycle()
            x += int(line.split(' ')[1])
        else:
            increment_cycle()
    print(signal)


def part_two():

    global cycles
    global x
    global signal

    signal = 0
    cycles = 0
    x = 1

    def increment_cycle():
        global cycles
        global signal
        cycles += 1
        column = cycles % 40 - 1
        drawn_pixel = column
        sprite_middle_column = x % 40
        sprite_columns = [sprite_middle_column, sprite_middle_column - 1, sprite_middle_column + 1]
        if drawn_pixel == 0:
            print('\n', end='')
        print('#' if drawn_pixel in sprite_columns else '.', end='')

    for line in inp_list:
        if ' ' in line:
            for _ in range(2):
                increment_cycle()
            x += int(line.split(' ')[1])
        else:
            increment_cycle()


part_one()
part_two()
