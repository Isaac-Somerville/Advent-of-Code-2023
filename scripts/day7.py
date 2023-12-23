full = open("data/full/day7.txt")
file = full

# test = open("data/test/day7_test.txt")
# file = test

lines = file.readlines()

def determine_type(hand):
    card_dict = {} # card : num of card
    max_occur = 1
    for card in hand:
        if card in card_dict:
            card_dict[card] += 1
            max_occur = max(max_occur, card_dict[card])
        else:
            card_dict[card] = 1
    if max_occur == 5:
        return "five-kind"
    if max_occur == 4:
        return "four-kind"
    if max_occur == 3:
        if len(card_dict) == 2:
            return "full-house"
        else:
            return "three-kind"
    if max_occur == 2:
        if len(card_dict) == 3:
            return "two-pair"
        else:
            return "one-pair"
    return "high-card"

def compare_hands_of_same_type(hand1,hand2):
    for i in range(len(hand1)):
        card1, card2 = hand1[i], hand2[i]
        strength1 = strength_dict[card1]
        strength2 = strength_dict[card2]
        if strength1 != strength2:
            if strength1 < strength2:
                return hand2
            else:
                return hand1
    return hand1

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[left + i]
 
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
 
    # Merge the temp arrays back into arr[left..right]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = left     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if compare_hands_of_same_type(hand_list[L[i]],hand_list[R[j]]) == hand_list[R[j]]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# left is for left index and right is right index of the
# sub-array of arr to be sorted
 
 
def mergeSort(arr, left, right):
    if left < right:
 
        # Same as (left+right)//2, but avoids overflow for
        # large left and h
        mid = left+(right-left)//2
 
        # Sort first and second halves
        mergeSort(arr, left, mid)
        mergeSort(arr, mid+1, right)
        merge(arr, left, mid, right)

def determine_type_jokers(hand):
    card_dict = {} # card : num of card
    max_occur = 0
    max_card = None
    num_jokers = 0
    for card in hand:
        if card == 'J':
            num_jokers += 1
        else:
            if card in card_dict:
                card_dict[card] += 1
                if card_dict[card] > max_occur:
                    max_occur = card_dict[card]
                    max_card = card
            else:
                card_dict[card] = 1
                if max_occur == 0:
                    max_occur = 1
                    max_card = card
    if num_jokers > 0 :
        if max_card == None:
            return "five-kind"
        else:
            max_occur += num_jokers
            card_dict[max_card] += num_jokers
    if max_occur == 5:
        return "five-kind"
    if max_occur == 4:
        return "four-kind"
    if max_occur == 3:
        if len(card_dict) == 2:
            return "full-house"
        else:
            return "three-kind"
    if max_occur == 2:
        if len(card_dict) == 3:
            return "two-pair"
        else:
            return "one-pair"
    return "high-card"

if __name__ == "__main__":
    
    ### PART 1 ###
    # cards = [str(i) for i in range(2,10)] + ['T', 'J', 'Q', 'K', 'A']
    # strengths = [i for i in range(2,15)]
    # strength_dict = dict(zip(cards,strengths))
    # type_list = ["five-kind", "four-kind", "full-house", "three-kind",
    #              "two-pair", "one-pair", "high-card"]
    # # print(strength_dict)
    # hand_list = []
    # bid_list = []
    # type_dict = {} # type of hand : list of indices whose hand is this type
    # for i in range(len(lines)):
    #     hand, bid = lines[i].split()
    #     bid_list.append(int(bid))
    #     hand_list.append(list(hand))
    # # print(hand_list)
    # # print(bid_list)
    # for i in range(len(hand_list)):
    #     # print(hand)
    #     type = determine_type(hand_list[i])
    #     if type in type_dict:
    #         type_dict[type].append(i)
    #     else:
    #         type_dict[type] = [i]
    # for type in type_dict:
    #     # print(type)
    #     mergeSort(type_dict[type], 0, len(type_dict[type])-1)
    #     # for id in type_dict[type]:
    #     #     print(hand_list[id])
    # id_ranking = []
    # type_list.reverse()
    # for type in type_list:
    #     if type in type_dict:
    #         id_ranking += type_dict[type]
    # # print(id_ranking)
    # total_winnings = 0
    # for i in range(len(id_ranking)):
    #     id = id_ranking[i]
    #     total_winnings += (i+1) * bid_list[id]
    # print(total_winnings)
    # for type in type_dict:
    #     print(type)
    #     print(type_dict[type])
    #     print("\n")
    #     for i in range(len(type_dict[type]) - 1):
    #         print(compare_hands_of_same_type(hand_list[type_dict[type][i]], hand_list[type_dict[type][i+1]]))

    ### PART 2 ###
    cards = [str(i) for i in range(2,10)] + ['T', 'J', 'Q', 'K', 'A']
    strengths = [i for i in range(2,15)]
    strength_dict = dict(zip(cards,strengths))
    strength_dict['J'] = 1
    print(strength_dict)
    type_list = ["five-kind", "four-kind", "full-house", "three-kind",
                 "two-pair", "one-pair", "high-card"]
    # print(strength_dict)
    hand_list = []
    bid_list = []
    type_dict = {} # type of hand : list of indices whose hand is this type
    for i in range(len(lines)):
        hand, bid = lines[i].split()
        bid_list.append(int(bid))
        hand_list.append(list(hand))
    # print(hand_list)
    # print(bid_list)
    for i in range(len(hand_list)):
        # print(hand)
        type = determine_type_jokers(hand_list[i])
        if type in type_dict:
            type_dict[type].append(i)
        else:
            type_dict[type] = [i]
    for type in type_dict:
        print(type)
        mergeSort(type_dict[type], 0, len(type_dict[type])-1)
        for id in type_dict[type]:
            print(hand_list[id])
        print("\n")
    id_ranking = []
    type_list.reverse()
    for type in type_list:
        if type in type_dict:
            id_ranking += type_dict[type]
    # print(id_ranking)
    total_winnings = 0
    for i in range(len(id_ranking)):
        id = id_ranking[i]
        total_winnings += (i+1) * bid_list[id]
    print(total_winnings)
    # for type in type_dict:
    #     print(type)
    #     print(type_dict[type])
    #     print("\n")
    #     for i in range(len(type_dict[type]) - 1):
    #         print(compare_hands_of_same_type(hand_list[type_dict[type][i]], hand_list[type_dict[type][i+1]]))
    

