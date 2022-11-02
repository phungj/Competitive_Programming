# A Dynamic Programming based Python
# Program for 0-1 Knapsack problem
# Returns the maximum value that can
# be put in a knapsack of capacity W
# Taken from https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/


def knapSack(W, wt, val, n):
    dp = [0 for i in range(W + 1)]  # Making the dp array

    for i in range(1, n + 1):  # taking first i elements
        for w in range(W, 0, -1):  # starting from back,so that we also have data of
            # previous computation when taking i-1 items
            if wt[i - 1] <= w:
                # finding the maximum value
                dp[w] = max(dp[w], dp[w - wt[i - 1]] + val[i - 1])

    return dp[W]  # returning the maximum value of knapsack


params = input().split(" ")
params = [int(param) for param in params]
jewel_sizes = []
jewel_values = []
min_jewel_size = 301

for i in range(params[0]):
    current_jewel = input().split(" ")
    current_jewel = [int(jewel) for jewel in current_jewel]
    jewel_sizes.append(current_jewel[0])
    jewel_values.append(current_jewel[1])

    if current_jewel[0] < min_jewel_size:
        min_jewel_size = current_jewel[0]

results = []
len_set_sizes = len(set(jewel_sizes))
min_knapsacks_size = min(min_jewel_size, params[1])

for i in range(1, min_knapsacks_size):
    results.append(0)

if len_set_sizes == 1 and params[1] > min_knapsacks_size:
    sorted_values = sorted(jewel_values, reverse=True)

    for i in range(min_knapsacks_size, params[1] + 1):
        results.append(sum(sorted_values[:i + 1]))
else:
    for i in range(min_knapsacks_size, params[1] + 1):
        results.append(knapSack(i, jewel_sizes, jewel_values, len(jewel_values)))

print(" ".join(str(result) for result in results))
