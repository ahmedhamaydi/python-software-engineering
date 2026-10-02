def selection_sort(items_list):

    for index, number in enumerate(items_list):
        minimum_index = index

        for search_index in range(index + 1, len(items_list)):
            if items_list[search_index] < items_list[minimum_index]:
                minimum_index = search_index

        if minimum_index != index:
            items_list[index], items_list[minimum_index] = items_list[minimum_index], items_list[index]

    return items_list


items = [5, 2, 7, 1, 3]
print(selection_sort(items))