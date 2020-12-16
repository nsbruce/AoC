from collections import defaultdict
from itertools import permutations, product

lines=open("day14-input.txt").read().splitlines()

mem=defaultdict(int)

for line in lines:
    key, val = line.split(' = ')
    if key=='mask':
        mask=val
    else:
        val=f"{int(val):036b}"
        res=''
        for i in range(len(val)):
            if mask[i] !='X':
                res+=mask[i]
            else:
                res+=val[i]
        mem[key]=int(res,2)

total=sum(mem.values())
print(f"Part1: {total}")


del mem
del mask

lines=open("day14-input.txt").read().splitlines()
mem=defaultdict(int)

def perm(length, chars='01'):
    permiter = product(chars,repeat=length)
    perms = [''.join(p) for p in permiter]
    return perms

for line in lines:
    key, val = line.split(' = ')
    if key=='mask':
        mask=val
    else:
        key=f"{int(''.join(filter(str.isdigit, key))):036b}"
        res=''
        for i in range(len(key)):
            if mask[i]=='0':
                res+=key[i]
            elif mask[i]=='1':
                res+=mask[i]
            elif mask[i]=='X':
                res+='X'
            else:
                raise ValueError(f"Char is {mask[i]}")
        if res.count('X')>0:
            floaters=perm(res.count('X'))
            for f in floaters:
                temp=res
                for i in range(res.count('X')):
                    temp=temp.replace('X',f[i],1)
                mem[temp]=int(val)
        else:
            mem[res]=int(val)
            

total=sum(mem.values())
print(f"Part2: {total}")

