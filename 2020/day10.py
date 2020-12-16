from collections import defaultdict

lines=sorted(int(line) for line in open('day10-input.txt').readlines())
lines.append(max(lines)+3)
diffs=[lines[0]]
for i in range(1,len(lines)):
    diffs.append(lines[i]-lines[i-1])
if max(diffs)>3:
    raise ValueError(f'Diffs max is {max(diffs)}')
print(len(diffs))

print(f'Part1: {diffs.count(1)*diffs.count(3)}')

paths_to_point = defaultdict(int)
paths_to_point[0]=1
for l in lines:
    paths_to_point[l]=paths_to_point[l-1]+paths_to_point[l-2]+paths_to_point[l-3]
print(f"Part2: {paths_to_point[max(lines)]}")
