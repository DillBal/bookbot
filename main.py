def main():
    path = "books/frankenstein.txt"
    text = read_file(path)
    num_words = word_count(text)
    char_count = character_count(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    for key in char_count:
        if key.isalpha():
            print(f"The '{key}' character was found {char_count[key]} times")
    
    print("--- End Report ---")

def word_count(text):
    words = text.split()
    return len(words)


def read_file(file_path):
    with open(file_path) as f:
        return f.read()

def character_count(text):
    lowered_text = list(text.lower())
    char_count = {}
    for char in lowered_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


if __name__=="__main__":
    main()