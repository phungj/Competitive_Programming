from collections import Counter

def subarraySum(nums: list[int], k: int) -> int:
    count = 0
    num_counter = Counter()
    num_counter[0] += 1

    curr_sum = 0

    for i in range(len(nums)):
        curr_sum += nums[i]

        if curr_sum - k in num_counter:
            count += num_counter[curr_sum - k]

        num_counter[curr_sum] += 1

    return count


if __name__ == '__main__':
    print(subarraySum([1, -1, 0], 0))
    print(subarraySum([1, 2, 3], 3))
    print(subarraySum([1, 1, 2], 2))