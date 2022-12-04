# https://adventofcode.com/2022/day/4
test = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

inp_list = test.split("\n")


def part_one():
    counter = 0
    for inp in inp_list:
        first, second = [list(map(int, x.split('-'))) for x in inp.split(',')]
        first_range, second_range = [range(x[0], x[1] + 1) for x in [first, second]]
        if (first[0] in second_range and first[1] in second_range) or (second[0] in first_range and second[1] in first_range):
            counter += 1.
    print(counter)


def part_two():
    counter = 0
    for inp in inp_list:
        first, second = [list(map(int, x.split('-'))) for x in inp.split(',')]
        first_range, second_range = [range(x[0], x[1] + 1) for x in [first, second]]
        if first[0] in second_range or first[1] in second_range or second[0] in first_range or second[1] in first_range:
            counter += 1
    print(counter)
