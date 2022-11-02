import os

file_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(file_path, 'r') as input:
    all_lines = input.readlines()


# Python3 program to find a triplet
# that sum to a given value

# returns true if there is triplet with
# sum equal to 'sum' present in A[].
# Also, prints the triplet

# Found at https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/
def find3Numbers(A, arr_size, sum):
    # Fix the first element as A[i]
    for i in range(0, arr_size - 2):

        # Fix the second element as A[j]
        for j in range(i + 1, arr_size - 1):

            # Now look for the third number
            for k in range(j + 1, arr_size):
                if A[i] + A[j] + A[k] == sum:
                    print("Triplet is", A[i],
                          ", ", A[j], ", ", A[k])
                    return True

    # If we reach here, then no
    # triplet was found
    return False


all_lines = [int(i) for i in all_lines]
print(find3Numbers(all_lines, len(all_lines), 2020))