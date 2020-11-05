import random

def printCity(map):
  for row in range(len(map)):
    printRow = ""
    for col in range(len(map[row])):
      if map[row][col] == 0:
        printRow += "\u001b[31m[ " + str(map[row][col]) + " ]  "
      else:
        printRow += "\u001b[34m[ " + str(map[row][col]) + " ]  "
    print(printRow)


def fillMap(r, c):
  map = []

  for i in range(r):
    row = []
    for j in range(c):
      row.append(demOrRepub())
    map.append(row)
  return map


def demOrRepub():
  val = random.randint(0, 1)
  #print(val)
  return val


#rows, cols = (3, 6)
#metropolis = [[0]*cols]*rows
#metropolis = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]

rows = 6
cols = 3
metropolis = fillMap(rows, cols)

printCity(metropolis)
