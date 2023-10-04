'''
This program converts words_4000_raw.txt to words_4000.txt
'''

word_list = []

f = open("words_4000_raw.txt", 'r')
for line in f:
    words = line.strip().split('\t')
    if len(words) != 4:
        # This is expected for the last line!
        print(f"Invalid line: {line}")
    word_list += words
f.close()

word_list = [word for word in word_list if word == word.lower()]
word_list.append('i')       # eliminated with removing caps
word_list.append('ate')     # just happened to catch this omission
word_list.sort()

f = open("words_4000.txt", 'w')
for word in word_list:
    f.write(word)
    f.write('\n')
