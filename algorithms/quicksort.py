def quick_sort(int_list):
    if int_list == [] or len(int_list) == 1:
        return int_list
    
    pivot = int_list[0]
    less_list =[]
    equal_list =[]
    greater_list =[]
    

    for number in int_list:
        if number < pivot:
            less_list.append(number)
        elif number == pivot:
            equal_list.append(number)
        else:
            greater_list.append(number)


    
    sorted_less = quick_sort(less_list)
    sorted_greater = quick_sort(greater_list)

    sorted_list = sorted_less + equal_list + sorted_greater
    return sorted_list

a = [5,2,7,6,9,3,5]
print(quick_sort(a))