def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = get_book_count(text)
    character_dict = get_character_count(text)
    print(character_dict)





def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_book_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    characters = {}
    l_text = text.lower()
    for c in l_text:
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1
    return characters
    

main()