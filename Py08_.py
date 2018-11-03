fname = input('Enter the file name: ')
if fname== 'na na boo boo':
    print('BlastOff!')
    exit()
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
tconf=0
float(tconf)
avg=0
float(avg)
for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence'):
        count = count + 1
        spos=line.find(':')
        conf=line[spos+1:]
        fconf=float(conf)
        #print(fconf)
        tconf=tconf+fconf
        avg=tconf/count
print(tconf)
print(count)
print('Media de confianza',avg)
        
        
