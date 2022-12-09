# https://adventofcode.com/2022/day/9

import math

test_part_one = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".split('\n')

test_part_two = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20""".split('\n')


def get_head_position(position: list[int], direction: str):
    if direction == "R":
        index, modifier = 0, 1
    elif direction == "L":
        index, modifier = 0, -1
    elif direction == "U":
        index, modifier = 1, 1
    else:
        index, modifier = 1, -1
    position[index] += 1 * modifier
    return position


def get_new_position(last_knot, knot):
    diff = math.dist(last_knot, knot)
    possible_moves = []
    if diff == 2:
        possible_moves = [0, 1], [0, -1], [1, 0], [-1, 0]
    elif diff > math.sqrt(2):
        possible_moves = [[1, 1], [-1, -1], [1, -1], [-1, 1]]
    for m in possible_moves:
        after_move = knot[0] + m[0], knot[1] + m[1]
        if math.dist(last_knot, after_move) == 1 or math.dist(last_knot, after_move) == math.sqrt(2):
            return after_move
    return knot


def solution(inp: list[str], knots: int):
    visited = set()
    knots_positions = [[0, 0] for _ in range(knots)]
    for i in inp:
        direction, dist = i.split(' ')
        dist = int(dist)
        for _ in range(dist):
            for k_index in range(len(knots_positions)):
                if k_index == 0:
                    knots_positions[0] = get_head_position(knots_positions[0], direction)
                else:
                    last_knot = knots_positions[k_index - 1]
                    knots_positions[k_index] = get_new_position(last_knot, knots_positions[k_index])
                    if k_index == len(knots_positions) - 1:
                        visited.add('_'.join([str(k) for k in knots_positions[k_index]]))
    print(len(visited))


solution(test_part_one, 2)  # PART ONE
solution(test_part_two, 10)  # PART TWO
