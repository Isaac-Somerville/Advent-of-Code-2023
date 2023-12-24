full = open("data/full/day9.txt")
file = full

# test = open("data/test/day9_test.txt")
# file = test

lines = file.readlines()

def find_differences(lst):
    diff_lst = [0 for _ in range(len(lst)-1)]
    for i in range(len(lst)-1):
        diff_lst[i] = lst[i+1] - lst[i]
    return diff_lst

def are_all_zeros(lst):
    return all(x == 0 for x in lst)

def part_1():
    history_lists = []
    for line in lines:
        history = list(map(int,line.split()))
        # print(history)
        history_lists.append(history)
    all_values = 0
    for history in history_lists:
        diff_tower = [history]
        current = history
        while are_all_zeros(current) == False:
            diff_lst = find_differences(current)
            diff_tower.append(diff_lst)
            current = diff_lst
        addition = 0
        for i in range(len(diff_tower)-1,-1,-1):
            diff_tower[i].append(diff_tower[i][-1] + addition)
            addition = diff_tower[i][-1]
        next_value = diff_tower[0][-1]
        all_values += next_value
    print(all_values)

def part_2():
    history_lists = []
    for line in lines:
        history = list(map(int,line.split()))
        # print(history)
        history_lists.append(history)
    all_values = 0
    for history in history_lists:
        diff_tower = [history]
        current = history
        while are_all_zeros(current) == False:
            diff_lst = find_differences(current)
            diff_tower.append(diff_lst)
            current = diff_lst
        addition = 0
        for i in range(len(diff_tower)-1,-1,-1):
            diff_tower[i] = [diff_tower[i][0] - addition] + diff_tower[i]
            addition = diff_tower[i][0]
        next_value = diff_tower[0][0]
        all_values += next_value
    print(all_values)
                


# part_1()
part_2()