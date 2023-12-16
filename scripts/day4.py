file = open("data/full/day4.txt")
# file = open("data/test/day4_test.txt")
lines = file.readlines()

def remove_before(string, substring):
    return string[string.find(substring)+len(substring) : ]

if __name__ == '__main__':
    # total_points = 0
    # for line in lines:
    #     matches = -1
    #     line = remove_before(line, ":")
    #     winning_nums, ticket_nums = line.split("|")
    #     winning_nums = set(winning_nums.split())
    #     # print(winning_nums)
    #     ticket_nums = ticket_nums.split()
    #     # print(ticket_nums)
    #     already_won = set()
    #     for num in ticket_nums:
    #         if num in winning_nums and num not in already_won:
    #             matches += 1
    #             already_won.add(num)
    #     if matches != -1:
    #         total_points += 2**matches
    # # print(total_points)

    score_dict = {} # num_card : num_wins_on_card
    instance_dict = {} # num_card : total_instances
    i = 0
    for line in lines:
        instance_dict[i] = 1
        matches = 0
        line = remove_before(line, ":")
        winning_nums, ticket_nums = line.split("|")
        winning_nums = set(winning_nums.split())
        # print(winning_nums)
        ticket_nums = ticket_nums.split()
        # print(ticket_nums)
        already_won = set()
        for num in ticket_nums:
            if num in winning_nums and num not in already_won:
                matches += 1
                already_won.add(num)
        score_dict[i] = matches
        i += 1
    for card in instance_dict:
        for i in range(card + 1, card + score_dict[card] + 1):
            instance_dict[i] += instance_dict[card]
        print(card, instance_dict)
    total_score = 0
    for card in instance_dict:
        total_score += instance_dict[card]
    print(score_dict)
    print(instance_dict)
    print(total_score)
    # print(total_points)