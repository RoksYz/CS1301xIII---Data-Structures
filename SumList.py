def sum_lists(listint):
    result = 0

    for s in listint:
        value = 0
        for item in s:
            value+=item
        result+=value
    return result

list_of_lists = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(sum_lists(list_of_lists))
