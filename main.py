def wordcount(book):
    with open(book) as f:
        content = f.read()
        words = content.split()
    return len(words)

def lettercount(book):
    result = {}
    with open(book) as f:
        content = f.read()
        lowered_content = content.lower()
        for i in range(len(lowered_content)):
            char = lowered_content[i]

            if char in result:
                result[char] += 1
            else:
                result[char] = 1
    return result

     



def main():
    book = "books/frankenstein.txt"
    print(f"Report of {book}")
    words = wordcount(book)
    letters = lettercount(book)
    sorted_letters = dict(sorted(letters.items(), key=lambda item: item[1]))
    print(f"{words} words found in the document")
    for letter in sorted_letters:
        if letter.isalpha():
            print(f"The '{letter}' character was found {letters[letter]} times")
    print("END REPORT")


main()