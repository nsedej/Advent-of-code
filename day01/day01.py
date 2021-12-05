def depth_inc_count(data_file):
    count = 0
    for i in range(1,len(data)):
        if data[i] > data[i-1]:
            count += 1
    return count

def depth_inc_count_3s(data_file):
    count = 0
    for i in range(len(data)-3):
        prev = sum(data[i-1:i+2])
        if prev < sum(data[i:i+3]):
            count += 1
    return count

if __name__ == '__main__':
    data_file = 'data.txt'
    with open(data_file, 'r') as d:
        data = [int(line) for line in d]

    print(depth_inc_count(data_file))
    print(depth_inc_count_3s(data_file))
