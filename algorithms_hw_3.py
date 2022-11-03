
# 1. Below The Arithmetical Mean
# When given a list, the program should return a list of all the elements below the original list’s arithmetical mean.
# The arithmetical mean is the sum of all elements divided by the number of elements.
# Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]


def less_arithmetical_mean(arr):
    avg = sum(arr) / len(arr)
    print("arithmetical mean: " + str(avg))

    for i in arr:
        if i < avg:
            print(i)

list = [1, 3, 5, 6, 4, 10, 2, 3]
print(less_arithmetical_mean(list))




# 2. Two Lowest Elements
# When given a list of elements, find the two lowest elements.
# They can be equal to each other or different.
# Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3


list = [198, 3, 4, 9, 10, 9, 2]
min1, min2 = sorted(list)[:2]
print(min1, (","), min2)









