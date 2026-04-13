CELL_COST = {
    # Traveling cells
    "O": 1, # Regular cell
    "Z": 5, # Zone (door, cave entrance)
    "G": 3, # Grass
    "g": 3, # Tall grass
    "1": 1, # 1-depth snow
    "2": 2, # 2-depth snow
    "3": 4, # 3-depth snow
    "4": 8, # 4-depth snow
    "s": 1, # Swamp
    "S": 10, # Deep swamp
    "m": 3, # Marsh (Grass in swamp)
    "M": 12, # Deep marsh (Grass in deep swamp)
    "V": 5, # Bike slope
    "E": 1, # Elevator
    "e": 1, # Elevator door

    # HM Obstacles
    "t": 5, # Tree
    "r": 5, # Rock
    "W": 5, # Water
    "w": 7, # Waterfall
    "C": 1, # Climb

    # Height-depending cells
    "A": 1, # Above ground (bridge)
    "a": 1, # Above ground (bike bridge)
    "@": 1, # Above solid block (bridge)
    "B": 1, # Below bridge
    "d": 5, # Below bridge on water

    # Orientation-depending cells
    "D": 3, # One-way ledge to go down
    "L": 3, # One-way ledge to go left
    "U": 3, # One-way ledge to go up
    "R": 3, # One-way ledge to go right
}

SOLID_BLOCKS = [
    "X", # Wall, Tree, etc
    "N", # NPC
    "P", # Post (Special process since it displays a message if coming from the bottom)
    "I", # Interactable (Static encounter, Shop, etc)
    "H", # Honey Tree
    "b", # Boulder (Cannot be removed like Cut or Rock Smash, so is actually an obstacle)
    ">", # Bike ramp oriented to the left
    "<", # Bike ramp oriented to the right
]