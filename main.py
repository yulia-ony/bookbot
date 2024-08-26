def main():
    path_to_book = "books/frankenstein.txt"
    book_text = text_from_book(path_to_book=path_to_book)
    number_words = count_words(book_text)
    number_characters = count_characters(book_text)
    list_of_characters = list_characters(number_characters)
    print(f"--- Begin report of {path_to_book} ---")
    print(f"{number_words} words found in the document")
    print()
    for item in list_of_characters:
        print(f"TThe '{item['character']}' character was found {item['num']} times")
    print("--- End report ---")


def text_from_book(path_to_book: str):
    with open(path_to_book) as f:
        return f.read()


def count_words(text: str):
    words = text.split()
    return len(words)


def count_characters(text: str):
    characters = {}
    for char in text:
        char_low = char.lower()
        if char_low in characters:
            characters[char_low] += 1
        else:
            characters[char_low] = 1
    return characters


def list_characters(characters: dict):
    character_list = []
    for k, v in characters.items():
        if k.isalpha():
            character_list.append({"character": k, "num": v})
    character_list.sort(reverse=True, key=sort_on)
    return character_list

def sort_on(dict):
    return dict["num"]


main()