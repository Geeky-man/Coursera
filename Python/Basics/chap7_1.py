
fh = open('word.txt')
for i in fh:
    i = i.rstrip().upper()
    print(i)
