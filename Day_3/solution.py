input_data = [x.rstrip() for x in open("input.txt").readlines()]

fabric = [[0 for i in range(1500)] for j in range(1500)]

def part1():
	overlap = 0
	perfect_claim = 0
	isOverlapped = False

	for data in input_data:
		order_id = int(data[1:data.index(' @')])
		column = int(data[data.index('@ ') + 2:data.index(',')])
		row = int(data[data.index(',') + 1:data.index(':')])
		width = int(data[data.index(': ') + 2:data.index('x')])
		height = int(data[data.index('x') + 1:])

		for r in range(0, height):
			for c in range(0, width):
				value = fabric[row + r][column + c]

				fabric[row + r][column + c] = order_id if value == 0 or value == order_id else 'X'
				
				if(fabric[row + r][column + c] == 'X'):
					isOverlapped = True

		if(isOverlapped == False): 
			print(order_id)
		else:
			isOverlapped = False


	for row in fabric:
		overlap += row.count('X')

	print(overlap)

part1()
part1()