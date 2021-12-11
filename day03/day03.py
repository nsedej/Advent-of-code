def line_generator(line):
    # yields next line character converted to int
    for char in line:
        try:
            yield(int(char))
        except: 
            pass

def decimal(number):
    # number is list of bits
    number = number[::-1] # reverse bit order
    return sum(number[i]*2**i for i in range(len(number)))

class DataHandler():
    def __init__(self, data):
        self.data = data
        self.length = len(data)
        self.gamma = decimal(self.most_common)
        self.epsilon = decimal(self.least_common)
        self.consumption = self.gamma*self.epsilon

    @property
    def most_common(self):
        for line in self.data:
            line_list = list(line_generator(line))
            try:
                line_sum = [line_list[i] + line_sum[i] for i in range(len(line_list))]
            except:
                line_sum = line_list
        return [1 if n>len(self.data)/2 else 0 for n in line_sum]

    @property
    def least_common(self):
        return [1 if n == 0 else 0 for n in self.most_common]

if __name__ == '__main__':
    data_file = 'input'
    with open(data_file, 'r') as d:
        data = [line for line in d]

    a = BinaryData(data)
    print(a.epsilon)
    print(a.gamma)
    print(a.consumption)
