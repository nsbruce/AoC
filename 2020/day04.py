with open ('day4-inputedited.txt')as f:
    lines=f.readlines()
for i in range(len(lines)):
    lines[i]=lines[i][:-1]
lines.insert(0,'')

dicts=[]
dictcounter=-1
for line in lines:
    if line=='':
        dictcounter+=1
        dicts.append({})
    else:
        key,value=line.split(':')
        dicts[dictcounter][key]=value


validkeys=['byr','iyr','eyr','hgt','hcl','ecl','pid']
valideyes=['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

counter=0

for d in dicts:
    if all(item in d.keys() for item in validkeys):
        byr=int(d['byr'])
        iyr=int(d['iyr'])
        eyr=int(d['eyr'])

        if byr>=1920 and byr<=2002 and iyr>=2010 and iyr<=2020 and eyr>=2020 and eyr<=2030:
            hgt=d['hgt']
            if (hgt[-2:]=='cm' and int(hgt[:-2])>=150 and int(hgt[:-2])<=193) or (hgt[-2:]=='in' and int(hgt[:-2])>=59 and int(hgt[:-2])<=76):
                hcl=d['hcl']
                if hcl[0]=='#' and hcl[1:].isalnum():
                    ecl=d['ecl']
                    if ecl in valideyes:
                        pid=d['pid']
                        if len(pid)==9:
                            try:
                                int(pid)
                                counter +=1
                            except ValueError:
                                pass

print(counter)