import Point
import random, logging

# declaration of dictionaries used for keeping track of positions on boards
boardU = { } 
boardE = { }
ShipsU = { }
ShipsE = { }

# character representation of numbers 1 - 10
ABlist = {
  1:'A',
  2:'B',
  3:'C',
  4:'D',
  5:'E',
  6:'F',
  7:'G',
  8:'H',
  9:'I',
  10:'J',
}

# ship length and ship count 
# TODO MAKE IT POSSIBLE FOR MORE THAN 1 SHIP TO PASS THROUGH
ShipFrameU = [
  [6,1],
  [5,1],
  [4,1],
  [3,1],
  [2,1]
]
ShipFrameE = [
  [6,1],
  [5,1],
  [4,1],
  [3,1],
  [2,1]
]

def main():
  global finished
  # boot operations
  generate()
  #placeShips(boardU),placeShips(boardE)

  genShips(boardU, ShipFrameU)
  finished = False
  genShips(boardE, ShipFrameE)

def generate():
  '''
  Generates both boards as dictionaries pointing to class instances
  '''   

  # for all points on the grid 
  for x in range(1, 11):
    for y in range(1, 11):

      # assigns string value to tempname, for example C4
      tempname = ABlist[x] + str(y)

      # assigns given string value to these two to-be instance variables
      tempname1 = tempname
      tempname2 = tempname

      # instance variables than can be invoked by the point name
      tempname1 = Point.PointU(tempname, (x, y))
      tempname2 = Point.PointE(tempname, (x, y))

      # dictionaries that have "coordinate names" for keys, pointers to their class instance as values
      boardU[tempname] = tempname1
      boardE[tempname] = tempname2

finished = False
shipID = -1
def genShips(board, ShipFrame):
  '''
  Ship generator. Places all of the ships on a board.
  '''
  global shipID
  global finished

  shipID += 1

  if shipID == 5:
    finished = True
    shipID = -1

  # debug
  print(ShipFrame[shipID][0])
  print(shipID)
  print(finished)


  while not finished:

    # horizontal = 1, vertical = 0
    alignment = random.randint(0,1)

    # random starting point of the ship
    startX = random.randint(1, 10)
    startY = random.randint(1, 10-ShipFrame[shipID][0])

    if alignment == 1:
      start = [startX, startY]
      SHIP = getInitShipPoints(start, 1, shipID, ShipFrame)
    else:
      start = [startY, startX]
      SHIP = getInitShipPoints(start, 0, shipID, ShipFrame)

    COUNT = 0
    for point in SHIP:
      if validatePoint(point, board) == False:
        # point is taken, generste new ones
        print("broken")
        break 
      else:
        COUNT += 1

        if COUNT == ShipFrame[shipID][0]:
          afterValidating(SHIP, board, shipID, ShipFrame)
          genShips(board, ShipFrame)
        continue
    continue

def afterValidating(SHIP, board, shipID, ShipFrame):
  '''
  Continuation of the genShips method, after making sure that all of the positions are not taken
  '''

  # debug
  print("I made it!" + str(SHIP))

  shipPoints = [ ]
  
  # lists all the 'Real' Points, sets them taken
  for point in SHIP:
    for key in board:
      if point == list(board[key].XY):       
        shipPoints.append(board[key])
        board[key].taken = True

        # debug
        #print(board[key].name)

  # pointer to a current ID value 
  tempID = shipID

  # creates the instance of the Ship class
  tempID = Point.Ship(shipID, len(SHIP), shipPoints)   

  # decrements the ammount of the current ship
  ShipFrame[shipID][1] -= 1 

def getInitShipPoints(cords, alignment, shipID, ShipFrame):
  '''
  Returns a list of ships points
  '''
  SHIP = []

  if alignment == 1:
    for p in range(ShipFrame[shipID][0]):
      SHIP.append([cords[0], cords[1] + p])
  else:
    for p in range(ShipFrame[shipID][0]):
      SHIP.append([cords[0] + p, cords[1]])
  return SHIP
 
def validatePoint(point, board):
  '''
  Checks if a given point is taken
  '''
  (x, y) = point
  for key in board.keys():
    if board[key].XY == (x, y):
      if board[key].taken == False:
        return True
      else:
        return False 


if __name__ == '__main__':
	main()
