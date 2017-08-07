import functools

lines = [line.rstrip('\n') for line in open('triangle1.txt')]

triangle = []
for line in lines:
    triangle_layer = []
    values = line.split()
    triangle_layer = [int(v) for v in values]
    triangle.append(pyramid_layer)

@functools.lru_cache(maxsize=None)
def getmaxofsub(x, y):
    if y  == len(triangle) or x>y: return 0
    return triangle[y][x] + max(getmaxofsub(x, y+1), getmaxofsub(x+1, y+1))


print(getmaxofsub(0,0))