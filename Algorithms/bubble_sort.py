# https://en.wikipedia.org/wiki/Bubble_sort
def bubble_sort(list):
    swapped = True
    size = len(list)
    while swapped:
        swapped = False
        for i in range(size):
            if list[i-1] > list[i]:
                list[i-1], list[i] = list[i], list[i-1]
                swapped = True
                print(list)
    return list

list = [10,1,9,2,8,3,7,4,6,5]
sroted = bubble_sort(list)
print(list)
