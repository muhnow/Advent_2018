import datetime, sys

input_data = [x.rstrip() for x in open("input.txt").readlines()]

records_list = []
guard_data = []

# extract the data into a dictionary of {timestamp, info from line after timestamp}
for data in input_data:
	startingIndex = data.index('-')
	
	month = int(data[startingIndex + 1:startingIndex + 3])
	day = int(data[startingIndex + 4:startingIndex + 6])
	hour = int(data[startingIndex + 7:startingIndex + 9])
	minute = int(data[startingIndex + 10:startingIndex + 12])
	info = data[data.index(']') + 2:]
	
	records_list.append({"date": datetime.datetime(1518, month, day, hour, minute), "info": info})

# sort the data by timestamp 
records_list.sort(key=lambda r: r["date"])

# build a dictionary on each of the guards for their sleep habits 
# {id, sleep list}
for record in records_list:
	if("Guard" in record["info"]):
		guard_id = int(record["info"][7:record["info"].index('begins')-1])

		if(not any(guard_id in d for d in guard_data)):
			guard_data.append({"id": guard_id, "sleep_list":[0] * 60})
	
	elif("falls asleep" in record["info"]):
		start_time = record["date"].minute
	elif("wakes up" in record["info"]):
		end_time = record["date"].minute

		guard_record = next((record for record in guard_data if record["id"] == guard_id))

		for x in range(start_time, end_time):
			guard_record["sleep_list"][x] += 1


# find the guard with the most minutes asleep, and find the minute he's asleep the most 
sleepy_guard = max(guard_data, key=lambda x:sum(x["sleep_list"]))

print(sleepy_guard["id"], sleepy_guard["sleep_list"].index(max(sleepy_guard["sleep_list"])))

# part 2 - find the guard who is the highest minutes asleep on a particular minute
sleepy_guard_2 = max(guard_data, key=lambda x:max(x["sleep_list"]));

print(sleepy_guard_2["id"], sleepy_guard_2["sleep_list"].index(max(sleepy_guard_2["sleep_list"])));