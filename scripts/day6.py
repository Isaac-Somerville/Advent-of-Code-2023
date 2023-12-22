from math import floor, ceil

full = open("data/full/day6.txt")
file = full

# test = open("data/test/day6_test.txt")
# file = test

lines = file.readlines()

def find_distance(total_time, charge_time):
    speed = charge_time
    distance = (total_time - charge_time) * speed
    return distance

def solve_quadratic(total_time, record_distance):
    """
    Solves (total_time - t) * t = record_distance <=> t^2 - total_time * t + record_distance = 0
    i.e. returns (total_time +- sqrt(total_time**2 - 4*1*record_distance)) / 2 
    """
    return ((total_time - (total_time**2 - 4*1*record_distance)**(1/2)) / 2, (total_time + (total_time**2 - 4*1*record_distance)**(1/2)) / 2)

if __name__ == "__main__":
    # times = list(map(int,lines[0].split()[1:]))
    # distances = list(map(int,lines[1].split()[1:]))
    # # print(times)
    # # print(distances)
    # total_prod = 1
    # for i in range(len(times)):
    #     lower_lim, upper_lim = solve_quadratic(times[i], distances[i])
    #     if ceil(lower_lim) - lower_lim == 0:
    #         lower_lim = ceil(lower_lim) + 1
    #     else:
    #         lower_lim = ceil(lower_lim)
    #     if floor(upper_lim) - upper_lim == 0:
    #         upper_lim = floor(upper_lim) - 1
    #     else:
    #         upper_lim = floor(upper_lim)
    #     total_prod *= upper_lim - lower_lim + 1
    # print(total_prod)

    time = int(''.join(lines[0].split()[1:]))
    distance = int(''.join(lines[1].split()[1:]))
    # print(times)
    # print(distances)
    total_prod = 1
    lower_lim, upper_lim = solve_quadratic(time, distance)
    if ceil(lower_lim) - lower_lim == 0:
        lower_lim = ceil(lower_lim) + 1
    else:
        lower_lim = ceil(lower_lim)
    if floor(upper_lim) - upper_lim == 0:
        upper_lim = floor(upper_lim) - 1
    else:
        upper_lim = floor(upper_lim)
    total_prod *= upper_lim - lower_lim + 1
    print(total_prod)
