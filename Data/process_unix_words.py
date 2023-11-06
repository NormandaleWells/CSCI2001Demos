# program to process unix_words_raw.txt
# to unix_words.txt.

f_in = open("unix_words_raw.txt", 'r')
f_out = open("unix_words.txt", 'w')
for line in f_in:
    word = line.strip()
    if word.lower() != word:
        continue
    if word[-2:] == "'s":
        continue
    f_out.write(line)
f_out.close()
f_in.close()
