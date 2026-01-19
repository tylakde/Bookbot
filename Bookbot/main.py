
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents
def get_word_count(file_contents):
    text = file_contents.split()
    return len(text)


def main():
    frankenstein =  "/home/tyla/workspace/Bookbot/books/books/frankenstein.txt"
    book_contents = get_book_text(frankenstein)
    print(book_contents)
    wordcount = get_word_count(book_contents)
    print(f"{wordcount} words found.")
main()
