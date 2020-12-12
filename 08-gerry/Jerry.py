from copy import deepcopy
import Borders, Result

###############################################
#   Helper function to Create District Maps   #
#   Checks if there are any empty cells       #
#   in a district map                         #
###############################################
def scanForFirstUnassigned(currentMap):
  for i in range(len(currentMap)):
    for j in range(len(currentMap[i])):
      if currentMap[i][j] == 0:
        return [i,j]
  return [-1,-1]

###############################################
##    - createDistrict function  -           ##
##  use recursion to create the different    ##
##  possible district configurations for     ##
##  a 6x3 state with a district size of 3    ##
###############################################
def createDistrict(currentMap, allMaps, distNum):
  #starting from the top-left cell, we will go through all of the different
  # permutations of state configurations and save the ones that work in an array
  # which will be returned

  #first, scan for the first 0 (unassigned) cell scanning left-to-right & top-to-bottom
  location = scanForFirstUnassigned(currentMap)

  #if the location returned -1, then the map is full (no empty cells)
  if location[0] != -1:
    #Variation 1, check if the next unassigned cell can join a vertical district
    if (location[0] < len(currentMap)-2 
      and currentMap[location[0]+1][location[1]]==0 
      and currentMap[location[0]+2][location[1]]==0):
      mapV1 = deepcopy(currentMap)
      mapV1[location[0]][location[1]] = distNum
      mapV1[location[0]+1][location[1]] = distNum
      mapV1[location[0]+2][location[1]] = distNum
      #print('added v1', end=', ')
      createDistrict(mapV1, allMaps, distNum+1)
    
    #Variation 2, check if the next unassigned cell can join a horizontal district
    if (location[1] < len(currentMap[location[0]])-2 
      and currentMap[location[0]][location[1]+1]==0 
      and currentMap[location[0]][location[1]+2]==0):
      mapV2 = deepcopy(currentMap)
      mapV2[location[0]][location[1]] = distNum
      mapV2[location[0]][location[1]+1] = distNum
      mapV2[location[0]][location[1]+2] = distNum
      #print('added v2', end=', ')
      createDistrict(mapV2, allMaps, distNum+1)

    #Variation 3, check if the next unassigned cell can join a ┌ district
    if (location[0] < len(currentMap)-1 and location[1] < len(currentMap[location[0]])-1
      and currentMap[location[0]+1][location[1]]==0 
      and currentMap[location[0]][location[1]+1]==0
      and not (location[0]==len(currentMap)-2 and location[1]==len(currentMap[location[0]])-2)):
      mapV3 = deepcopy(currentMap)
      mapV3[location[0]][location[1]] = distNum
      mapV3[location[0]+1][location[1]] = distNum
      mapV3[location[0]][location[1]+1] = distNum
      #print('added v3', end=', ')
      createDistrict(mapV3, allMaps, distNum+1)

    #Variation 4, check if the next unassigned cell can join a ┐ district
    if (location[0] < len(currentMap)-1 and location[1] < len(currentMap[location[0]])-1
      and currentMap[location[0]][location[1]+1]==0 
      and currentMap[location[0]+1][location[1]+1]==0
      and not (location[0]==len(currentMap)-2 and location[1]==0)):
      mapV4 = deepcopy(currentMap)
      mapV4[location[0]][location[1]] = distNum
      mapV4[location[0]][location[1]+1] = distNum
      mapV4[location[0]+1][location[1]+1] = distNum
      #print('added v4', end=', ')
      createDistrict(mapV4, allMaps, distNum+1)

    #Variation 5, check if the next unassigned cell can join a ┘ district
    if (location[0] < len(currentMap)-1 and location[1] > 0
      and currentMap[location[0]+1][location[1]]==0 
      and currentMap[location[0]+1][location[1]-1]==0
      and not (location[0]==0 and location[1]==1)):
      mapV5 = deepcopy(currentMap)
      mapV5[location[0]][location[1]] = distNum
      mapV5[location[0]+1][location[1]] = distNum
      mapV5[location[0]+1][location[1]-1] = distNum
      #print('added v5', end=', ')
      createDistrict(mapV5, allMaps, distNum+1)

    #Variation 6, check if the next unassigned cell can join a L district
    if (location[0] < len(currentMap)-1 and location[1] < len(currentMap[location[0]])-1
      and currentMap[location[0]+1][location[1]]==0 
      and currentMap[location[0]+1][location[1]+1]==0
      and not (location[0]==0 and location[1]==len(currentMap[location[0]])-2)):
      mapV6 = deepcopy(currentMap)
      mapV6[location[0]][location[1]] = distNum
      mapV6[location[0]+1][location[1]] = distNum
      mapV6[location[0]+1][location[1]+1] = distNum
      #print('added v6', end=', ')
      createDistrict(mapV6, allMaps, distNum+1)

  else:
    allMaps.append(currentMap)
    #print('FOUND A MAP!')
###############################################
##    END of createDistrict function         ##
###############################################


################################################
##        - gerrymander function -            ##
##  returns an array of all possible district ##
##  variations sorted by how many districts   ##
##  were won by a given team for a given set  ##
##  of votes                                  ##
################################################
def gerrymander(votes, team):
  #create an array to store all the district variations
  #gerrymandered worlds will be stored by districts won
  multiverseResults = []
  #assume a square state with 3 cells per district and # of cells is divisible by 3
  numDist = int( len(votes) * len(votes[0]) / 3 )
  for i in range(numDist+1):
    multiverseResults.append([i])
  
  #create a state map with no districts
  noDistricts = []
  for i in range(len(votes)):
    blankRow = []
    for c in range(len(votes[0])):
      blankRow.append(0)
    noDistricts.append(blankRow)
  #create the infinite district variations
  allMaps = []
  createDistrict(noDistricts, allMaps, 1)
  '''
  for i in range(len(allMaps)):
    print('\n' + Borders.createDistrictBorders(votes, allMaps[i]))
  print("There are %d variations", len(allMaps)) ###there are 170 variations
  '''
  #analyze which party won in each district map variations
  for i in range(len(allMaps)):
    result = Result.checkWin(votes, allMaps[i])
    multiverseResults[result[len(result)-1][team]].append(allMaps[i])
  
  return multiverseResults, len(allMaps)
###############################################
##      END of gerrymander function          ##
###############################################
    
