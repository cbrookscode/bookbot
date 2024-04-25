def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_char_dict(text)
    print(f"{num_words} words found in the document")
    print(chars_dict)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_dict(text):
    chars = {}
    lower_case_words = text.lower()
    for char in lower_case_words:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

main()



def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_char_dict(text)
    sorted_list_from_dict = get_list_from_dict(chars_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    print("")
    print_character_counts(sorted_list_from_dict)
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(dict):
    return dict[1]

def get_char_dict(text):
    chars = {}
    lower_case_words = text.lower()
    for char in lower_case_words:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars


def get_list_from_dict(dict):
    dict_list = list(dict.items())
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def print_character_counts(list):
    for item in list:
        if not item[0].isalpha():
            continue
        print(f"The '{item[0]}' character was found {item[1]} times")

main()