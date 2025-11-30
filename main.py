import sys
from stats import get_count_words, get_count_characters, chars_dict_to_sorted_list

def main():

    how_to_use()

    book_path = sys.argv[1]
    book = get_book_text(book_path)
    words_count = get_count_words(book)
    characters_count = get_count_characters(book)
    sorted_list = chars_dict_to_sorted_list(characters_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for ch in sorted_list:
        if ch["name"].isalpha() == True:
            print(f"{ch["name"]}: {ch["num"]}")
    print("============= END ===============")
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

def how_to_use():
    entry = sys.argv
    if len(entry) != 2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()