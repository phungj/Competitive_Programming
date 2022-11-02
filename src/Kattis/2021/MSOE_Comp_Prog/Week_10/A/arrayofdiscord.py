n = int(input())
nums = [int(x) for x in input().split(" ")]

current_num = 0
i = 1

while i < n:
    prev_num = nums[i - 1]
    current_num = nums[i]

    if (prev_num == 0 and current_num != 9 and len(str(current_num)) == 1) or (prev_num != 0 and len(str(current_num)) == len(str(prev_num)) and (str(current_num) != '9' * len(str(current_num)) or current_num == 9) or prev_num == current_num):
        nums[i] = str(nums[i])

        if current_num == 9 and prev_num == 0 and i == len(nums) - 1:
            print("impossible")
            exit(0)
        elif prev_num == 1:
            nums[i] = 0
        elif prev_num == 0 and current_num != 9:
            nums[i - 1] = 9
        elif prev_num == current_num and str(nums[i - 1])[0] == '1':
            prev_first_digit = str(nums[i - 1])[0]

            if prev_first_digit == '1':
                prev_first_digit = '9'
            else:
                prev_first_digit = '1'

            nums[i - 1] = int(prev_first_digit + str(nums[i - 1])[1:])
        else:
            first_digit = nums[i][0]

            if first_digit == '9':
                first_digit = '1'
            else:
                first_digit = '9'

            nums[i] = int(str(first_digit) + nums[i][1:])

        nums = [str(num) for num in nums]
        print(' '.join(nums))
        exit(0)
    else:
        i += 1

print("impossible")
