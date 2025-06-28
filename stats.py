# bookbot

def get_num_words(text):
    words = text.split()
    return len(words)


def get_character_count(text):

    char_dict = {}

    lowercase_text = text.lower()

    words = lowercase_text.split()

    for word in words:
        characters = list(word)

        for character in characters:
            if character not in char_dict:
                char_dict[character] = 1
            else:
                char_dict[character] += 1

    return char_dict

def sort_on(items):
    return items["num"]

def sort_char_dict(char_dict):
    list_of_dicts = []

    for character in char_dict:
        new_char_dict = {"name": character, "num": char_dict[character]}
        list_of_dicts.append(new_char_dict)

    list_of_dicts.sort(reverse=True, key=sort_on)

    return list_of_dicts
