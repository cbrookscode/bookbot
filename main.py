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
