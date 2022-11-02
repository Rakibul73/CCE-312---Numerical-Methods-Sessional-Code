
def showMatrix():
    print("\n")
    for i in sd:
        for j in i:
            print(j, end="\t\t")
        print("\n")


def getone(pp):
    for i in range(len(sd[0])):
        if sd[pp][pp] != 1:
            q00 = sd[pp][pp]

            for j in range(len(sd[0])):
                sd[pp][j] = sd[pp][j] / q00


def getzero(r, c):
    for i in range(len(sd[0])):
        if sd[r][c] != 0:
            q04 = sd[r][c]
    
            for j in range(len(sd[0])):
                sd[r][j] = sd[r][j] - ((q04) * sd[c][j])


# 3 x 3
sd = [
    [2, -6, -1, -38],
    [-3, -1, 7, -34],
    [-8, 1, -2, -20]
]
showMatrix()

for i in range(len(sd)):
    getone(i)

    for j in range(len(sd)):
        if i != j:
            getzero(j, i)

showMatrix()