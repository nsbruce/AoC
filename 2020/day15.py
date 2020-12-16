
nums=open("day15-input.txt").read().split(',')
nums=[int(n) for n in nums]

def playelfgame(seq, stop):
    while len(seq)<stop:
        indexes = [i for i, x in enumerate(seq) if x==seq[-1]]
        if len(indexes)==1:
            seq.append(0)
        else:
            seq.append(indexes[-1]-indexes[-2])
    return seq[-1]

def playelfgame2(seq,stop):
    thedict={num:index for index,num in enumerate(seq,1)}
    index=len(seq)
    current=seq[-1]
    
    while index<stop:
        prev=thedict.get(current) # Returns none if it doesn't exist
        thedict[current]=index
        current=index-prev if prev else 0
        index+=1
    return current


print(f'Part1: {playelfgame2(nums,2020)}')
print(f'Part2: {playelfgame2(nums,30000000)}')
