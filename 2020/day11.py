import numpy as np

lines=[line.replace('\n','') for line in open('day11-input.txt').readlines()]
waitingarea = np.empty( (len(lines), len(lines[0])), dtype=str)
for y in range(waitingarea.shape[0]):
    for x in range(waitingarea.shape[1]):
        waitingarea[y,x]=lines[y][x]



def get_thing(row,col,waitingarea):
    seat=waitingarea[row,col]
    if seat=='.':
        return '.'

    if col-1<0: startcol=0
    else: startcol=col-1

    if col+2>waitingarea.shape[1]-1: endcol=waitingarea.shape[1]
    else: endcol=col+2

    if row-1<0: startrow=0
    else: startrow=row-1

    if row+2>waitingarea.shape[0]-1: endrow=waitingarea.shape[0]
    else: endrow=row+2

    count=np.count_nonzero(waitingarea[startrow:endrow,startcol:endcol]=='#')
    
    if seat=='L' and count == 0:
        return '#'
    if seat=='#' and count > 4:
        return 'L'
    else:
        return seat

def get_thing2(x,y,waitingarea):
    maxy=waitingarea.shape[0]-1
    maxx=waitingarea.shape[1]-1

    seat=waitingarea[y,x]
    if seat=='.':
        return '.'

    count=0

    directions=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    checkx,checky=0,0
    for xstep,ystep in directions:

            checkx=x+xstep
            checky=y+ystep
            while checkx>=0 and checkx<=maxx and checky>=0 and checky<=maxy:
                if waitingarea[checky,checkx]=='#':
                    count+=1
                    break
                elif waitingarea[checky, checkx]=='L':
                    break
                else:
                    checkx+=xstep
                    checky+=ystep
    if seat=='L' and count == 0:
        return '#'
    if seat=='#' and count >= 5:
        return 'L'
    else:
        return seat

beforecount=-1
endcount=np.count_nonzero(waitingarea=='#')
while beforecount != endcount:
    beforecount=endcount
    AFTERwaitingarea=np.empty_like(waitingarea)
    for ix,iy in np.ndindex(waitingarea.shape):
        AFTERwaitingarea[ix,iy] = get_thing(ix,iy,waitingarea)

    endcount=np.count_nonzero(AFTERwaitingarea=='#')
    waitingarea=AFTERwaitingarea

print(f'Part1: {endcount}')




waitingarea = np.empty( (len(lines), len(lines[0])), dtype=str)
for y in range(waitingarea.shape[0]):
    for x in range(waitingarea.shape[1]):
        waitingarea[y,x]=lines[y][x]


while True:
    AFTERwaitingarea=np.empty_like(waitingarea)
    for iy,ix in np.ndindex(waitingarea.shape):
        AFTERwaitingarea[iy,ix] = get_thing2(x=ix,y=iy,waitingarea=waitingarea)
    if (waitingarea==AFTERwaitingarea).all():
        break
    waitingarea=AFTERwaitingarea



print(f"Part2: {np.count_nonzero(AFTERwaitingarea=='#')}")

