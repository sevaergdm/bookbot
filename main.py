from stats import count_words, count_characters, create_sorted_list_of_dicts
import sys


def main():
    args = sys.argv

    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = get_book_text(args[1])
    num_words = count_words(book)
    num_chars = count_characters(book)
    dict_list = create_sorted_list_of_dicts(num_chars)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in dict_list:
        print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


main()
