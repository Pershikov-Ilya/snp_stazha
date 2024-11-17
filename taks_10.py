import re


def count_words(stroke: str):

    stroke = stroke.lower()
    if not isinstance(stroke, str):
        print(False)

    result = {}
    find_words = re.findall(r'\w+', stroke)

    for i in find_words:
        count = find_words.count(i)
        result[i] = count

    return result


print(count_words("A man, a plan, a canal -- Panama"))

