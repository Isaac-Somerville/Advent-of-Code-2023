full = open("data/full/day8.txt")
file = full

# test = open("data/test/day8_test.txt")
# file = test

lines = file.readlines()

def loop_found(current_node, seen_nodes, num_steps, len_instructions):
    for i in range(len(seen_nodes[current_node])):
        seen_steps = seen_nodes[current_node][i]
        if seen_steps % len_instructions == num_steps % len_instructions:
            print("Loop found:", current_node, num_steps, seen_steps)
            return seen_steps
    return -1

def lcm(a,b):
    return a / gcd(a,b) * b

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

if __name__ == "__main__":

    ### PART 1 ###
    # instructions = []
    # for char in lines[0]:
    #     if char == "L":
    #         instructions.append(0)
    #     elif char == "R":
    #         instructions.append(1)
    # print(instructions)
    
    # graph_dict = {}
    # for i in range(2, len(lines)):
    #     # print(lines[i])
    #     parent, left, right = lines[i].replace("= (", "").replace(")", "").replace(",", "").replace("\n", "").split(" ")
    #     graph_dict[parent] = [left, right]
    
    # num_steps = 0
    # current_node = 'AAA'
    # len_instructions = len(instructions)
    # while current_node != 'ZZZ':
    #     direction = instructions[num_steps % len_instructions]
    #     current_node = graph_dict[current_node][direction]
    #     num_steps += 1
    # print("steps: ", num_steps)

    ### PART 2 ###
    instructions = []
    for char in lines[0]:
        if char == "L":
            instructions.append(0)
        elif char == "R":
            instructions.append(1)
    print(instructions)
    
    graph_dict = {}
    starting_nodes = []
    end_nodes = set()
    for i in range(2, len(lines)):
        # print(lines[i])
        parent, left, right = lines[i].replace("= (", "").replace(")", "").replace(",", "").replace("\n", "").split(" ")
        if parent[-1] == "A":
            starting_nodes.append(parent)
        if parent[-1] == "Z":
            end_nodes.add(parent)
        graph_dict[parent] = [left, right]
    
    print(starting_nodes)
    print(end_nodes)
    len_instructions = len(instructions)
    # num_at_end_nodes = 0
    # while num_at_end_nodes != len(starting_nodes):
    #     num_at_end_nodes = 0
    #     direction = instructions[num_steps % len_instructions]
    #     for i in range(len(starting_nodes)):
    #         current_node = starting_nodes[i]
    #         next_node = graph_dict[current_node][direction]
    #         if next_node in end_nodes:
    #             num_at_end_nodes += 1
    #         starting_nodes[i] = next_node
    #     num_steps += 1
    # print("steps: ", num_steps)

    steps_to_end_nodes_dict = dict(zip(starting_nodes, [[] for _ in range(len(starting_nodes))]))
    loop_lengths = dict(zip(starting_nodes, [0 for _ in range(len(starting_nodes))]))
    print(steps_to_end_nodes_dict)
    for start in starting_nodes:
        current_node = start
        seen_nodes = {} # node : num_steps to node
        num_steps = 0
        while current_node not in seen_nodes or loop_found(current_node, seen_nodes, num_steps, len_instructions) == -1:
            if current_node in end_nodes:
                print("end node: ", current_node, num_steps)
                steps_to_end_nodes_dict[start].append(num_steps)
            if current_node in seen_nodes:
                seen_nodes[current_node].append(num_steps)
            else:
                seen_nodes[current_node] = [num_steps]
            direction = instructions[num_steps % len_instructions]
            # take step
            current_node = graph_dict[current_node][direction]
            num_steps += 1
        loop_start = current_node
        loop_length = num_steps - loop_found(current_node, seen_nodes, num_steps, len_instructions)
        loop_lengths[start] = loop_length
        print("start node:", start)
        # print(seen_nodes)
        print("loop start: ", loop_start)
        print("loop length: ", loop_length)
        print(steps_to_end_nodes_dict)
        print("\n")
    print(loop_lengths)

    lowest_mult = 1
    for start in starting_nodes:
        lowest_mult = lcm(lowest_mult, loop_lengths[start])
        print(lowest_mult)