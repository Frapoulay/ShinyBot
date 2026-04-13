from modules.cell import CELL_COST, SOLID_BLOCKS
from modules.ramp import Ramp
from modules.zone import Position
from modules.emu import BIZHAWK, PLATINE
import modules.zone as zone

# Credits for A* algorithm implementation :
# - Python Implementation : https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
# - Improving Heuristics calculation : https://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html

PUZZLE_BOULDERS = [
    (Position(25,16,zone.MONTABRUPT_SALLE1), Position(26,16,zone.MONTABRUPT_SALLE1)),
    (Position(6,31,zone.ROUTEVICTOIRE_SALLEOUEST), Position(6,32,zone.ROUTEVICTOIRE_SALLEOUEST)),
    (Position(18,42,zone.MONTCOURONNE_PASSAGEVESTIGION), Position(18,43,zone.MONTCOURONNE_PASSAGEVESTIGION))
]

PLAYER_POSITION = 0
BOULDER_POSITION = 1

DIRECTIONS = [
    {"orientation": (-1, 0), "solidLedges": ["D","L","R"]}, # Up
    {"orientation": (0, -1), "solidLedges": ["D","U","R"]}, # Left
    {"orientation": (0, 1),  "solidLedges": ["D","L","U"]}, # Right
    {"orientation": (1, 0),  "solidLedges": ["L","U","R"]}, # Down
]

##################################################################################################
#                                                                                                #
#     Methods responsible of using A* algorithm to find the best path between two positions      #
#                                                                                                #
##################################################################################################

#################################
# Node class for A* Pathfinding #
#################################

class Node():
    def __init__(self, position: Position, zoneMap, parent = None):
        self.parent = parent
        self.position = position
        self.cellType = zoneMap[position.Y][position.X]

        # Special status
        self.noBikeCell = self.cellType in ["W","w","S","s","m","M","g","1","2","3","4"]
        self.waterCell = self.cellType in ["W","w","d"]
        self.encounterCell = self.cellType in ["W","G","g","m","M"]

        # A* core parameters
        self.g = 0
        self.h = 0
        self.f = 0

        self.pushBoulder = False
        self.isSurfing = self.waterCell
        
        self.onABikeSlope = False
        self.bikeSlopeDestination = None
        self.bikeSlopeMomentumCell = None

        self.rampData: Ramp|None = None

        ### Special process for bridges since two above/below cells share the same X,Y position, see solid blocks processing ###
        # We avoid starting on a bridge, so on starting node we consider we're below (except on a @ cell which is impossible)
        if (not parent):
            self.isBelow = self.cellType in ["B","d","A","a"] 
            self.isAbove = self.cellType in ["@"]

        # If you were below a bridge, you're leaving when not on Above or Below cell
        elif (parent.isBelow):
            
            self.isBelow = self.cellType in ["A","a","@","B","d"]
            self.isAbove = False

            # Can only start/stop surfing through B and d cells
            if (self.cellType == "d" and parent.cellType == "B"):
                self.isSurfing = True
            elif (self.cellType == "B" and parent.cellType == "d"):
                self.isSurfing = False
            else:
                self.isSurfing = parent.isSurfing
        
        # If you were not, above/below condition just depends on current cell value
        else:
            self.isBelow = self.cellType in ["B","d"]
            self.isAbove = self.cellType in ["A","a","@"]

    def canBike(self):
        return (self.position.zone.canBike and not self.noBikeCell and not self.isSurfing)

    def getNodeKey(self):
        return (self.position.X, self.position.Y, self.isAbove)

    # Two nodes may share the same position but be above or below a bridge, so we must check those conditions as well
    def __eq__(self, other):
        if isinstance(other, Node):
            return self.position == other.position and self.isBelow == other.isBelow and self.isAbove == other.isAbove
        return False

    def __str__(self):
        return (str(self.position) + " - " + self.cellType 
            + (" is below" if self.isBelow else " is not below")
            + (" and is above !" if self.isAbove else " and is not above !")
            + (" (parent = (" + str(self.parent.position.X) + "," + str(self.parent.position.Y) + "))" if self.parent else "")
            + (" PUSH !" if self.pushBoulder else "")
            + (" SURF !" if self.isSurfing else "")
            + (" ON A SLOPE !" + (" (destination = " + str(self.bikeSlopeDestination) + ")" if self.bikeSlopeDestination else "") if self.onABikeSlope else "")
            + (" ON A RAMP ! (destination = " + str(self.rampData.destinationCell) + ")" if self.rampData else "")
            + "\n")

    def __repr__(self):
        return str(self)



#########################################################################################################
# Find best possible path between two points in the same zone, while trying to push boulders if needeed #
#########################################################################################################
def getMostEfficientPath(start: Position, end: Position, gameName, repelActive = False, zoneMap = None, isBelow = None, maxCost = None):

    # Default : if not provided, zone map is end position zone map
    if (zoneMap is None):
        zoneMap = end.zone.map

    # A* algorithm only works for positions in the same zone
    if (start.zone != end.zone):
        return None
    
    # Make sure the location is reachable
    if (not zone.checkPositionValidity(start, zoneMap) or not zone.checkPositionValidity(end, zoneMap)):
        return None

    # Boulders might block the way, we'll track them and process them if needed
    possiblePath, blockingBoulders = astarAlgorithm(start, end, gameName, repelActive, zoneMap, isBelow, maxCost)

    # No path found, checking for boulders
    if (not possiblePath and len(blockingBoulders) > 0):

        # First try to check if pushing the boulders is actually worth it
        boulderFreeMap = removeAllBoulders(zoneMap)

        # No point in pushing boulders if no path can be found on a boulder-free map
        if (not astarAlgorithm(start, end, gameName, repelActive, boulderFreeMap, isBelow, maxCost)[0]):
            return None

        # Push the boulders close to endPosition first
        blockingBoulders = sortBoulders(blockingBoulders, end)
        playerPosition = blockingBoulders[0][PLAYER_POSITION]
        boulderPosition = blockingBoulders[0][BOULDER_POSITION]
        bouldersToPush = [(playerPosition, boulderPosition)]

        # Operations will depend on the player and boulders positions
        xDiff = boulderPosition.X - playerPosition.X
        yDiff = boulderPosition.Y - playerPosition.Y

        # Create a copy of the map since we'll edit it
        newMap = zoneMap[:]

        # Try to push the boulder all the way
        while True:

            # Push the boulder in the direction the player is facing
            updatedBoulder = Position(boulderPosition.X + xDiff, boulderPosition.Y + yDiff, boulderPosition.zone)
            updatedPlayer = Position(playerPosition.X + xDiff, playerPosition.Y + yDiff, playerPosition.zone)

            # Update the map to take into account the pushed boulder
            updateMapWithPushedBoulders(newMap, boulderPosition, playerPosition)

            # Try to find a way now that the boulder has been pushed
            possiblePath, newBlockingBoulders = astarAlgorithm(playerPosition, end, gameName, repelActive, newMap, maxCost = maxCost)

            # A path has been found, return it
            if (possiblePath):

                # Create a new map and update it everytime a boulder is pushed
                newMap = zoneMap[:]

                # Create a path that goes from start to end while pushing all boulders in bouldersToPush
                boulderPath = [Node(start, newMap)]
                previousPosition = start

                for boulder in bouldersToPush:
 
                    # Go from previous position to boulder pushing position
                    pathToPlayerPosition = astarAlgorithm(previousPosition, boulder[PLAYER_POSITION], gameName, repelActive, newMap, maxCost = maxCost, parentNode = boulderPath[-1])[0]
                    lastNode = pathToPlayerPosition[-1]

                    # Remove start node to link it to the previous path
                    pathToPlayerPosition.pop(0)
                    
                    # Go from boulder pushing position to boulder position while pushing it
                    pushingBoulder = Node(boulder[BOULDER_POSITION], newMap, lastNode)
                    pushingBoulder.pushBoulder = True
                    pushingBoulder.g = lastNode.g + CELL_COST["O"]
                    pathToPlayerPosition.append(pushingBoulder)

                    # Update the map to take into account the pushed boulder
                    updateMapWithPushedBoulders(newMap, boulder[BOULDER_POSITION], boulder[PLAYER_POSITION])

                    # Link subpath to global path
                    boulderPath.extend(pathToPlayerPosition)
                    previousPosition = boulder[BOULDER_POSITION]

                # Go from last boulder to end, remove last boulder node to link it to the previous path
                pathToEnd = astarAlgorithm(previousPosition, end, gameName, repelActive, newMap, maxCost = maxCost, parentNode = boulderPath[-1])[0]
                pathToEnd.pop(0)
                boulderPath.extend(pathToEnd)

                # Return complete path
                return boulderPath

            # No path has been found but boulder can still be pushed, keep trying
            elif ((updatedPlayer, updatedBoulder) in newBlockingBoulders):
                playerPosition = updatedPlayer
                boulderPosition = updatedBoulder
                bouldersToPush.append((playerPosition, boulderPosition))

            # Boulder has been pushed all the way and still no path found
            # Try another boulder but keep the same map
            elif (len(newBlockingBoulders) > 0):

                # Push the boulders close to endPosition first
                newBlockingBoulders = sortBoulders(newBlockingBoulders, end)
                playerPosition = newBlockingBoulders[0][PLAYER_POSITION]
                boulderPosition = newBlockingBoulders[0][BOULDER_POSITION]
                bouldersToPush.append((playerPosition, boulderPosition))

                xDiff = boulderPosition.X - playerPosition.X
                yDiff = boulderPosition.Y - playerPosition.Y

            # No boulder left to push and no path found
            else:
                return None
    else:
        return possiblePath



#######################################################################################
# Use A* algorithm to find most efficient path between two positions in the same zone #
#######################################################################################
def astarAlgorithm(start: Position, end: Position, gameName, repelActive, zoneMap, isBelow = None, maxCost = None, parentNode: Node = None):

    # Boulders might block the way, we'll track them and process them if needed
    blockingBoulders = []

    # Create start and end node
    start_node = Node(start, zoneMap)
    end_node = Node(end, zoneMap)

    # If extending an existing path, retrieve its cost
    if (parentNode):
        start_node.g = parentNode.g

    # If provided, add isBelow and isAbove status (help to differentiate if starting on a a/A cell) 
    if (isBelow is not None):
        start_node.isBelow = isBelow
        start_node.isAbove = not isBelow

    # Initialize both open and closed list
    open_dict = {}
    closed_dict = {}

    # Add the start node
    open_dict[start_node.getNodeKey()] = start_node

    # Loop until you find the end
    while len(open_dict) > 0:

        # Get the node with most efficient path
        current_key = next(iter(open_dict))
        current_node = open_dict[current_key]

        for key, item in open_dict.items():
            if item.f < current_node.f:
                current_node = item
                current_key = key

        # Pop the node off open list, add to closed list
        open_dict.pop(current_key)
        closed_dict[current_key] = current_node

        # Found the goal
        if current_node.position == end_node.position:
            path = []
            current = current_node

            # Retrace back the complete path
            while current is not None:

                # Add nodes following a specific path for bike slopes or ramps
                if (current.bikeSlopeDestination and current.bikeSlopeDestination == path[-1].position):
                    path.extend(generateSlopeNodePath(current, path[-1], zoneMap))

                elif (current.rampData and not current.rampData.processed):
                    path.extend(generateRampNodePath(current, gameName, repelActive, zoneMap, isBelow, maxCost))

                # Regular node processing
                else:  
                    path.append(current)
                
                current = current.parent

            # Return reversed path
            return path[::-1], []
        
        # Generate children
        children = []
        for new_position in DIRECTIONS: # Adjacent squares

            # Get node position
            node_position = Position(current_node.position.X + new_position["orientation"][1],
                                     current_node.position.Y + new_position["orientation"][0],
                                     current_node.position.zone)
            
            nextCellValue = zoneMap[node_position.Y][node_position.X]
            topCellValue = zoneMap[node_position.Y - 1][node_position.X]
            highSpeedRamp = None

            # Can't walk through solid blocks
            if nextCellValue in SOLID_BLOCKS + new_position["solidLedges"]:

                # If the solid block is a boulder and the cell after that is a free cell, we can try pushing the boulder
                if (nextCellValue == "b" and isBoulderPushable(zoneMap,current_node.position,node_position,new_position["orientation"],blockingBoulders)):
                    blockingBoulders.append((current_node.position, node_position))

                # If the solid block is a bike ramp, we might be able to jump up
                if (nextCellValue in ["<",">"]):

                    # Can only jump left-oriented ramp from the right and vice-versa
                    if (new_position["orientation"] == (1,0) or new_position["orientation"] == (-1,0)
                        or new_position["orientation"] == (0,1) and nextCellValue == ">"
                        or new_position["orientation"] == (0,-1) and nextCellValue == "<"):
                        continue

                    # Find high-speed destination cell (up to 4 cells left or right)
                    highSpeedRamp = Ramp(node_position, nextCellValue, isHighSpeed = True)
                    highSpeedRamp.findMomentumCell(zoneMap)

                    # Try the low-speed bike to see if it unlocks an alternative path
                    lowSpeedRamp = Ramp(node_position, nextCellValue, isHighSpeed = False)
                    lowSpeedRamp.findMomentumCell(zoneMap)

                    # If we can jump up the ramp with high speed, find destination cell and set it as child position
                    if (highSpeedRamp.momentumCell):
                        highSpeedRamp.findDestinationCell(zoneMap)

                        node_position = highSpeedRamp.destinationCell
                        nextCellValue = zoneMap[node_position.Y][node_position.X]
                        topCellValue = zoneMap[node_position.Y - 1][node_position.X]

                    # Add low-speed bike destination cell (1 cell left or right) as additional child
                    if (lowSpeedRamp.momentumCell):
                        lowSpeedRamp.findDestinationCell(zoneMap)

                        lowSpeedNode = Node(lowSpeedRamp.destinationCell, zoneMap, current_node)
                        lowSpeedNode.rampData = lowSpeedRamp
                        children.append(lowSpeedNode)

                # Default : don't take the node
                else:
                    continue

            # If on a bridge, don't go on Below cells
            if (current_node.isAbove and nextCellValue in ["B","d"]):
                continue

            # If under a bridge
            if (current_node.isBelow):

                # Only leave by passing on a Below cell (d if surfing, B if not)
                if (current_node.cellType in ["a","A"] and nextCellValue not in ["a","A",("d" if current_node.isSurfing else "B")]):
                    continue

                # Don't go on blocked below cells
                if (current_node.cellType in ["B","d"] and nextCellValue == "@"):
                    continue

            # Don't go up if a post is just above since it triggers a dialogue
            if (topCellValue == "P" and new_position["orientation"] == (-1, 0)):
                continue
            
            # Go up the slope, teleport up to three cells after the slope
            if (nextCellValue == "V" and new_position["orientation"] == (-1, 0)):

                # Search for specific cells needed to go up the slope
                current_node.bikeSlopeDestination = findSlopeDestinationCell(node_position)
                current_node.bikeSlopeMomentumCell = findSlopeMomentumCell(node_position)
                node_position = current_node.bikeSlopeDestination

            # Rock Climb : teleport to position after climbing
            if (current_node.cellType == "C" and nextCellValue == "C"):
                node_position = getRockClimbEndPosition(zoneMap, current_node.position, new_position["orientation"])

            # We can walk through the block : add node to the children list
            new_node = Node(node_position, zoneMap, current_node)
            new_node.rampData = highSpeedRamp
            children.append(new_node)

        # Loop through children
        for child in children:

            # Create the NodeKey item to read inside the closed and open dictionnaries
            childNodeKey = child.getNodeKey()

            # Child is already in the closed_dict : don't process it
            if childNodeKey in closed_dict:
                continue

            # Default cell cost is 999, basically solid block
            cellCost = CELL_COST.get(child.cellType, 999)

            # Override cost if jumping from a ramp
            if (child.rampData):
                cellCost = 10 if child.rampData.isHighSpeed else 5

            # Surfing is twice as slow in Diamond/Pearl
            if (child.cellType in ["W","d"] and gameName != PLATINE):
                cellCost *= 2

            # If surfing, reduce water cells cost and increase the rest
            if (child.parent.isSurfing):
                cellCost += (4 if not child.waterCell else -2)
            
            # If repel is active, reduce encounter cells cost
            if (repelActive):
                cellCost -= (2 if child.encounterCell else 0)

            # If biking is possible, increase non-bike cells cost when on a bike cell, and vice-versa
            if (start.zone.canBike):
                if (child.parent.noBikeCell):
                    cellCost += (2 if child.cellType in ["O","G"] else 0)
                else:
                    cellCost += (2 if child.noBikeCell else 0)

            # If going down a bike rope, reduce cell cost
            if (child.cellType == "V" and child.position.Y > child.parent.position.Y):
                cellCost -= 4

            # Don't add nodes that go above maxCost if provided
            if (maxCost is not None and current_node.g + cellCost > maxCost):
                continue

            # Create the f, g, and h values (see A* algorith processing for more details)
            child.g = current_node.g + cellCost
            child.h = abs(child.position.Y - end_node.position.Y) + abs(child.position.X - end_node.position.X) # Manhattan distance
            child.f = child.g + child.h

            # Child is already in the open list and a similar or better path exists : don't process it
            if childNodeKey in open_dict:
                existing_node = open_dict[childNodeKey]
                if child.g >= existing_node.g:
                    continue

            # Add the child to the open list
            open_dict[childNodeKey] = child

    # We reached the end of the loop so no path has been found, maybe boulders are blocking the way
    return None, blockingBoulders



#########################################################################
#                                                                       #
#     Methods responsible of dealing with obstacles in A* algorithm     #
#                                                                       #
#########################################################################

#####################################################################################
# Retrieve every pushed boulder from processed nodes and update the map accordingly #
#####################################################################################
def getMapAtCurrentState(processedNodes, originalMap):

    # Keep track of obstacles for the input process
    destroyedObstacles = []

    # Create a copy of the original map that we can update
    updatedMap = originalMap[:]

    # Check every already processed node for pushed boulders
    if (len(processedNodes) > 0):

        # If a boulder has been pushed, update the map accordingly
        for node in processedNodes:
            if (node.pushBoulder): 
                updateMapWithPushedBoulders(updatedMap, node.position, node.parent.position)

            if (node.cellType in ["r","t"]):
                destroyedObstacles.append(node.position)

    return updatedMap, destroyedObstacles


#########################################################
# Update boulder position on the map after being pushed #
#########################################################
def updateMapWithPushedBoulders(zoneMap, boulderPosition, playerPosition):
        
    # Operations will depend on the player and boulders positions
    xDiff = boulderPosition.X - playerPosition.X
    yDiff = boulderPosition.Y - playerPosition.Y

    # Update the map to take into account the pushed boulder
    if (xDiff == 1):
        zoneMap[boulderPosition.Y] = zoneMap[boulderPosition.Y][:boulderPosition.X] + "Ob" + zoneMap[boulderPosition.Y][boulderPosition.X+2:]
    elif (xDiff == -1):
        zoneMap[boulderPosition.Y] = zoneMap[boulderPosition.Y][:boulderPosition.X-1] + "bO" + zoneMap[boulderPosition.Y][boulderPosition.X+1:]
    else:
        zoneMap[boulderPosition.Y] = zoneMap[boulderPosition.Y][:boulderPosition.X] + "O" + zoneMap[boulderPosition.Y][boulderPosition.X+1:]
        zoneMap[boulderPosition.Y + yDiff] = zoneMap[boulderPosition.Y + yDiff][:boulderPosition.X] + "b" + zoneMap[boulderPosition.Y + yDiff][boulderPosition.X+1:]


################################################
# Sort boulder list by distance to destination #
################################################
def sortBoulders(boulderList, endPosition):

    # Calculate boulder distance to endPosition
    for boulder in boulderList:
        boulder[1].setDistanceTo(endPosition)

    # Sort by distance to endPosition
    sortedList = sorted(boulderList, key=lambda x: x[1].distance)

    # Specific process for particular boulders that need to be pushed last
    for boulder in PUZZLE_BOULDERS:
        if (boulder in sortedList):
            sortedList.remove(boulder)
            sortedList.append(boulder)

    return sortedList


#############################################################################################################
# Boulder is pushable if the cell after that is an empty one, and the boulder hasn't already been processed #
#############################################################################################################
def isBoulderPushable(zoneMap, playerPosition, boulderPosition, orientation, blockingBoulders):
    return (zoneMap[boulderPosition.Y + orientation[0]][boulderPosition.X + orientation[1]] == "O" 
                and (playerPosition, boulderPosition) not in blockingBoulders)


###################################################
# Replace all boulders with free cells on the map #
###################################################
def removeAllBoulders(zoneMap):
    return [row.replace('b', 'O') for row in zoneMap]


#############################################
# Get final position after using Rock Climb #
#############################################
def getRockClimbEndPosition(zoneMap, playerPosition, orientation):
    
    # Try to find the first cell after rock climb
    for i in range(1,11):

        # Found the end position of rock climb
        if (zoneMap[playerPosition.Y + i*orientation[0]][playerPosition.X + i*orientation[1]] != "C"):
            return Position(playerPosition.X + i*orientation[1], playerPosition.Y + i*orientation[0], playerPosition.zone)
        
    # No position has been found after 10 cells, not theoretically possible
    return playerPosition


##################################################
# Get final position after going up a bike slope #
##################################################
def findSlopeDestinationCell(slopePosition):
    # Check for the furthest free cell up the slope 
    if (slopePosition.zone.map[slopePosition.Y - 3][slopePosition.X] in SOLID_BLOCKS):
        return Position(slopePosition.X, slopePosition.Y - 2, slopePosition.zone)
    elif (slopePosition.zone.map[slopePosition.Y - 4][slopePosition.X] in SOLID_BLOCKS):
        return Position(slopePosition.X, slopePosition.Y - 3, slopePosition.zone)
    else:
        return Position(slopePosition.X, slopePosition.Y - 4, slopePosition.zone)


################################################################################
# Find cell needed to be reached to gain momentum before going up a bike slope #
################################################################################
def findSlopeMomentumCell(slopePosition):
    zoneMap = slopePosition.zone.map

    # Search for a close free cell to gain momentum in order to go up the slope
    for orientation in [(1,0),(0,-1),(0,1)]: # Down, Left, Right
        if (zoneMap[slopePosition.Y + 1 + orientation[0]][slopePosition.X + orientation[1]] in ["O","G","B"]):
            return Position(slopePosition.X + orientation[1], slopePosition.Y + 1 + orientation[0], slopePosition.zone)


####################################################
# Generate every node needed to go up a bike slope #
####################################################
def generateSlopeNodePath(slopeNode, destinationNode, zoneMap):

    slopePath = []
    slopePath.append(slopeNode)
    slopePath.append(Node(slopeNode.bikeSlopeMomentumCell, zoneMap, slopePath[-1])) # Momentum Cell
    slopePath.append(Node(slopeNode.position, zoneMap, slopePath[-1])) # Cell in front of the slope
    
    slopeDestinationId = 1

    # Add nodes until we're at the top
    while (destinationNode.position.Y < slopeNode.position.Y - slopeDestinationId):
        slopePath.append(Node(Position(slopeNode.position.X, slopeNode.position.Y - slopeDestinationId, slopeNode.position.zone), zoneMap, slopePath[-1]))
        slopeDestinationId += 1

    for node in slopePath:
        node.onABikeSlope = True

    destinationNode.onABikeSlope = True
    destinationNode.parent = slopePath[-1]

    return slopePath[::-1]



#########################################
# Link a node path to another node path #
#########################################
def addToNodePath(mainPath: list[Node], additionalPath: list[Node], pathCost = CELL_COST["O"]):

    # Iterate on each node and link it to previous nodes with parent/g attributes
    for newNode in additionalPath:
        if (mainPath):
            mainPath[-1].parent = newNode
            mainPath[-1].g = newNode.g + pathCost
        mainPath.append(newNode)



#######################################################
# Generate every node needed to jump from a bike ramp #
#######################################################
def generateRampNodePath(destinationNode: Node, gameName, repelActive, zoneMap, isBelow, maxCost):
    rampData = destinationNode.rampData
    rampData.processed = True
    startingPosition = Position(rampData.position.X - rampData.orientation, rampData.position.Y, rampData.position.zone)

    # High-speed bike : go back and forth from start to momentum cell to gain momentum
    if (rampData.isHighSpeed):
        rampPath = astarAlgorithm(startingPosition, rampData.momentumCell, gameName, repelActive, zoneMap, isBelow, maxCost, destinationNode)[0]
        startingNode = rampPath.pop(0) # Remove starting position from ramp node path since it was already included in the global path

        # Final node path : <path> -> momentum cell -> <path> -> starting cell
        addToNodePath(rampPath, [rampPath[0], startingNode])
        parentNode = rampPath[-1]
 
    # Low-speed bike : starting position is already momentum cell
    else:
        rampPath = []
        parentNode = destinationNode.parent

    # Add remaining nodes until destination cell
    for x in range(1, 1 + abs(rampData.destinationCell.X - startingPosition.X)):
        pathNode = Node(Position(startingPosition.X + x * rampData.orientation, startingPosition.Y, startingPosition.zone), zoneMap, parentNode)
        parentNode = pathNode
        addToNodePath(rampPath, [pathNode])

    # Save ramp data to all nodes in the path
    for node in rampPath:
        node.rampData = rampData

    return rampPath[::-1]