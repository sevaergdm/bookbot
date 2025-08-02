def count_words(txt):
    words = txt.split()
    return len(words)


def count_characters(txt):
    char_dict = {}
    for char in txt:
        lower_char = str(char).lower()
        if lower_char not in char_dict:
            char_dict[lower_char] = 1
        else:
            char_dict[lower_char] += 1
    return char_dict


def sort_on(items):
    return items["num"]


def create_sorted_list_of_dicts(dict):
    output = []
    for i in dict:
        if i.isalpha():
            output.append({"char": i, "num": dict[i]})

    output.sort(reverse=True, key=sort_on)

    return output
