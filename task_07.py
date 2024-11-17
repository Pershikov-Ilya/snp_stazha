def combine_anagrams(words_array=None):
    if not words_array:
        return None

    anagrams = {}

    for i in words_array:
        sort_i = ''.join(sorted(i.lower()))
        print(i, sort_i)

        if sort_i in anagrams:
            anagrams[sort_i].append(i)
            print("after increased", anagrams, "\n")
        else:
            anagrams[sort_i] = [i]
            print("after increased", anagrams, "\n")

    return list(anagrams.values())


print(combine_anagrams(["cars", "rof", "sepotato", "for", "potatoes",
                        "racs", "four", "scar", "creams", "scream"]))