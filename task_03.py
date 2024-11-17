def max_odd(array=None):
    if array is None or not isinstance(array, list):
        return None

    all_num = [x for x in array if isinstance(x, (int, float))]

    odd_num = [x for x in all_num if x % 2 != 0]

    if odd_num:
        return max(odd_num)
    else:
        return None


print(max_odd([1, 2, 3, 4, 4]))
print(max_odd([21.0, 2, 3, 4, 4]))
print(max_odd(['ololo', 2, 3, 4, [1, 2], None]))
print(max_odd(['ololo', 'fufufu']))
print(max_odd([2, 2, 4]))