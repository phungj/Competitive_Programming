import os

def subArraySum(arr, n, sum_):
    # Pick a starting
    # point
    for i in range(n):
        curr_sum = arr[i]

        # try all subarrays
        # starting with 'i'
        j = i + 1
        while j <= n:

            if curr_sum == sum_:
                print("Sum found between")
                print("indexes % d and % d" % (i, j - 1))

                return i, j

            if curr_sum > sum_ or j == n:
                break

            curr_sum = curr_sum + arr[j]
            j += 1

    print("No subarray found")
    return 0


file_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(file_path, 'r') as input:
    all_lines = input.readlines()

for i in range(len(all_lines)):
    all_lines[i] = all_lines[i].strip('\n')
    all_lines[i] = int(all_lines[i])

invalid_num = 373803594

indices = subArraySum(all_lines, len(all_lines), invalid_num)
sub_array = all_lines[indices[0]:indices[1]]

print(min(sub_array) + max(sub_array))
