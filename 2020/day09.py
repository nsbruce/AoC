# bufferlen=5 # for day9-inputtest.txt
bufferlen=25
with open('day9-input.txt') as f:
    lines=f.readlines()
lines=[int(line.replace('\n','')) for line in lines]

for i in range(bufferlen,len(lines)):
    sumval=lines[i]
    buf=lines[i-bufferlen:i]
    check=[sumval-b for b in buf]
    shared=list(set(buf).intersection(check))
    if len(shared)>1:
        for item in shared:
            if item*2==sumval:
                shared.remove(item)
    if len(shared)==0:
        print(f'Part1: {sumval}')
        break

for i in range(len(lines)):
    tempsum=0
    counter=0
    while tempsum<sumval:
        tempsum+=lines[i+counter]
        counter +=1
    if tempsum==sumval:
        print(f'Part2: {min(lines[i:i+counter])+max(lines[i:i+counter])}')
        break
