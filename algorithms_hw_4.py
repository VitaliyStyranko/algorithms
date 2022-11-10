# 1. Even First
# Your input is a list of integers, and you have to reorder its entries so that the even entries appear first.
# You are required to solve it without allocating additional storage (operate with the input list).
# Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]


def even_first(arr):
    even_num = []
    odd_num = []
    for i in arr:
        if i % 2 == 0:
            even_num.append(i)
        if i % 2 != 0:
            odd_num.append(i)

    return even_num + odd_num


list = [7, 3, 5, 6, 4, 10, 3, 2]
print(even_first(list))



# 2. Increment a Number
# Write a program that takes as input a list of digits encoding a nonnegative decimal integer D
# and updates the list to represent the integer D + 1.
# For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].

def add_one(arr):
    index = len(arr) - 1
    while index >= 0 and arr[index] == 9:
        arr[index] = 0
        index -= 1
    if index < 0:
        arr.insert(0, 1)
    else:
        arr[index] += 1


list = [1, 2, 9]
add_one(list)
for num in list:
    print(num, end=' ')

