from modules.cell import SOLID_BLOCKS
from modules.zone import Position


class Ramp():
    def __init__(self, position: Position, cellType: str, isHighSpeed: bool):
        self.isHighSpeed = isHighSpeed
        self.orientation = 1 if cellType == "<" else -1
        self.position: Position = position
        self.momentumCell: Position|None = None
        self.destinationCell: Position|None = None
        self.processed = False

    #####################################################
    # Get final position after jumping from a bike ramp #
    #####################################################
    def findDestinationCell(self, zoneMap):

        # High bike speed : check for the furthest free cell after jumping from the ramp
        if (self.isHighSpeed):
            if (zoneMap[self.position.Y][self.position.X + 4 * self.orientation] in SOLID_BLOCKS):
                self.destinationCell = Position(self.position.X + 3 * self.orientation, self.position.Y, self.position.zone)
            elif (zoneMap[self.position.Y][self.position.X + 5 * self.orientation] in SOLID_BLOCKS):
                self.destinationCell =  Position(self.position.X + 4 * self.orientation, self.position.Y, self.position.zone)
            else:
                self.destinationCell =  Position(self.position.X + 5 * self.orientation, self.position.Y, self.position.zone)

        # Low bike speed : go to next cell after the ramp
        else:
            self.destinationCell =  Position(self.position.X + 1 * self.orientation, self.position.Y, self.position.zone)


    def findMomentumCell(self, zoneMap):
        playerPosition = Position(self.position.X - self.orientation, self.position.Y, self.position.zone)

        # Low-speed bike : no need for momentum, just start in front of the ramp
        if (not self.isHighSpeed):
            self.momentumCell = playerPosition
            return

        # High-speed bike : find a valid path two cells away
        for x in [-2, 2, 0, -1, 1]:
            for y in [-2, 2, 0, -1, 1]:

                # Momentum cell is exactly two cells away
                if (abs(x) + abs(y) == 2):
                    potentialMomentumCell = Position(playerPosition.X + x, playerPosition.Y + y, playerPosition.zone)

                    # Momentum cell is not regular cell, find another one
                    if (potentialMomentumCell.getCell(zoneMap) != "O"):
                        continue

                    # Straight line : only one path
                    if (x == 0 or y == 0):
                        pathCell = Position(playerPosition.X + (x // 2), playerPosition.Y + (y // 2), playerPosition.zone)

                        if (pathCell.getCell(zoneMap) == "O"):
                            self.momentumCell = potentialMomentumCell

                    # Curved path : check both potential paths
                    else:
                        pathCellX = Position(playerPosition.X + x, playerPosition.Y, playerPosition.zone)
                        pathCellY = Position(playerPosition.X, playerPosition.Y + y, playerPosition.zone)

                        if (pathCellX.getCell(zoneMap) == "O" or pathCellY.getCell(zoneMap) == "O"):
                            self.momentumCell = potentialMomentumCell

                    # Take the first momentum cell we find
                    if (self.momentumCell):
                        return
                        
        