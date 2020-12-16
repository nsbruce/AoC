import numpy as np
lines=open('day12-inputtest.txt').read().splitlines()

dirs=[line[0] for line in lines]
mags=[int(line[1:]) for line in lines]
navs=zip(dirs,mags)

do={
    'N':lambda m: m*1j,
    'S':lambda m: m*-1j,
    'E':lambda m: m*1,
    'W':lambda m: -1*m,
    'F':lambda m: do[bearingfrominstr[pointing]](m),
    'R':lambda d: (pointing-d) % 360, #np.exp(1j*-np.deg2rad(d)),
    'L':lambda d: (pointing+d) % 360 #np.exp(1j*np.deg2rad(d))
}

bearingfrominstr={
    90:'N',
    270:'S',
    0:'E',
    180:'W'
}

pointing=0 # 'E'
print(f'Start pointing: {pointing} deg. ({bearingfrominstr[pointing]})')

total=0+0j
for instr, mag in navs:
    val = do[instr](mag)
    if instr=='R' or instr=='L':
        pointing = val
        # if pointing==360: pointing=0
        print(f'Nav: {instr}{mag} | New pointing: {pointing} deg. ({bearingfrominstr[pointing]})')
    else: 
        total += val
        print(f'Nav: {instr}{mag} | New total: {total}')

print(f'--> Part1: {np.abs(np.real(total))+np.abs(np.imag(total))}\n')





navs=zip(dirs,mags)


waypoint=10+1j
ship=0+0j

movewaypoint={
    'N':lambda m: m*1j,
    'S':lambda m: m*-1j,
    'E':lambda m: m*1,
    'W':lambda m: -1*m,
    'R':lambda d: np.exp(-1j*np.deg2rad(d)),
    'L':lambda d: np.exp(1j*np.deg2rad(d))
}

for instr, mag in navs:
    print(f'Nav: {instr}{mag}')
    print(f' | Ship: {ship}  | Waypoint: {waypoint}')
    if instr=='F':
        ship+=mag*waypoint
    elif instr in ['R','L']:
        waypoint*=movewaypoint[instr](mag)
    else:
        waypoint+=movewaypoint[instr](mag)
    print(f' | Ship: {ship}  | Waypoint: {waypoint}')

print(f'--> Part2: {np.abs(np.real(ship))+np.abs(np.imag(ship))}\n')
