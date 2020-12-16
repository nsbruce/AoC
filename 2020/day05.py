
ids=[]
with open ('day5-input.txt') as f:
    for l in f:
        l=l.replace('F', '0').replace('B', '1').replace('R','1').replace('L','0')
        i=int(l[:7],2)*8+int(l[7:],2)
        ids.append(id)
print(max(ids))

missing=[]
for i in range(955):
    if i not in ids:
        missing.append(i)
print(missing)