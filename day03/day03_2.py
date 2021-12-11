def line_generator(line):
    # yields next line character converted to int
    for char in line:
        try:
            yield(int(char))
        except: 
            pass

def decimal(number):
    # number is list of bits
    return sum(number[i]*2**i for i in range(len(number)))

class DataHandler():
    def __init__(self, data):
        self._data = data
        self.gamma = decimal(self.most_common(data)[::-1])
        self.epsilon = decimal(self.least_common(data)[::-1])
        self.consumption = self.gamma*self.epsilon

        self.O_rating = decimal(self.bit_criteria_oxygen()[::-1])
        self.CO2_rating = decimal(self.bit_criteria_CO2()[::-1])
    
    @property
    def data(self):
        # turn list of strings into list of lists
        return [list(line_generator(line)) for line in self._data]

    @staticmethod
    def most_common(data):
        for line in data:
            line_list = list(line_generator(line))
            try:
                line_sum = [line_list[i] + line_sum[i] for i in range(len(line_list))]
            except:
                line_sum = line_list
        return [1 if n>=len(data)/2 else 0 for n in line_sum]

    def least_common(self, data):
        return [1 if n == 0 else 0 for n in self.most_common(data)]

    def bit_criteria_oxygen(self):
        data = self.data
        bit_counter = 0
        while len(data) > 1:
            data_new = []
            most_common = self.most_common(data)
            for line in data:
                if line[bit_counter] == most_common[bit_counter]:
                    data_new.append(line)
            bit_counter += 1
            data = data_new
        return data_new[0]

    def bit_criteria_CO2(self):
        data = self.data
        bit_counter = 0
        while len(data) > 1:
            data_new = []
            most_common = self.least_common(data)
            for line in data:
                if line[bit_counter] == most_common[bit_counter]:
                    data_new.append(line)
            bit_counter += 1
            data = data_new
        return data_new[0]
        




if __name__ == '__main__':
    data_file = 'input'
    with open(data_file, 'r') as d:
        data = [line for line in d]

    a = DataHandler(data)
    print(a.O_rating)
    print(a.CO2_rating)
    print(a.O_rating*a.CO2_rating)
