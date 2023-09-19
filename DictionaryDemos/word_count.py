file_ref = open("minitale.txt", "r")

counts = {}

for line in file_ref:
    line = line.strip()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 0
        counts[word] = counts[word] + 1

print(counts)

file_ref.close()
