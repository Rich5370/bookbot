from stats import *
import sys

def get_book_text(filepath):
  # open text file via a file path
  with open(filepath) as f:
    return f.read()


def main():

  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  book_filepath = sys.argv[1]
  book_text = get_book_text(book_filepath)

  num_words = get_num_words(book_text)
  num_chars_dict = get_num_chars(book_text)
  sorted_list = get_sorted_list(num_chars_dict)
  
  # ////////// REPORT //////////

  # Borders
  top_border = "="*12
  middle_border_1 = "-"*11
  middle_border_2 = "-"*9
  end_border = "="*13

  # >> Display Book Report

  print(f"{top_border} BOOKBOT {top_border}")
  print(f"Analyzing book found at {book_filepath}...")
  print(f"{middle_border_1} Word Count {middle_border_1}")

  # >> Display Word Count
  print(f"Found {num_words} total words")

  print(f"{middle_border_2} Character Count {middle_border_2}")

  # >> Display Char Report
  # Iterate throught list and only print ALPHA.
  for stat in sorted_list:
    if stat['char'].isalpha():
      print(f"{stat['char']}: {stat['count']}")
    else:
      continue

  # End Border
  print(f"{end_border} END {end_border}")


# Call MAIN
main()
