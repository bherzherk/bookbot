from stats import word_counter, char_counter, sort_dict
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    number_of_words = word_counter(text)
    number_of_characters = char_counter(text)
    number_of_characters = sort_dict(number_of_characters)
    print(f"Found {number_of_words} total words")
    for key, value in number_of_characters.items():
        if key.isalpha():
            print(f"{key}: {value}")

main()
