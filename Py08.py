fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
totconf=0
for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence'):
        count = count + 1
        spos=line.find(':')
        conf=line[spos+1:]
        print(count)
        float(conf)
        totconf=totconf+conf
print(totconf)
        
        
