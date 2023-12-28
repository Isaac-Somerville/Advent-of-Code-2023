test = open("data/test/day11_test.txt")
file = test

full = open("data/full/day11.txt")
file = full

lines = file.readlines()

def are_all_empty(lst):
    return all(x != "#" for x in lst)

def find_distance(galaxy1, galaxy2, empty_rows, empty_cols, part):
    a, c = min(galaxy1[0], galaxy2[0]), max(galaxy1[0], galaxy2[0])
    b, d = min(galaxy1[1], galaxy2[1]), max(galaxy1[1], galaxy2[1])
    double_rows = [x for x in empty_rows if x > a and x < c]
    double_cols = [x for x in empty_cols if x > b and x < d]
    if part == 1:
        mult = 1
    else: # part == 2
        mult = 1000000 - 1
    row_dist = c - a + mult * len(double_rows)
    col_dist = d - b + mult * len(double_cols)
    return row_dist + col_dist

def main(part):
    grid = []
    empty_rows = []
    empty_cols = []
    galaxies = []
    for i in range(len(lines)):
        # add rows, check empty rows
        line = list(lines[i].replace("\n",""))
        if are_all_empty(line):
            grid.append(["+" for _ in range(len(line))])
            empty_rows.append(i)
        else:
            grid.append(line)
    # for line in grid:
    #     print(line)
    for j in range(len(grid[0])):
        # check empty cols
        col = [line[j] for line in grid]
        if are_all_empty(col):
            empty_cols.append(j)
            for i in range(len(grid)):
                grid[i][j] = "+"
    # print("\n")
    # for line in grid:
    #     print(line)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "#":
                galaxies.append((i,j))
    distances = [[0 for _ in range(len(galaxies))] for _ in range(len(galaxies))]
    for i in range(len(galaxies) - 1):
        for j in range(i+1, len(galaxies)):
            distances[i][j] = find_distance(galaxies[i], galaxies[j], empty_rows, empty_cols, part)
    # print(empty_rows)
    # print(empty_cols)
    # print(galaxies)
    # for line in distances:
    #     print(line)
    total_sum = 0
    for line in distances:
        total_sum += sum(line)
    print(total_sum)
    
# part = 1
part = 2
main(part)