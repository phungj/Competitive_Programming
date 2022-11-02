import os

file_path = os.path.join(os.path.dirname(__file__), "sanitized_input.txt")

with open(file_path, 'r') as input:
    all_lines = input.readlines()

for i in range(len(all_lines)):
    all_lines[i] = all_lines[i].strip("\n")

fields = []
field_ranges = []
index = 0
current_line = all_lines[index]

while not current_line == "":
    colon_index = current_line.index(":")
    split_current_line = current_line[colon_index + 2:].split(" ")
    fields.append(current_line[:colon_index])
    field_ranges.append((split_current_line[0], split_current_line[2]))
    index += 1
    current_line = all_lines[index]

ranges = []
temp_tuple = ()

for field in field_ranges:
    temp_tuple = ()

    for interval in field:
        split_field = interval.split("-")
        split_field = [int(s) for s in split_field]
        temp_tuple += (range(split_field[0], split_field[1] + 1),)

    ranges.append(temp_tuple)

index += 2
your_ticket = all_lines[index]
index += 3
current_line = all_lines[index]
tickets = [your_ticket]

while not current_line == "" and index < 220:
    tickets.append(current_line)
    index += 1
    current_line = all_lines[index]

tickets = [i.split(",") for i in tickets]

indexed_fields = {f: [] for f in range(len(tickets[0]))}

while tickets[0]:
    for ticket in tickets:
        for i in range(len(ticket)):
            indexed_fields.get(i).append(ticket.pop(0))

field_dict = {f: -1 for f in fields}

broken = False

# while fields:
# TODO: Continue here