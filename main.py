def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    chars_dict = character_count(text)
    sorted_dict = list_dict(chars_dict)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    
    for chars in sorted_dict:
        print(f"The '{chars["name"]}' character was found {chars["num"]} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    text_lower = text.lower()
    text_dict = {}
    for letter in text_lower:
        if letter in text_dict:
            text_dict[letter] += 1
        else:
            text_dict[letter] = 1
    return text_dict

def sort_on(dict):
    return dict["num"]

def list_dict(dict):
    char_list = []
    for key in dict:
        if key.isalpha():
            new_dict = {}
            new_dict["name"] = key
            new_dict["num"] = dict[key]
            char_list.append(new_dict)
    char_list.sort(reverse=True, key=sort_on)
    return char_list

main()