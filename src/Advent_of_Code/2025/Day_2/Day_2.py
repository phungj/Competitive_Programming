# Part 1
# with open('input.txt', 'r') as input_file:
#     ranges = input_file.readline().split(',')
#     split_ranges = [range.split('-') for range in ranges]
#     invalid_id_sum = 0

#     for start, end in split_ranges:
#         for i in range(int(start), int(end) + 1):
#             str_i = str(i)

#             if len(str_i) % 2 == 0 and str_i[:len(str_i) // 2] == str_i[len(str_i) // 2:]:
#                 invalid_id_sum += i
        
#     print(invalid_id_sum)

# Part 2

with open('input.txt', 'r') as input_file:
    ranges = input_file.readline().split(',')
    split_ranges = [range.split('-') for range in ranges]
    invalid_id_sum = 0

    for start, end in split_ranges:
        for i in range(int(start), int(end) + 1):
            str_i = str(i)
            str_i_len = len(str_i)

            for j in range(1, str_i_len // 2 + 1):
                if str_i_len % j == 0:
                    if str_i[:j] * (str_i_len // j) == str_i:
                        invalid_id_sum += i

                        break
        
    print(invalid_id_sum)
