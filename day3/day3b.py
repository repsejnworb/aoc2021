from collections import Counter

def get_column(matrix, index):
    return [row[index] for row in matrix]

def multimode(iterable, reverse=False):
    c = Counter(iterable)
    if reverse:
        lowest_frequency = min(c.values())
        least_frequent = filter(lambda x: x[1] == lowest_frequency, c.most_common()[::-1])
        return list(least_frequent)
    else:
        highest_frequency = max(c.values())
        most_frequent = filter(lambda x: x[1] == highest_frequency, c.most_common())
        return list(most_frequent)

input_matrix = list()
with open('./input.txt', 'r') as fio:
    for line in fio:
        columns = list(line.strip())
        input_matrix.append(columns)

num_columns = len(input_matrix[0])

oxygen_generator_rating = 0 # most common, if equal pick 1
c02_scrubber_rating = 0 # least common, if equal pick 0

most_frequent_remaining = input_matrix[:]
least_frequent_remaining = input_matrix[:]
for index in range(num_columns):

    # oxygen
    if not len(most_frequent_remaining) == 1:
        column = get_column(most_frequent_remaining, index)
        most_frequent = multimode(column)
        match most_frequent:
            case [_, _]:
                most_frequent_remaining = [row for row in most_frequent_remaining if row[index] == '1']
                
            case [(x, _)]:
                most_frequent_remaining = [row for row in most_frequent_remaining if row[index] == x]

        if len(most_frequent_remaining) == 1:
            oxygen_generator_rating = int(''.join(most_frequent_remaining[0]), 2)

    #c02
    if not len(least_frequent_remaining) == 1:
        column = get_column(least_frequent_remaining, index)
        print(len(least_frequent_remaining))
        least_frequent = multimode(column, reverse=True)
        match least_frequent:
            case [_, _]:
                least_frequent_remaining = [row for row in least_frequent_remaining if row[index] == '0']
                
            case [(x, _)]:
                least_frequent_remaining = [row for row in least_frequent_remaining if row[index] == x]

        if len(least_frequent_remaining) == 1:
            c02_scrubber_rating = int(''.join(least_frequent_remaining[0]), 2)

print(oxygen_generator_rating)
print(c02_scrubber_rating)
print(oxygen_generator_rating*c02_scrubber_rating)




