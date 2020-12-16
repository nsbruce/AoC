import re

allowedbags=['shiny gold']
prev = -1
curr = 0
with open('day7-input.txt') as f:
    while prev<curr:
        prev = curr
        f.seek(0,0)
        for line in f:
            parent,children=line.split('contain')
            parent=parent.replace(' bags ','')
            for color in allowedbags:
                if color in children and parent not in allowedbags:
                    allowedbags.append(parent)
        curr=len(allowedbags)
print(f'Part 1: {len(allowedbags)-1}')# -1 because shiny gold doesn't count


class Bag:
    def __init__(self, color, children):
        self.child_endings=[' bags.',' bags', ' bag.', ' bag']
        self.color=self.__parse_color__(color)
        self.children=self.__parse_children__(children)

    def __parse_children__(self,children):
        children=children.split(', ')
        if 'no other' in children[0]:
            return []
        else:
            output=[]
            for child in children:
                number=int(child[0])
                for ending in self.child_endings:
                    child=child.replace(ending,'')
                child=child.replace('\n','')
                child=child[2:]
                output.extend([child for i in range(number)])
            return output

    def __parse_color__(self,color):
        return color.replace(' bags','')

bags=[]
with open('day7-input.txt') as f:
    for line in f:
        parent,children=line.split(' contain ')
        bags.append(Bag(parent,children))

included=[]
for bag in bags:
    if bag.color=='shiny gold':
        included.append([bag])


index=0
while len(included[index])>0:
    lastchildren=[]
    for bag in included[index]:
        temp=bag.children
        for child in temp:
            lastchildren.append(child)
    if index==0:
        print(lastchildren)
    included.append([])
    index += 1

    for bag in bags:
        if bag.color in lastchildren:
            number=lastchildren.count(bag.color)
            included[index].extend([bag for i in range(number)])
            # bags.remove(bag)


count=0
for i in included:
    count+=len(i)
print(f'Part 2: {count-1}')