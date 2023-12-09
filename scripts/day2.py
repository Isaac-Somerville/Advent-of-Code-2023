def remove_before(string, substring):
    return string[string.find(substring)+len(substring) : ]

if __name__ == "__main__":
    file = open("input/day2.txt")
    lines = file.readlines()

    ### PART 1 ###
    # valid_ids_sum = 0
    # max_dict = {"red" : 12, "green" : 13, "blue" : 14}
    # i = 1
    # for line in lines:
    #     valid = True
    #     print(line)
    #     line = remove_before(line, ": ")
    #     print(line)
    #     rounds = line.split("; ")
    #     print(rounds)
    #     for round in rounds:
    #         occur_dict = {"red" : 0, "green" : 0, "blue" : 0}
    #         indiv_count = round.split(", ")
    #         print(indiv_count)
    #         for pair in indiv_count:
    #             freq, colour = pair.split()
    #             occur_dict[colour] = int(freq)
    #         print(occur_dict)
    #         for colour in occur_dict:
    #             if occur_dict[colour] > max_dict[colour]:
    #                 print("invalid")
    #                 valid = False
    #                 break
    #         if valid == False:
    #             break
    #     if valid == True:
    #         print("valid")
    #         valid_ids_sum += i
    #     print(" ")
    #     i += 1
    # print(valid_ids_sum)

    ### PART 2 ###
    sum_of_powers = 0
    for line in lines:
        power = 1
        min_dict = {"red" : 0, "green" : 0, "blue" : 0}
        line = remove_before(line, ": ")
        rounds = line.split("; ")
        for round in rounds:
            indiv_count = round.split(", ")
            for pair in indiv_count:
                freq, colour = pair.split()
                min_dict[colour] = max(int(freq), min_dict[colour])
        for colour in min_dict:
            power *= min_dict[colour]
        sum_of_powers += power
    print(sum_of_powers)
