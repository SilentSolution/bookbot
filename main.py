import sys
from stats import (
    count_words, 
    count_each_character, 
    sort_dict
)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    num_words = count_words(text)
    chars_count_dict = count_each_character(text)
    sorted_chars_list = sort_dict(chars_count_dict)
    print_report(book_path, num_words, sorted_chars_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def print_report(book_path, num_words, sorted_chars_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for dict in sorted_chars_list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")

    print("============= END ===============")


main()