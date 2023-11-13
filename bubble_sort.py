list = [7, 6, 2, 3, 10, 13]
print(list)
def bubble_sort(list):
    n = len(list)
    for i in range (n):
        for y in range (0, n-i-1):
            if list[y]>list[y+1]:
                list[y], list[y+1] = list[y+1], list[y]
    return list

print(bubble_sort(list))
