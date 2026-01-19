
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents
def main():
    frankenstein =  "/home/tyla/workspace/Bookbot/Bookbot/books/books/frankenstein.txt"
    book_contents = get_book_text(frankenstein)
    print(book_contents)
main()
