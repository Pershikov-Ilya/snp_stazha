def coincidence(array=None, num_for_array=None):
    if array is None or num_for_array is None:
        return []

    if not isinstance(array, list) or not isinstance(num_for_array, range):
        return []

    start, end = num_for_array.start, num_for_array.stop
    return [i for i in array if isinstance(i, (int, float)) and start <= i < end]


print(coincidence([1, 2, 3, 4, 5], range(3, 6)))
print(coincidence())
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 5)))
