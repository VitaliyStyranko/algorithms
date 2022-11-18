# 1. Selection Sort
# Implement the selection sort algorithm that is sorting in descending order.


def descending_selection_sort(arr):
    for i in range(len(arr)):
        max_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]

    return arr


list_test = [5, 4, 1, 5, 12, 0, 45, -4, -1, 6]
print(descending_selection_sort(list_test))


# 2. Bubble Sort
# Implement the bubble sort algorithm that is sorting in descending order.

def descending_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


list_test = [2, 7, 23, 1, -3, 2, 0, 14]
print(descending_bubble_sort(list_test))


# 3. Insertion Sort
# Implement the insertion sort algorithm that is sorting in descending order.


def descending_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -=1
        arr[j + 1] = key

    return arr


list_test = [-7, 2, 11, 2, 0, 38, -1, 4]
print(descending_insertion_sort(list_test))


# 4. Merge Sort
# Implement the merge sort algorithm that is sorting in descending order.


def descending_merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    return descending_merge_arrays(descending_merge_sort(arr[:middle]), descending_merge_sort(arr[middle:]))


def descending_merge_arrays(left_arr, right_arr):
    merged_array = []
    i = j = 0
    while i < len(left_arr) or j < len(right_arr):
        if i == len(left_arr):
            merged_array.append(right_arr[j])
            j += 1
            continue
        if j == len(right_arr):
            merged_array.append(left_arr[i])
            i += 1
            continue

        if left_arr[i] >= right_arr[j]:
            merged_array.append(left_arr[i])
            i += 1
        else:
            merged_array.append(right_arr[j])
            j += 1
    return merged_array


list_test = [-7, 2, 20, 2, 0, 4, 9]
print(descending_merge_sort(list_test))







