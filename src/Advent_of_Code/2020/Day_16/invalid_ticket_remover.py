import os

file_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(file_path, 'r') as input:
    all_lines = input.readlines()

for i in range(len(all_lines)):
    all_lines[i] = all_lines[i].strip("\n")

fields = []
index = 0
current_line = all_lines[index]

while not current_line == "":
    colon_index = current_line.index(":")
    split_current_line = current_line[colon_index + 2:].split(" ")
    fields.append((split_current_line[0], split_current_line[2]))
    index += 1
    current_line = all_lines[index]

ranges = []

for field in fields:
    for interval in field:
        split_field = interval.split("-")
        split_field = [int(s) for s in split_field]
        ranges.extend(range(split_field[0], split_field[1] + 1))

ranges = set(ranges)

index += 2
your_ticket = all_lines[index]
index += 3
current_line = all_lines[index]
nearby_tickets = []

while not current_line == "" and index < 261:
    nearby_tickets.append(current_line.split(","))
    index += 1
    current_line = all_lines[index]

sum = 0

for ticket in nearby_tickets:
    for number in ticket:
        number = int(number)

        if number not in ranges:
            nearby_tickets.remove(ticket)

file_path = os.path.join(os.path.dirname(__file__), "sanitized_input.txt")
with open(file_path, 'w') as sanitized_input:
    for ticket in nearby_tickets:
        ticket = ",".join(ticket)
        sanitized_input.write("%s\n" % ticket)

    sanitized_input.close()
