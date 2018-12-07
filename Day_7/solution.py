#input_data = [x.rstrip() for x in open("input.txt").readlines()]
input_data = [x.rstrip() for x in open("base_input.txt").readlines()]

sequence = []

for data in input_data:
	first = data[5]
	second = data[36]

	first_dict = [d for d in sequence if d["step"] == first]
	second_dict = [d for d in sequence if d["step"] == second]

	if(not first_dict):
		sequence.append({"step":first, "dependencies":[]})

	if(second_dict):
		dependencies = second_dict[0]["dependencies"]
		
		if(first not in dependencies):
			dependencies.append(first)
			sequence[sequence.index(second_dict[0])] = {"step":second, "dependencies":dependencies}
	
	else:
		sequence.append({"step":second, "dependencies":[first]})


# Now that we have all of the steps with each of their dependencies, maybe
# the next steps would be to start by completing the steps with no dependencies 
# based on alphabetical order. As a step is completed, go through and update the dependencies 
# of all steps that contain the completed step to indicate it has been completed 
