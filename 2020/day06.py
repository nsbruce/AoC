temp=''
count=0
with open('day6-input.txt') as f:
    for l in f:
        l=l.replace('\n', '')

        if l.isalnum():
            temp+=l
        else:
            count+=len(''.join(set(temp)))
            temp=''
count+=len(''.join(set(temp)))
print(f'Shared: {count}')

temp=''
count=0
first=True
with open('day6-input.txt') as f:
    for l in f:
        l=l.replace('\n', '')
        if l.isalnum():
            if first==True:
                temp=l
                first=False
            else:
                temp=''.join(set(l).intersection(temp))
        else:
            count+=len(temp)
            temp=''
            first=True
count+=len(temp)
print(f'Same: {count}')