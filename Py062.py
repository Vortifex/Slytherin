fhand = open('directory.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('28/10/2018') == -1: continue
print(line)

