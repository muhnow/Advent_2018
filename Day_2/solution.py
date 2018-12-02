import difflib

input_data = [x.rstrip() for x in open("input.txt").readlines()]

def part1():
	two_count = three_count = 0
	has_two = has_three = False

	for data in input_data:
		for character in data:
			count = data.count(character)
			
			has_two	= True if count == 2 else has_two
			has_three = True if count == 3 else has_three

			if(has_two and has_three): break

		two_count += 1 if has_two else 0	
		three_count += 1 if has_three else 0
		has_two = has_three = False

	print(two_count * three_count)

def part2():
	correct_block = ""

	for outer, x in enumerate(input_data):
		for y in input_data[outer+1:]:
			diff_indices = [i for i in range(len(x)) if x[i] != y[i]]
			if(len(diff_indices) == 1):
				index = diff_indices[0]

				correct_block = x[:index] + x[index+1:]
				break

	print(correct_block)

part1()
part2()
