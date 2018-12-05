input_data = open("input.txt").readline();
#input_data = "dabAcCaCBAcCcaDA"

## Original Solution 
def parsePolymer(polymer):
	currUnit = lastUnit = ""
	returnPolymer = ""
	hasChanged = False

	for index,unit in enumerate(polymer):
		if(not lastUnit):
			lastUnit = unit
		elif(lastUnit):
			currUnit = unit

			if(((currUnit.islower() and lastUnit.isupper()) or (currUnit.isupper() and lastUnit.islower()))
			 	and lastUnit.upper() == currUnit.upper()):
				
				polymer[index] = ""
				polymer[index-1] = ""
				
				lastUnit = ""
				hasChanged = True

			else:
				lastUnit = currUnit

	return returnPolymer.join(polymer),hasChanged


#result,hasChanged = parsePolymer(list(input_data))

#while(hasChanged):
#	result,hasChanged = parsePolymer(list(result))


# Revised Solution
def parsePolymerAsStack(polymer):
	stack = []

	for currUnit in polymer:
		popped = False

		if stack:
			lastUnit = stack[-1]

			if(((currUnit.islower() and lastUnit.isupper()) or (currUnit.isupper() and lastUnit.islower()))
				and currUnit.upper() == lastUnit.upper()):

				stack.pop()
				popped = True

		if not popped:
			stack.append(currUnit)

	return len(stack)

print(parsePolymerAsStack(input_data))

# Part 2
alphabet = 'abcdefghijklmnopqrstuvwxyz'
configs = []
polymer_stats = []
answer = 1000000000

for letter in alphabet:
	temp_input = input_data

	temp_input = temp_input.replace(letter.upper(), '')
	temp_input = temp_input.replace(letter.lower(), '')

	answer = min(answer, parsePolymerAsStack(temp_input))

print(answer)
