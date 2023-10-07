def words_sorting(*words):
    words_dictionary = {}

    for word in words:
        words_dictionary[word] = sum([ord(el) for el in word])

    if sum(words_dictionary.values()) % 2 != 0:
        return '\n'.join([f"{w} - {s}" for w, s in sorted(words_dictionary.items(), key=lambda x: -x[1])])
    else:
        return '\n'.join([f"{w} - {s}" for w, s in sorted(words_dictionary.items(), key=lambda x: x[0])])


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
    ))
print(
    words_sorting(
        'cacophony',
        'accolade'
    ))
