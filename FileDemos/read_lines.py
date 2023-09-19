file_ref = open("minitale.txt", "r")

lines = file_ref.readlines()

for line in lines:
    #line = line.strip()
    #words = line.split()
    print(line)
    #print(words)

file_ref.close()
