Python 3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def checkWin(vote, map):
  count = []  # count the results from each district stored by row
  numDist = int( len(vote) * len(vote[0]) / 3 )
  for i in range(numDist+2): # last 2 rows are to record results
    row = []
    for j in range(2+1): # 2 parties plues an extra column to record district result
      row.append(0)
    count.append(row)
  for i in range(len(map)):
    for j in range(len(map[i])):
      count[map[i][j]-1][vote[i][j]] += 1
  # 2nd to last row will contain the total votes
  # last row  will contain the district wins
  # col 2 indicates who won that district (in a 2 party system)
  sum0 = 0
  sum1 = 0
  win0 = 0
  win1 = 0
  for i in range(numDist):
    sum0 += count[i][0]
    sum1 += count[i][1]
    if count[i][0] > count[i][1]:
      count[i][2] = 0
      win0 += 1
    elif count[i][1] > count[i][0]:
      count[i][2] = 1
      win1 += 1
    else:
      count[i][2]=-1
  count[numDist][0] = sum0  #total votes for 0
  count[numDist][1] = sum1  #total votes for 1
  count[numDist+1][0] = win0  #district wins for 0
  count[numDist+1][1] = win1  #district wins for 1
  return count