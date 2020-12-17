import numpy as np

lines=open('day17-input.txt').read().splitlines()

inputgrid=np.zeros((len(lines),len(lines[0])),dtype=int)
for y,line in enumerate(lines):
    for x,char in enumerate(line):
        if char == '#': inputgrid[y,x]=1 

if len(lines)%2==0:
    # if input is even side length
    maxinputgriddim=20
    middleindex=maxinputgriddim//2 # actually one below middle but w/e
    inputwidth=inputgrid.shape[0]
    grid=np.zeros((maxinputgriddim,maxinputgriddim,maxinputgriddim),dtype=int)
    grid[middleindex,(maxinputgriddim-inputwidth)//2:(maxinputgriddim-inputwidth)//2+inputwidth,(maxinputgriddim-inputwidth)//2:(maxinputgriddim-inputwidth)//2+inputwidth]=inputgrid
else:
    # if input is odd side length
    maxinputgriddim=15 # must be odd
    middleindex=(maxinputgriddim-1)//2
    inputwidth=inputgrid.shape[0]-1 # zero indexing
    grid=np.zeros((maxinputgriddim,maxinputgriddim,maxinputgriddim), dtype=int)
    grid[middleindex,int(middleindex-inputwidth//2):int(middleindex+inputwidth//2+1),int(middleindex-inputwidth//2):int(middleindex+inputwidth//2+1)]=inputgrid



def processindex(zi,yi,xi, grid):
    
    x1=0 if xi-1<0 else xi-1
    x2=grid.shape[2] if xi+1==grid.shape[2] else xi+2

    y1=0 if yi-1<0 else yi-1
    y2=grid.shape[1] if yi+1==grid.shape[1] else yi+2

    z1=0 if zi-1<0 else zi-1
    z2=grid.shape[0] if zi+1==grid.shape[0] else zi+2

    if grid[zi,yi,xi]==1 and (xi-1<0 or yi-1<0 or zi-1<0 or xi+1==grid.shape[2] or yi+1==grid.shape[1] or zi+1==grid.shape[0]):
        raise IndexError("Increase maxinputgriddim")

    count=np.count_nonzero(grid[z1:z2,y1:y2,x1:x2])

    if grid[zi,yi,xi]==1 and (count == 3 or count==4):
        return 1
    elif grid[zi,yi,xi]==0 and count == 3:
        return 1
    else:
        return 0


cycle=0
while cycle<6:
    AFTERgrid=np.empty_like(grid)
    count=0
    for z,y,x in np.ndindex(grid.shape):
        AFTERgrid[z,y,x]=processindex(z,y,x,grid)
        count +=1
    grid=AFTERgrid
    cycle += 1

print(f"Part1: {np.count_nonzero(grid)}")






# Into 4D land we go

if len(lines)%2==0:
    # if input is even side length
    grid=np.zeros((maxinputgriddim,maxinputgriddim,maxinputgriddim,maxinputgriddim),dtype=int)
    grid[middleindex,middleindex,(maxinputgriddim-inputwidth)//2:(maxinputgriddim-inputwidth)//2+inputwidth,(maxinputgriddim-inputwidth)//2:(maxinputgriddim-inputwidth)//2+inputwidth]=inputgrid
else:
    # if input is odd side length
    grid=np.zeros((maxinputgriddim,maxinputgriddim,maxinputgriddim,maxinputgriddim), dtype=int)
    grid[middleindex,middleindex,int(middleindex-inputwidth//2):int(middleindex+inputwidth//2+1),int(middleindex-inputwidth//2):int(middleindex+inputwidth//2+1)]=inputgrid



def processindex4D(wi,zi,yi,xi, grid):
    
    x1=0 if xi-1<0 else xi-1
    x2=grid.shape[3] if xi+1==grid.shape[3] else xi+2

    y1=0 if yi-1<0 else yi-1
    y2=grid.shape[2] if yi+1==grid.shape[2] else yi+2

    z1=0 if zi-1<0 else zi-1
    z2=grid.shape[1] if zi+1==grid.shape[1] else zi+2

    w1=0 if wi-1<0 else wi-1
    w2=grid.shape[0] if wi+1==grid.shape[0] else wi+2

    if grid[wi,zi,yi,xi]==1 and (xi-1<0 or yi-1<0 or zi-1<0 or wi-1<0 or xi+1==grid.shape[3] or yi+1==grid.shape[2] or zi+1==grid.shape[1] or wi+1==grid.shape[0]):
        raise IndexError("Increase maxinputgriddim")

    count=np.count_nonzero(grid[w1:w2,z1:z2,y1:y2,x1:x2])

    if grid[wi,zi,yi,xi]==1 and (count == 3 or count==4):
        return 1
    elif grid[wi,zi,yi,xi]==0 and count == 3:
        return 1
    else:
        return 0

cycle=0
while cycle<6:
    AFTERgrid=np.empty_like(grid)
    count=0
    for w,z,y,x in np.ndindex(grid.shape):
        AFTERgrid[w,z,y,x]=processindex4D(w,z,y,x,grid)
        count +=1
    grid=AFTERgrid
    cycle += 1

print(f"Part2: {np.count_nonzero(grid)}")



