# https://en.wikipedia.org/wiki/Bubble_sort
def bubble_sort(list):
    swapped = True
    while swapped:
        swapped = False
        for i in len(list):
            if list[i-1] > list[i]:
                list[i-1], list[i] = list[i], list[i-1]
                swapped = True
    return list

# def bubble_sort_optimized(array):
#     has_swapped = True
#
#     num_of_iterations = 0
#
#     while has_swapped:
#         has_swapped = False
#         for i in range(len(array) - num_of_iterations - 1):
#             if array[i] > array[i + 1]:
#                 array[i], array[i + 1] = array[i + 1], array[i]
#                 has_swapped = True
#         num_of_iterations += 1
