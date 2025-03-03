def get_num_words(text):
  # split the text by space and then return the len of the array
  return len(text.split())

def get_num_chars(text):
  # split text down to char: count

  # remove all linebreaks
  remove_linebreaks = ''.join(text.splitlines())
  # remove spaces between words
  long_string = remove_linebreaks.replace(" ","")
  # change all characters to lowercase
  long_string_lowercase = long_string.lower()

  # Dictionary Comprehension listing char:counts
  char_stats_dict = {char: long_string_lowercase.count(char) for char in long_string_lowercase}

  return char_stats_dict


def get_sorted_list(dictionary):
  char_stats_list = []

  def sort_on_value(this_dict):
    # This function will be referred in the method .sort(key=''), which will allow a sort by value.
    return this_dict["count"]

  for char, count in dictionary.items():
    # Iterates over the key:value pairs of the dictionay and breaks them up into individual dictionaries that contain one key:value pair, and appends that to a list.
    char_dict = {'char': char, 'count': count}
    char_stats_list.append(char_dict)
  
  # Sorts the list and sorts by :value in reverse order.
  # NOTE: The function is mentioned by name, and not called()
  char_stats_list.sort(reverse=True, key=sort_on_value)

  return char_stats_list
  
