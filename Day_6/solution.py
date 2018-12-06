input_data = [x.rstrip() for x in open("input.txt").readlines()]
#input_data = [x.rstrip() for x in open("base_input.txt").readlines()]

grid = [[0 for i in range(360)] for j in range(360)]
#grid = [[0 for i in range(40)] for j in range(40)]
coordinates = []

for index, data in enumerate(input_data):
	x = int(data[:data.index(',')])
	y = int(data[data.index(',') + 2:])

	coordinates.append((x,y))
	grid[x][y] = index;

closest = 100000
distances = []
safe_spots = 0

for y,row in enumerate(grid):
	for x,col in enumerate(row):
		for index, coord in enumerate(coordinates):
			distance = abs((x - coord[0])) + abs((y - coord[1]))
			dict_to_add = {"coordinates":coord, "distance":distance, "index":index}

			if(dict_to_add not in distances):
				distances.append(dict_to_add)
	
			closest = min(closest, distance)

		safe_spots += 1 if sum(item["distance"] for item in distances) < 10000 else 0
		shortest_coords = [d for d in distances if d["distance"] == closest]

		grid[y][x] = '.' if len(shortest_coords) > 1 else shortest_coords[0]["index"]
		distances = []
		closest = 100000

coords_to_ignore = []
area_dicts = []

for y,row in enumerate(grid):
	for x,col in enumerate(row):
		index = grid[y][x]

		if(x == 0 or x == len(row)- 1 or y == 0 or y == len(grid) - 1):
			if(index not in coords_to_ignore):
				coords_to_ignore.append(index)
		else:
			if(index not in coords_to_ignore):
				area_dict = [d for d in area_dicts if d["id"] == index]
				if(len(area_dict) == 0):
					area_dicts.append({"id":index, "area":1})
				elif(len(area_dict) > 0):
					area_dict_index = area_dicts.index(area_dict[0])

					updated_area_dict = {"id":index, "area": area_dict[0]["area"] + 1}
					area_dicts[area_dict_index] = updated_area_dict

filtered_dicts = list(filter(lambda x: x["id"] not in coords_to_ignore, area_dicts))
greatest_area = max(filtered_dicts, key=lambda x:x["area"])

print(greatest_area["area"], greatest_area["id"])
print(safe_spots)