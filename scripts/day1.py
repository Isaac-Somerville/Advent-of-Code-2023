file = open("input/day1.txt")

########## PART 1 ###########

# total = 0
# for line in file.readlines():
#     # print(line)
#     first_num, last_num = None, None
#     i = 0
#     n = len(line)
#     while first_num == None or last_num == None:
#         if first_num == None and line[i].isnumeric():
#             first_num = line[i]
#             print(first_num)
#         if last_num == None and line[n-i-1].isnumeric():
#             last_num = line[n-i-1]
#             print(last_num)
#         i += 1
#     calib_value = int(first_num + last_num)
#     print(calib_value)
#     total += calib_value

# print("total: ", total)

########## PART 2 ###########

num_dict = {
    "one": "1", 
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5", 
    "six": "6", 
    "seven": "7", 
    "eight": "8", 
    "nine": "9"
}

total = 0
for line in file.readlines():
    # print(line)
    first_num, last_num = None, None
    i = 0
    n = len(line)
    while first_num == None or last_num == None:
        if first_num == None:
            if line[i].isnumeric():
                first_num = line[i]
            else:
                for j in range(3,6):
                    if i+j < n and line[i:i+j] in num_dict:
                        first_num = num_dict[line[i:i+j]]
        if last_num == None:
            if line[n-i-1].isnumeric():
                last_num = line[n-i-1]
            else:
                for j in range(3,6):
                    if n-i-j >= 0 and line[n-i-j:n-i] in num_dict:
                        last_num = num_dict[line[n-i-j:n-i]]
        i += 1
    calib_value = int(first_num + last_num)
    # print(first_num, last_num, calib_value)
    total += calib_value

print("total: ", total)