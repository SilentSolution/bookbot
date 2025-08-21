from stats import count_words, count_each_character



def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    characters_count = count_each_character(text)
    print(f"{num_words} words found in the document")
    print(characters_count)



def get_book_text(path):
    with open(path) as f:
        return f.read()



main()