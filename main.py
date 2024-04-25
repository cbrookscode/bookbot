def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_char_dict(text)
    sorted_list_from_dict = char_dict_to_sorted_list(chars_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    print()
    for item in sorted_list_from_dict:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_dict(text):
    chars = {}
    lower_case_characters = text.lower()
    for char in lower_case_characters:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def char_dict_to_sorted_list(char_dict):
    sorted_list = []
    for char in char_dict:
        sorted_list.append({"char": char, "num": char_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()