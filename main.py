from sys   import argv, exit
from stats import get_words_count, get_char_counts, get_sorted_list_char_counts

def main():
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    
    file_path = argv[1]
    text = get_book_text(file_path)

    num_words = get_words_count(text)
    char_counts = get_char_counts(text)
    sorted_char_counts = get_sorted_list_char_counts(char_counts)

    print_results(file_path, num_words, sorted_char_counts)

    return

def get_book_text(file_path: str) -> str:
    res = ""

    with open(file_path) as inFile:
        res = inFile.read()

    return res

def print_results(book_path: str, word_count: int, count_list: list[dict[str, int]]) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    print_char_results(count_list)

    return

def print_char_results(char_dicts: list[dict[str, int|str]]) -> None:
    for char_dict in char_dicts:
        if char_dict["letter"].isalpha():
            print(f"{char_dict['letter']}: {char_dict['count']}")

main()

