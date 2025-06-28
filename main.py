# bookbot

import sys
from stats import get_num_words, get_character_count, sort_char_dict

def get_book_text(file_path):
    file_contents = None

    with open(file_path) as file:
        file_contents = file.read()

    return file_contents

def pretty_print_report(filepath, word_count, char_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char in char_list:
        if char["name"].isalpha():
            print(f"{char["name"]}: {char["num"]}")

    print("============= END ===============")


def main():
   
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    book_text = get_book_text(book_path)

    num_words = get_num_words(book_text)

    word_dict = get_character_count(book_text)

    sorted_char_list = sort_char_dict(word_dict)

    pretty_print_report(book_path, num_words, sorted_char_list)


main()
