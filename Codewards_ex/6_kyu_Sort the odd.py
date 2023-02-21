def sort_array(seq):
    odd = [i for i in seq if i % 2 != 0]
    odd.sort()

    for j in range(len(seq)):
        if seq[j] % 2 != 0:
            seq[j] = odd[0]
            odd.remove(odd[0])

    return seq

print(sort_array([5, 8, 6, 3, 4]))

# [-39, -33, 27, 41, -20, -20, -14, 43, 47, 16, -24] should equal
# [-39, -33, 27, 41, -20, -14, -20, 43, 47, 16, -24]


"""
Task
You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

Examples
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

"""