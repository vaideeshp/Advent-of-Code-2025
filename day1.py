# AOC 2025 day 1

with open("data.txt") as file:
    datapoints = file.read().splitlines()

def part1(datapoints, initial_position=50):
    current_position = initial_position
    number_of_zero = 0

    for datapoint in datapoints:
        direction, distance = datapoint[0], int(datapoint[1:])
        
        if direction == "L":
            current_position = (current_position - distance) % 100
        else:
            current_position = (current_position + distance) % 100

        number_of_zero += (current_position == 0)

    return number_of_zero

def part2(datapoints, initial_position=50):
    current_position = initial_position
    number_of_zero = 0

    for datapoint in datapoints:
        direction, distance = datapoint[0], int(datapoint[1:])

        if direction == "L":
            number_of_zero += abs((current_position - distance) // 100) # number of full rotations
            current_position = (current_position - distance) % 100
            #number_of_zero += (current_position == 0)
        else:
            number_of_zero += abs((current_position + distance) // 100) # number of full rotations
            current_position = (current_position + distance) % 100

        number_of_zero += (current_position == 0)

    return number_of_zero

print(part2(datapoints))





