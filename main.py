from stats import get_num_words
from stats import get_sep_count
from stats import get_sorted_dictionary
from stats import print_report
import sys
from stats import verify_sys

def get_book_text():
    with open(sys.argv[1]) as f:
        file_contents = f.read()
    print(f"{get_num_words()} words found in the document")

def main():
    verify_sys()
    print_report(sys.argv[1],get_num_words(),get_sorted_dictionary())

main()