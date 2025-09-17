from stats import count_words, count_characters

def get_book_text(path):
    with open(path) as file:
        return file.read()


def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_text)
    print(f"{num_words} words found in the document")
    char_count = count_characters(book_text)
    print(char_count)
    

if __name__ == "__main__":
    main()
