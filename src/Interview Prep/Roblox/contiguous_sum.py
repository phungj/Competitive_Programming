# Taken from Roblox Speak page
# Want a sneak peek at the type of questions you might get asked? Here’s a retired problem that Roblox used to ask during technical interviews:
#
# Given an array containing integers and a target number K, determine if there are continuous numbers that exist such that the sum of them equals to K.
# Examples:
#
# Input: array = [1, 2, 3, 4, 8], k = 5
# Output: true
#
# Input: array = [1, 2, 3, 4, 8], k = 0
# Output: false


def contiguous_sum(array, k):
    num_set = {0}

    curr_sum = 0

    for i in range(len(array)):
        curr_sum += array[i]

        if curr_sum - k in num_set:
            return True
        else:
            num_set.add(curr_sum)

    return False


if __name__ == '__main__':
    print(contiguous_sum([1, 2, 3, 4, 8], 5))
    print(contiguous_sum([1, 2, 3, 4, 8], 0))

    print(contiguous_sum([1], 1))
    print(contiguous_sum([-1], -1))
    print(contiguous_sum([1], -1))

    print(contiguous_sum([1, -2, 1], 0))

    print(contiguous_sum([0], 0))
    print(contiguous_sum([0, 1, -1], 0))

    print(contiguous_sum([1, -1, 2], 2))