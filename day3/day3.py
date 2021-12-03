def get_column(matrix, index):
    return [row[index] for row in matrix]

def most_frequent_element(iterable):
    return max(set(iterable), key = iterable.count)

def least_frequent_element(iterable):
    return min(set(iterable), key = iterable.count)


input_matrix = list()
with open('./input.txt', 'r') as fio:
    #input_matrix = fio.read().splitlines()
    for line in fio:
        columns = list(line.strip())
        input_matrix.append(columns)

num_columns = len(input_matrix[0])

#part 1
gamma_rate = list()
epsilon_rate = list()

for index in range(num_columns):
    column = get_column(input_matrix, index)
    gamma_rate.append(most_frequent_element(column))
    epsilon_rate.append(least_frequent_element(column))

gamma_rate_decimal = int(''.join(gamma_rate), 2)
epsilon_rate_decimal = int(''.join(epsilon_rate), 2)

print(gamma_rate_decimal * epsilon_rate_decimal)
