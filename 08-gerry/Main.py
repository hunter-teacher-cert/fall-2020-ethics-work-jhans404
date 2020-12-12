Python 3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
import Borders, Result, Jerry

# Set the state size
ROWS = 6
COLS = 3
MAPSperROW = int(11/COLS)
NUMBERofDISTRICTS = int(ROWS * COLS / 3)

#####################################
##         Vote by cell            ##
#####################################
votes = []
if (False):
#create the state in a 2D array populated with random 1s and 0s
  for i in range(ROWS):
    row = []
    for j in range(COLS):
      row.append(random.randint(0,1))
    votes.append(row)
else:
#option to input vote results by hand
  votes.append([1,0,0])
  votes.append([0,1,0])
  votes.append([0,0,1])
  votes.append([0,1,0])
  votes.append([1,0,0])
  votes.append([0,1,0])

#####################################
##         Create Districs         ##
#####################################
districtMap = [];
if (True):
#simple distric map
  for i in range(1,ROWS+1):
    row = []
    for j in range(COLS):
      row.append(i)
    districtMap.append(row)
else:
#input districts by hand
  districtMap.append([1,1,2])
  districtMap.append([3,1,2])
  districtMap.append([3,4,2])
  districtMap.append([3,4,6])
  districtMap.append([5,4,6])
  districtMap.append([5,5,6])

'''
# Look at original district layout
print("\nDISTRICT MAP:")
for i in range(ROWS):
  print(districtMap[i])

# Check how every cell "voted"
print("\nVOTES BY REGION:")
for i in range(ROWS):
  print(votes[i])
'''
# Print votes with district borders
print("The votes with the original districts:")
print('\n' + Borders.createDistrictBorders(votes, districtMap))

results = Result.checkWin(votes, districtMap)
#print(results)
print("Popular Vote:")
print("Rep: \033[31m%.1f\033[0m%%,  Dem: \033[36m%.1f\033[0m%%" %(results[len(results)-2][0]*100/(ROWS*COLS), results[len(results)-2][1]*100/(ROWS*COLS)))

announce = ""
if results[len(results)-1][0] > results[len(results)-1][1]:
  announce += "\033[31;1;4mRepublicans Win!\033[0m"
elif results[len(results)-1][1] > results[len(results)-1][0]:
  announce += "\033[36;1;4mDeomcrats Win!\033[0m"
else:
  announce += "\033[32;1;4mIt's a tie!\033[0m"
print("\nBy District -", announce)
print("Reps won", Borders.addColor(results[len(results)-1][0],0), "district(s)")
print("Dems won", Borders.addColor(results[len(results)-1][1],1), "district(s)")

###################################################
#
#           DONE WITH INITIAL VOTING
#           NOW ANALYZE GERRYMANDERING OPTIONS
#
###################################################

gerry = input("\n\nWould you like to see if we can win with gerrymandering? (Y or N)  ").lower()

if (gerry == 'n'):
  print("\nYou're right. Better to leave that box closed.")
else:
  print("\n\tTsk tsk... we probably shouldn't, but here we go anyway...")
  team = int(input("\nWho are you rooting for? (0 or 1)  "))
  if team == 0:
    print("\n\tOK. Let's check if the Republicans can win.")
  elif team ==1:
    print("\n\tOK. Let's check if the Democrats can win.")
  else:
    print("\n\tOK. This isn't a bipartisan election?")
  multiverse, worlds = Jerry.gerrymander(votes, team)
  wins = -1
  while wins < NUMBERofDISTRICTS+1:
    print("\nNumber of plans in which " + Borders.addColor(team) + " wins...\t\tPercentage:")
    for i in range(len(multiverse)):
      wins = len(multiverse[i])-1
      if (i > (len(multiverse)-1)/2 and wins > 0):
        if wins > 999:
          print("  " + str(i) + " districts:\t" + Borders.addColor(wins,team) + "\t\t\t\t\t", end = "")
        else:
          print("  " + str(i) + " districts:\t" + Borders.addColor(wins,team) + "\t\t\t\t\t\t", end = "")
        if team == 0:
          print("\033[31m%.2f\033[0m%%" %(100*wins/worlds))
        else:
          print("\033[36m%.2f\033[0m%%" %(100*wins/worlds))
      else:
        if wins > 999:
          print("  " + str(i) + " districts:\t" + str(wins) + "\t\t\t\t\t", end = "")
        else:
          print("  " + str(i) + " districts:\t" + str(wins) + "\t\t\t\t\t\t", end = "")
        print("%.2f%%" %(100*wins/worlds))
    
    wins = int(input("\nEnter a number 0-" + str(NUMBERofDISTRICTS) + " to see district layouts with those number of wins.\n(or enter a number greater than " + str(NUMBERofDISTRICTS) + " to exit):  "))
    if (0 <= wins <= NUMBERofDISTRICTS and len(multiverse[wins]) > 1):
      #MAPSperROW = int(input("How many maps would you like printed per row? "))
      Borders.printMaps(MAPSperROW, votes, multiverse[wins])
      print("\tThese are all " + str(len(multiverse[wins])-1) + " district layouts where party " + Borders.addColor(team) + " wins " + str(wins) + " districts.")
    elif (0 <= wins <= NUMBERofDISTRICTS and len(multiverse[wins]) == 1):
      print("\tThere are no district maps where " + Borders.addColor(team) + " wins " + str(wins) + " districts.")