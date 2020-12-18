
class Infix:
    def __init__(self, function):
        self.function = function
    def __ror__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))
    def __or__(self, other):
        return self.function(other)
    def __call__(self, value1, value2):
        return self.function(value1, value2)

plus=Infix(lambda x,y: x+y)
times=Infix(lambda x,y: x*y)


sump1=sump2=0
for line in open('day18-input.txt').read().splitlines():

    line=line.replace('*', '|times|').replace('+', '|plus|')
    sump1+=eval(line)

    line = line.replace("(","((").replace(")","))")
    line = line.replace( " |times| ", ") * (").replace('|plus|','+')
    line = "(" + line + ")"
    sump2 += eval(line)

print(f"Part1: {sump1}")
print(f"Part2: {sump2}")
