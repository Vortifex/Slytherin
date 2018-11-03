fhand = open('dir2.txt')
count = 0
for line in fhand:
    if line.startswith('Directorio'):
        count = count + 1
print(count)

