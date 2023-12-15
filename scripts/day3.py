from numpy import prod

file = open("data/full/day3.txt")
# file = open("data/test/day3_test.txt")
lines = file.readlines()

def check_part_number(mat, i, j):
    i_steps = [-1, 0, 1]
    j_steps = [-1, 0, 1]
    is_part_number = False
    num_string = ''
    while j < len(mat[i]) and mat[i][j].isnumeric():
        for i_step in i_steps:
            for j_step in j_steps:
                if 0 <= i+i_step < len(mat) and 0 <= j+j_step < len(mat[i]):
                    if not mat[i+i_step][j+j_step].isnumeric() and mat[i+i_step][j+j_step] != ".":
                        is_part_number = True
        num_string += mat[i][j]
        j += 1
    # print(num_string)
    return is_part_number, int(num_string), j

def count_adj_nums(mat, i, j):
    i_steps = [-1, 0, 1]
    j_steps = [-1, 0, 1]
    num_list = []
    in_num = False
    for i_step in i_steps:
        for j_step in j_steps:
            if 0 <= i+i_step < len(mat) and 0 <= j+j_step < len(mat[i]):
                if mat[i+i_step][j+j_step].isnumeric() and in_num == False:
                    in_num = True
                    num = calc_num(mat, i+i_step, j+j_step)
                    num_list.append(num)
                elif not mat[i+i_step][j+j_step].isnumeric() and in_num == True:
                    in_num = False
        in_num = False
    gear_ratio = prod(num_list)
    num_count = len(num_list)
    # print(num_list)
    return num_count, gear_ratio

def calc_num(mat, i, j):
    # print(mat[i][j])
    # print(i,j)
    l_step, r_step = -1, 1
    while j+l_step >= 0 and mat[i][j+l_step].isnumeric():
        l_step -= 1
    while j+r_step < len(mat[i]) and mat[i][j+r_step].isnumeric():
        r_step += 1
    # print(j+l_step, j+r_step)
    # print(mat[i][j+l_step+1 : j+r_step])
    return int(''.join(mat[i][j+l_step+1 : j+r_step]))


                
                
if __name__ == "__main__":
    mat = []
    for line in lines:
        line = list(line.replace('\n', ''))
        mat.append(line)

    # total_part_nums, i, j = 0, 0, 0
    # while i < len(mat):
    #     while j < len(mat[i]):
    #         if mat[i][j].isnumeric():
    #             is_part_number, num, j = check_part_number(mat,i,j)
    #             print(is_part_number, num, j)
    #             if is_part_number:
    #                 total_part_nums += num
    #         else:
    #             j += 1
    #     i += 1
    #     j = 0
    # print(total_part_nums)

    total_part_nums = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == '*':
               adj_nums, gear_ratio = count_adj_nums(mat, i, j)
               if adj_nums == 2:
                #    print("gear ratio", gear_ratio)
                   total_part_nums += gear_ratio
    print("Total Part Numbers: ", total_part_nums)