# program to remove proper nouns from word_list.txt,
# creating word_list_no_proper.txt.

def main():
    words = set()
    f_in = open("word_list.txt")
    for line in f_in:
        word = line.strip()
        if not word[0].isupper():
            words.add(word)
    f_in.close()

    print(f'Found {len(words)} uncapitalized words')

    f_out = open("word_list_no_proper.txt", "w")
    for word in sorted(words):
        f_out.write(word + '\n')

if __name__ == "__main__":
    main()
