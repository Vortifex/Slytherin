fhand=open('directory.txt')
count = 0
for line in fhand:
    if line.startswith('18'):
        count=count + 1
print(count)
