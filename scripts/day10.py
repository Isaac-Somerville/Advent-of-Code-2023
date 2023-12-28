full = open("data/full/day10.txt")
file = full

# test1 = open("data/test/day10_test1.txt")
# file = test1

# test2 = open("data/test/day10_test2.txt")
# file = test2

# test3 = open("data/test/day10_test3.txt")
# file = test3

# test4 = open("data/test/day10_test4.txt")
# file = test4

# test5 = open("data/test/day10_test5.txt")
# file = test5

lines = file.readlines()

def move_step(pos, dirs, dir):
    vec = dirs[dir]
    next_pos = [pos[0] + vec[0], pos[1] + vec[1]]
    return next_pos

def char_from_idxs(grid, pos):
    return grid[pos[0]][pos[1]]

def blow_up_grid(grid, pipe):
    print(grid)
    # print(len(grid[0]))
    # print(len(grid))
    blown_up_grid = [["*" for _ in range(2*len(grid[0]))] for _ in range(2*len(grid))]
    new_pipe = set()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            blown_up_grid[2*i][2*j] = grid[i][j]
            if (i,j) in pipe:
                new_pipe.add((2*i, 2*j))
    return blown_up_grid, new_pipe

def connect_pipe(grid, pipe, i, j):
    if i-1 >= 0 and i+1 < len(grid):
        up, down = [i-1, j], [i+1, j]
        if tuple(up) in pipe and tuple(down) in pipe:
            if (char_from_idxs(grid, up) in {"|", "7", "F", "S"}) and (char_from_idxs(grid, down) in {"|", "J", "L", "S"}):
                grid[i][j] = "|"
                pipe.add((i,j))
    
    if j-1 >= 0 and j+1 < len(grid[i]):
        left, right = [i, j-1], [i, j+1]
        if tuple(left) in pipe and tuple(right) in pipe:
            if (char_from_idxs(grid, left) in {"-", "F", "L", "S"}) and (char_from_idxs(grid, right) in {"-", "7", "J", "S"}):
                grid[i][j] = "-"
                pipe.add((i,j))

    return grid, pipe

def find_enclosed(grid, pipe, enclosed_set, outer_set, i, j):
    dirs = {"u" : [-1,0], "d" : [1,0], "l" : [0,-1], "r" : [0,1]}
    seen = {(i,j)}
    queue = [[i,j]]
    while queue != []:
        next_queue = []
        for pos in queue:
            for dir in dirs:
                next_pos = move_step(pos, dirs, dir)
                if tuple(next_pos) in enclosed_set:
                    enclosed_set.add((i,j))
                    return enclosed_set, outer_set
                if tuple(next_pos) in outer_set:
                    outer_set.add((i,j))
                    return enclosed_set, outer_set
                if tuple(next_pos) not in pipe and tuple(next_pos) not in seen:
                    seen.add(tuple(next_pos))
                    next_queue.append(next_pos)
        queue = next_queue
    enclosed_set.add((i,j))
    return enclosed_set, outer_set




def part1():
    grid = []
    for i in range(len(lines)):
        line = lines[i]
        if line.find("S") != -1:
            start = [i, line.find("S")]
        grid.append(list(line.replace("\n","")))
    # print(start)
    # print(grid)
    dirs = {"u" : [-1,0], "d" : [1,0], "l" : [0,-1], "r" : [0,1]}
    next_dir_dict = {
        "|u" : "u", "|d" : "d",
        "-r" : "r", "-l" : "l",
        "Ld" : "r", "Ll" : "u",
        "Jd" : "l", "Jr" : "u",
        "7u" : "l", "7r" : "d",
        "Fu" : "r", "Fl" : "d"
    }
    dirs_for_chars = {
        "|" : ["u", "d"],
        "-" : ["l", "r"],
        "L" : ["u", "r"],
        "J" : ["u", "l"],
        "7" : ["l", "d"],
        "F" : ["r", "d"]
    }
    seen_positions = set()
    seen_positions.add(tuple(start))
    current_positions = []

    for dir in dirs:
        next_pos = move_step(start, dirs, dir)
        # print(next_pos)
        next_char = char_from_idxs(grid, next_pos)
        if next_char + dir in next_dir_dict:
            current_positions.append(next_pos)
            seen_positions.add(tuple(next_pos))
    distance = 0

    next_positions = current_positions
    while next_positions != current_positions or distance == 0:
        distance += 1
        current_positions = next_positions.copy()
        # print(current_positions)
        # print(seen_positions)
        for i in range(len(current_positions)):
            pos = current_positions[i]
            # print(current_positions)
            char = char_from_idxs(grid, pos)
            # print(current_positions)
            for dir in dirs_for_chars[char]:
                next_pos = move_step(pos, dirs, dir)
                # print(current_positions)
                if tuple(next_pos) not in seen_positions:
                    next_char = char_from_idxs(grid, next_pos)
                    # print(current_positions)
                    if next_char + dir in next_dir_dict:
                        print(distance, next_pos, next_char)
                        next_positions[i] = next_pos
                        # print(current_positions)
                        seen_positions.add(tuple(next_pos))
                        # print(current_positions)
        print(current_positions)
        print(next_positions)
        print("\n")
    print(distance)

def part2():
    grid = []
    for i in range(len(lines)):
        line = lines[i]
        if line.find("S") != -1:
            start = [i, line.find("S")]
        grid.append(list(line.replace("\n","")))
    # print(start)
    # print(grid)
    dirs = {"u" : [-1,0], "d" : [1,0], "l" : [0,-1], "r" : [0,1]}
    next_dir_dict = {
        "|u" : "u", "|d" : "d",
        "-r" : "r", "-l" : "l",
        "Ld" : "r", "Ll" : "u",
        "Jd" : "l", "Jr" : "u",
        "7u" : "l", "7r" : "d",
        "Fu" : "r", "Fl" : "d"
    }
    dirs_for_chars = {
        "|" : ["u", "d"],
        "-" : ["l", "r"],
        "L" : ["u", "r"],
        "J" : ["u", "l"],
        "7" : ["l", "d"],
        "F" : ["r", "d"]
    }
    seen_positions = set()
    seen_positions.add(tuple(start))
    current_positions = []

    for dir in dirs:
        next_pos = move_step(start, dirs, dir)
        # print(next_pos)
        next_char = char_from_idxs(grid, next_pos)
        if next_char + dir in next_dir_dict:
            current_positions.append(next_pos)
            seen_positions.add(tuple(next_pos))
    distance = 0

    next_positions = current_positions
    while next_positions != current_positions or distance == 0:
        distance += 1
        current_positions = next_positions.copy()
        # print(current_positions)
        # print(seen_positions)
        for i in range(len(current_positions)):
            pos = current_positions[i]
            # print(current_positions)
            char = char_from_idxs(grid, pos)
            # print(current_positions)
            for dir in dirs_for_chars[char]:
                next_pos = move_step(pos, dirs, dir)
                # print(current_positions)
                if tuple(next_pos) not in seen_positions:
                    next_char = char_from_idxs(grid, next_pos)
                    # print(current_positions)
                    if next_char + dir in next_dir_dict:
                        print(distance, next_pos, next_char)
                        next_positions[i] = next_pos
                        # print(current_positions)
                        seen_positions.add(tuple(next_pos))
                        # print(current_positions)
        print(current_positions)
        print(next_positions)
        print("\n")

    new_grid, new_pipe = blow_up_grid(grid, seen_positions)
    # for line in new_grid:
    #     print(line)
    for i in range(len(new_grid)):
        for j in range(len(new_grid[i])):
            if new_grid[i][j] == "*":
                new_grid, new_pipe = connect_pipe(new_grid, new_pipe, i, j)
    for line in new_grid:
        print(line)

    enclosed_set = set()
    outer_set = set()
    for i in range(len(new_grid)):
        if (i, 0) not in new_pipe:
            outer_set.add((i,0))
        if (i, len(new_grid[i])-1) not in new_pipe:
            outer_set.add((i, len(new_grid[i])-1))

    for j in range(len(new_grid[0])):
        if (0, j) not in new_pipe:
            outer_set.add((0,j))
        if (len(new_grid)-1, j) not in new_pipe:
            outer_set.add((len(new_grid)-1, j))

    for i in range(len(new_grid)):
        for j in range(len(new_grid[i])):
            if new_grid[i][j] != "*" and (i,j) not in new_pipe:
                enclosed_set, outer_set = find_enclosed(new_grid, new_pipe, enclosed_set, outer_set, i, j)
    print(enclosed_set)
    print(outer_set)
    print(len(enclosed_set))


part2()