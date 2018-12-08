input_data = [x.rstrip() for x in open("input.txt").readlines()]
#input_data = [x.rstrip() for x in open("base_input.txt").readlines()]

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

def process_sequence(seq):
	step_dicts = [d for d in seq if d["dependencies"] == []]

	if(len(step_dicts) == 1):
		return step_dicts[0]["step"],step_dicts[0]
	elif(len(step_dicts) > 1):
		matching_dict = min(step_dicts, key=lambda x:x["step"])
		return matching_dict["step"],matching_dict
	else:
		return None

def prune_sequence(seq, step):
	dependent_steps = [d for d in seq if step in d["dependencies"]]

	for x in dependent_steps:
		x["dependencies"].pop(x["dependencies"].index(step))

	return seq

ordered_steps = []

part2_sequence = sequence

while len(sequence) > 0:
	next_step,matching_step = process_sequence(sequence)
	if(next_step is None):
		break
	else:
		ordered_steps.append(next_step)
		sequence.pop(sequence.index(matching_step))
		if(len(matching_step) > 0):
			prune_sequence(sequence, next_step)


print("".join(ordered_steps))


