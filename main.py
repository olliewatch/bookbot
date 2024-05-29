def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    num_chars = get_char_count(text.lower())
    char_report = get_char_report(num_chars)
    
    
    #print(f"{num_words} words found in this book.")
    #print(num_chars)
    generate_report(num_words, char_report, book_path)
    
    
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    #Initialise empty dictionary
    char_dict = {}
    
    #Loop through characters in the text
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        elif char.isalpha():
            char_dict[char] = 1
    return char_dict

def get_char_report(dict):
    #Inititalise empty list
    char_report = []
    
    #Loop through keys and values of char_dict
    for char, count in dict.items():
        #Create a new dictionary for each character and it's count
        new_dict = {"char" : char, "num" : count}
        
        #Append new dictionary to the list
        char_report.append(new_dict)
    char_report.sort(reverse = True, key = sort_on)
    return char_report

def generate_report(word_count, char_report, path):
    #Print header
    print(f"--- Begin report on {path} ---")
    
    #Print word count
    print(f"{word_count} words found in the document")
    
    #Loop through the sorted list of dictionaries
    for item in char_report:
        char = item["char"]
        count = item["num"]
        print(f"The '{char}' character was found '{count}' times")
    
    #Print footer
    print("--- End report ---")

def sort_on(dict):
    return dict["num"]



if __name__ == "__main__":
    main()