from stats import count_words

def get_book_text(path):
    with open(path) as file:
        return file.read()


def main():
    num_words = count_words(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document")


if __name__ == "__main__":
    main()
