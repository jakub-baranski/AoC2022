# https://adventofcode.com/2022/day/7

from collections import defaultdict

test = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

lines = test.split('\n')


def part_one_and_two():
    directories = defaultdict(int)
    cwd = []

    for line in lines:
        if line[0] == "$":
            if line[2:4] == 'cd':
                dest = line[5:]
                if dest == '..':
                    cwd.pop()
                elif dest == '/':
                    cwd = []
                else:
                    cwd.append('__'.join(cwd) + ("__" if cwd else "") + dest)
        else:
            size_or_type, name = line.split(' ')
            if size_or_type != 'dir':
                for path in cwd:
                    directories[path] += int(size_or_type)
                directories['/'] += int(size_or_type)

    # Part one answer
    print(sum(value for value in directories.values() if value < 100000))

    needed_space = 30000000 - (70000000 - directories['/'])

    # PART TWO
    pairs = [(k, v) for k, v in directories.items()]
    sorted_pairs = sorted(pairs, key=lambda x: x[1])
    # Part two answer
    print(next(pair for pair in sorted_pairs if pair[1] >= needed_space)[1])

