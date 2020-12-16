import numpy as np
lines=open('day13-input.txt').read().splitlines()

earliest=int(lines[0])
print(f"I can leave at {earliest}")
buses=lines[1].split(',')
buses=list(filter(('x').__ne__, buses))
buses=[int(bus) for bus in buses]
print(f"Bus options are {buses}")

for bus in buses:
    print(f"Bus: {bus}, Nearest: {np.ceil(earliest/bus)}, Diff: {np.ceil(earliest/bus)*bus-earliest}")



offsets = []
for idx, item in enumerate(lines[1].split(',')):
    if item != 'x':
        offsets.append(idx)

def chinese_remainder(values):
    prod = 1
    for _, n in values:
        prod *= n
    total = 0
    for val, n in values:
        b = prod // n
        total += val * b * pow(b, n - 2, n)
        total %= prod
    return total

bus = [int(x) if x != "x" else -1 for x in lines[1].split(",")]
off = [(bus[x]-x,bus[x]) for x in range(len(bus)) if bus[x] > 0]
print(chinese_remainder(off))