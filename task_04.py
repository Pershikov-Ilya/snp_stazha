def sort_list(array):
    num = [x for x in array if isinstance(x, (int, float))]

    if not num:
        return []

    min_num = min(num)
    max_num = max(num)

    result = [max_num if x == min_num else min_num if x == max_num else x for x in array]

    result.append(min_num)

    return result


print(sort_list([]))
print(sort_list([2, 4, 6, 8]))
print(sort_list([1]))
print(sort_list(['f', 2, 1, 3]))

