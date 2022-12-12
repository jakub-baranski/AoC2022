# https://adventofcode.com/2022/day/11
import math
from collections import deque
from functools import reduce


class Monkey:
    items: deque[int]
    test_div: int
    test_dict: dict[bool, int]

    inspect_count = 0

    def __init__(self, items, operation, test_div: int,  test_dict) -> None:
        self.items = deque()
        self.items.extend(items)
        self.monkey_operation = operation
        self.test_div = test_div
        self.test_dict = test_dict
        super().__init__()

    def operation(self, current_worry: int) -> int:
        self.inspect_count += 1
        return self.monkey_operation(current_worry)

    def test(self, current_worry: int) -> bool:
        return current_worry % self.test_div == 0

    def throw(self, test_result: bool) -> int:
        return self.test_dict[test_result]


def get_monkeys():
    # I'm not parsing that input...
    return [
        Monkey(
            items=[74, 64, 74, 63, 53],
            operation=lambda x: x * 7,
            test_div=5,
            test_dict={True: 1, False: 6}
        ),
        Monkey(
            items=[69, 99, 95, 62],
            operation=lambda x: x * x,
            test_div=17,
            test_dict={True: 2, False: 5}
        ),
        Monkey(
            items=[59, 81],
            operation=lambda x: x + 8,
            test_div=7,
            test_dict={True: 4, False: 3}
        ),
        Monkey(
            items=[50, 67, 63, 57, 63, 83, 97],
            operation=lambda x: x + 4,
            test_div=13,
            test_dict={True: 0, False: 7}
        ),
        Monkey(
            items=[61, 94, 85, 52, 81, 90, 94, 70],
            operation=lambda x: x + 3,
            test_div=19,
            test_dict={True: 7, False: 3}
        ),
        Monkey(
            items=[69],
            operation=lambda x: x + 5,
            test_div=3,
            test_dict={True: 4, False: 2}
        ),
        Monkey(
            items=[54, 55, 58],
            operation=lambda x: x + 7,
            test_div=11,
            test_dict={True: 1, False: 5}
        ),
        Monkey(
            items=[79, 51, 83, 88, 93, 76],
            operation=lambda x: x * 3,
            test_div=2,
            test_dict={True: 0, False: 6}
        ),

    ]


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def part_two():
    monkeys = get_monkeys()

    for i in range(10000):

        dividers = list(map(lambda x: x.test_div, monkeys))

        m = reduce(lambda x, y: lcm(x, y), dividers)

        for monkey in monkeys:

            while 1:
                try:
                    item = monkey.items.popleft()
                except IndexError:
                    break
                worry = monkey.operation(item)
                # Modulo LCM of the largest common multiple of divisors of all monkeys
                worry = math.floor(worry % m)
                test = monkey.test(worry)
                throw_to_monkey = monkey.throw(test)
                monkeys[throw_to_monkey].items.append(worry)

    inspects = list(map(lambda x: x.inspect_count, monkeys))
    most_active = sorted(inspects)[-2:]
    print(most_active[0] * most_active[1])


part_two()
