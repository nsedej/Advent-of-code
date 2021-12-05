def first(data):
    horizontal, depth = 0,0
    with open(data, 'r') as d:
        for line in d:
            line = line.split()
            if line[0] == 'forward':
                horizontal += int(line[1])
            elif line[0] == 'down':
                depth += int(line[1])
            elif line[0] == 'up':
                depth -= int(line[1])
    return horizontal*depth

def second(data):
    horizontal, depth, aim = 0,0,0
    with open(data, 'r') as d:
        for line in d:
            line = line.split()
            if line[0] == 'forward':
                horizontal += int(line[1])
                depth += aim*int(line[1])
            elif line[0] == 'down':
                aim += int(line[1])
            elif line[0] == 'up':
                aim -= int(line[1])
    return horizontal*depth

if __name__ == '__main__':
    data_file = 'data.txt'
    with open(data_file, 'r') as d:
        data = 0
    
    print(first(data_file))
    print(second(data_file))