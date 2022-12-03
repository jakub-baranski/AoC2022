# https://adventofcode.com/2022/day/3
from textwrap import wrap

test = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

inp_list = test.split("\n")


def get_priority(char: str):
    return ord(char) - (96 if char.islower() else 38)


def part_one():
    res = 0
    for inp in inp_list:
        first, second = wrap(inp, len(inp) // 2)
        if intersection := set(first) & set(second):
            res += get_priority(intersection.pop())
    print(res)


def part_two():
    res = 0
    groups = zip(inp_list, inp_list[1:], inp_list[2:])
    for a, b, c in list(groups)[::3]:
        intersection = set(a) & set(b) & set(c)
        res += get_priority(intersection.pop())
    print(res)


part_one()
part_two()
