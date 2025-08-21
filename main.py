from stats import count_words, count_each_character, sort_dict



def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    chars_count_dict = count_each_character(text)
    sorted_chars_list = sort_dict(chars_count_dict)

    # print report
    print(
        f"""============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------"""
    )

    for dict in sorted_chars_list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")

    print("============= END ===============")




def get_book_text(path):
    with open(path) as f:
        return f.read()



main()