acc=0
visited=[]
index=0
with open ('day8-input.txt') as f:
    lines=f.readlines()

while True:
    if index in visited:
        print(f'Part1: {acc}')
        break
    else:
        visited.append(index)
    line=lines[index].replace('\n','')

    if line[:3]=='nop':
        index +=1
    elif line[:3]=='acc':
        start,num=line.split(' ')
        acc += int(num)
        index +=1
    elif line[:3]=='jmp':
        start,num=line.split(' ')
        index += int(num)
    else:
        raise Exception(f"Line started with '{line[:3]}'")


acc=0
visited=[]
index=0
triedchanging=[]
attempting=False
maxattempts=0
for line in lines:
    if 'nop' in line or 'jmp' in line:
        maxattempts+=1

linescopy=lines.copy()
attemptscounter=len(triedchanging)
while attemptscounter<=maxattempts:

    if index in visited:
        print('Failed')
        linescopy=lines.copy()
        index=0
        attempting=False
        visited=[]
        acc=0
        continue
    else:
        visited.append(index)

    line=linescopy[index].replace('\n','')

    if line[:3]=='nop':
        if attempting==False and index not in triedchanging:
            print(f'Changing: {line}')
            linescopy[index]=linescopy[index].replace('nop','jmp')
            attempting=True
            triedchanging.append(index)
            visited=[]
            index=0
            acc=0
            attemptscounter+=1
            continue
        index +=1

    elif line[:3]=='jmp':
        if attempting==False and index not in triedchanging:
            print(f'Changing: {line}')
            linescopy[index]=linescopy[index].replace('jmp','nop')
            attempting=True
            triedchanging.append(index)
            visited=[]
            index=0
            acc=0
            attemptscounter+=1
            continue
        start,num=line.split(' ')
        index += int(num)

    elif line[:3]=='acc':
        start,num=line.split(' ')
        acc += int(num)
        index +=1

        
    else:
        raise Exception(f"Line started with '{line[:3]}'")

    if index==len(lines):
        print('Success!')
        print(f'Part2: {acc}')
        break


print('This took ' +str(len(triedchanging))+' iterations')