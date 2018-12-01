import itertools
# part 1
input_data = [int(x) for x in open("input.txt").readlines()]
print(sum(input_data))

# part 2
frequency = 0
frequency_set = set([0])
for num in itertools.cycle(input_data):
    frequency += num
    if frequency in frequency_set:
        print(frequency)
        break
    frequency_set.add(frequency)

