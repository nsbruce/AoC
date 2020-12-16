import numpy as np

class Rule:
    def __init__(self, name, rules):
        self.name=name
        self.ranges=self.__parse_rules__(rules)

    def __parse_rules__(self, rules):
        rules = rules.split(' or ')
        rules = [list(map(int, rule.split('-'))) for rule in rules]
        return rules

    def get_illegal(self, numbers):
        if not numbers:
            return None
        illegal=numbers.copy()
        for n in numbers:
            if (min(self.ranges[0]) <= n <= max(self.ranges[0])) or (min(self.ranges[1]) <= n <= max(self.ranges[1])):
                illegal.remove(n)

        if len(illegal)<1:
            return None
        else:
            return illegal
    
    def get_allvalid(self, numbers):
        return all(((min(self.ranges[0]) <= x <= max(self.ranges[0])) or (min(self.ranges[1]) <= x <= max(self.ranges[1]))) for x in numbers)


sections= open('day16-input.txt').read().split('\n\n')

rules=sections[0].split('\n')

_, yourticket=sections[1].split('\n')
yourticket=list(map(int, yourticket.split(',')))
nearbytickets=[list(map(int, a.split(','))) for a in sections[2].split('\n')[1:]]
rules=[Rule(r.split(': ')[0],r.split(': ')[1]) for r in rules]


# Part 1
errors=[]
validtickets=nearbytickets.copy()
for t in nearbytickets:
    tempticket=t.copy()
    for r in rules:
        tempticket=r.get_illegal(tempticket)
    if tempticket:
        validtickets.remove(t)
        errors=errors+tempticket

print(f"Part1: {sum(errors)}")



# Part 2
validtickets.append(yourticket)
validtickets=np.array(validtickets)
names={r.name:[] for r in rules}

ticketlen=validtickets.shape[1]

for i in range(ticketlen):
    for rule in rules:
        if rule.get_allvalid(validtickets[:,i]):
            names[rule.name].append(i)


definednames={}
departureindexes=[]
while len(names)>0:
    for i in range(ticketlen):
        if [i] in names.values():
            name=list(names.keys())[list(names.values()).index([i])]
            definednames[name]=i
            if 'departure' in name:
                departureindexes.append(i)
            names.pop(name)
            for name in names:
                if i in names[name]:
                    names[name].remove(i)

total=1
for i in departureindexes:
    total*=yourticket[i]

print(f"Part2: {total}")
