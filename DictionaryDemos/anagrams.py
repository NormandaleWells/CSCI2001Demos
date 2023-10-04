import sys


def get_letters(word):
    return "".join(sorted(word))


def main():
    word_file = open("word_list_no_proper.txt")
    anagrams = {}
    for line in word_file:
        word = line.strip().lower()
        letters = get_letters(word)
        if letters not in anagrams:
            anagrams[letters] = [word]
        else:
            anagrams[letters].append(word)

    for line in sys.stdin:
        line = line.strip()
        letters = get_letters(line)
        if letters in anagrams:
            print(anagrams[letters])
        else:
            print(f"{line} is not a known word")


if __name__ == "__main__":
    main()
