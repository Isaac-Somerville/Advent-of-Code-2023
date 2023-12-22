full = open("data/full/day5.txt")
file = full

# test = open("data/test/day5_test.txt")
# file = test

lines = file.readlines()

def find_intersection(int_1, int_2):
    """
    Returns intersection of two ranges [a,b] and [c,d]
    """
    a, b = int_1
    c, d = int_2
    left, right = max(a,c), min(b,d)
    if right < left:
        return None
    else:
        return [left, right]
    
def remove_subinterval(interval, subint):
    """
    Returns interval(s) produced from removing subint [c,d] from interval [a,b]
    """
    a,b = interval
    intersection = find_intersection(interval,subint) 
    if intersection == None:
        return interval
    e,f = intersection
    if e > a:
        if f < b:
            return [[a,e-1],[f+1,b]]
        elif f == b:
            return [[a,e-1]]
    elif e == a:
        if f < b:
            return [[f,b]]
        elif f == b:
            return None
        

if __name__ == '__main__':
    dict_dict = {} # dictionary name : dictionary
    source_dest_dict = {} # current dict : next dict (e.g, 'seed-to-soil' : 'soil-to-fertilizer')
    range_dict_dict = {} # dictionary name : ranges seen
    prev_dict = None
    current_dict = None

    for line in lines:
        # create dictionary of dictionary mappings
        if not line[0].isnumeric() and line != '\n':
            line = line.replace(":", "")
            line = line.split()
            if line[0] == 'seeds':
                target_seeds = list(map(int,line[1:]))
                # print(target_seeds)
            else:
                if current_dict != None:
                    prev_dict = current_dict
                current_dict = line[0]
                dict_dict[current_dict] = {}
                range_dict_dict[current_dict] = {}
                if prev_dict != None:
                    source_dest_dict[prev_dict] = current_dict
                # print(source_dest_dict)
        elif line[0].isnumeric():
            # fill current dictionary
            line = line.split()
            # print(list(map(int,line)))
            dest, source, num_range = list(map(int,line))
            # print(dest, source, num_range)
            dict_dict[current_dict][source] = [dest, num_range]
            range_dict_dict[current_dict][(source, source + num_range - 1)] = [dest, dest + num_range - 1]
            # print(dict_dict[current_dict])
            # print(range_dict_dict[current_dict])
        # print(line[0])
    source_dest_dict[current_dict] = None
    for dict in dict_dict:
        print(dict, dict_dict[dict])
        print(dict, range_dict_dict[dict])
        print("\n")
    
    min_location = None
    for seed in target_seeds:
        current_dict = 'seed-to-soil'
        current_var = seed
        while current_dict in source_dest_dict:
            next_dict = source_dest_dict[current_dict]
            for var in dict_dict[current_dict]:
                if var <= current_var < var + dict_dict[current_dict][var][1]:
                    current_var = dict_dict[current_dict][var][0] + current_var - var
                    break
            # print(current_dict, current_var)
            current_dict = next_dict
        if min_location == None:
            min_location = current_var
        else:
            min_location = min(current_var, min_location)
    #     print("Location: ", current_var)
    #     print("\n")
    print("Minimum location: ", min_location)

    # print(find_intersection(1,4,2,3))

    i = 0
    min_location = None
    while i < len(target_seeds):
        # seen_range_dict = {}
        range_start = target_seeds[i]
        range_end = target_seeds[i] + target_seeds[i+1] - 1
        current_dict = 'seed-to-soil'
        # seen_range_dict[current_dict] = [[range_start, range_end]]
        queue = [[range_start, range_end]]
        while current_dict in source_dest_dict:
            # print(current_dict)
            # print(queue)
            # print("\n")
            next_dict = source_dest_dict[current_dict]
            next_queue = []
            # seen_range_dict[next_dict] = []
            for current_range in queue:
                for source_range in range_dict_dict[current_dict]:
                    # print(current_range)
                    # print(source_range)
                    source_range_intersect = find_intersection(current_range, source_range)
                    # print(source_range_intersect)
                    if source_range_intersect != None:
                        diff = source_range_intersect[0] - source_range[0]
                        width = source_range_intersect[1] - source_range_intersect[0]
                        # print(diff)
                        dest_range = range_dict_dict[current_dict][source_range]
                        # print(dest_range)
                        dest_range_intersect = [dest_range[0] + diff, dest_range[0] + diff + width]
                        # print(dest_range_intersect)
                        next_queue.append(dest_range_intersect)
                        leftover = remove_subinterval(current_range, source_range_intersect)
                        if leftover == None:
                            current_range = None
                            break
                        current_range = leftover[0]
                        if len(leftover) == 2:
                            queue.append(leftover[1])
                    # print("\n")
                if current_range != None:
                    next_queue.append(current_range)
            queue = next_queue
            current_dict = next_dict
        # print(queue)
        current_min = min([current_range[0] for current_range in queue])
        print("Current Minimum Location: ", current_min)   
        min_location = current_min if min_location == None else min(current_min, min_location)
        print("Running Minimum Location: ", min_location)
        print("\n")
        i += 2



    # print(dict_dict)