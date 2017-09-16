import Point
import random, sys
import subprocess as sp

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
ShipFrameU = [
  [5,1],
  [4,1],
  [3,1],
  [3,1],
  [2,1]
]
ShipFrameE = [
  [5,1],
  [4,1],
  [3,1],
  [3,1],
  [2,1]
]
shotLog = []
hitLog = []
shipKillLog = []

shotLogE = []
hitLogE = []
shipKillLogE = []

def main():
  '''
  Starting point, boot operations and game loop
  '''
  global finished, shotLog, hitLog, TURN

  generate()
  genShips(boardU, ShipFrameU)

  # allows for the second call of the genShips method
  finished = False
  genShips(boardE, ShipFrameE)

  # game loop
  TURN = "USER"
  gameOver = False
  while not gameOver:

    # if all ships sunk, end game
    if len(shipKillLog) == len(ShipFrameU):
      print("You have won!")
      sys.exit(0)
    if len(shipKillLogE) == len(ShipFrameE):
      print("You have lost.")
      sys.exit(0)
      

    tmp = sp.call('clear', shell=True)
    print("---Enemy turn---")
    print("Shots taken: {0}".format(str(shotLogE)))
    print("Hits: {0}".format(str(hitLogE)))
    print("Ships sunk: {0}".format(str(shipKillLogE)))

    # users's turn beginning
    TURN = "USER"
    print("---Your turn---")
    print("Shots taken: {0}".format(str(shotLog)))
    print("Hits: {0}".format(str(hitLog)))
    print("Ships sunk: {0}".format(str(shipKillLog)))
    try:
      inp = input(": ")

      # help command
      if inp == "help":
        print("Type point's coordinate NAME to shoot, eg: d5, E7\nUse 'exit' to turn the game off")
        continue
      
      # exit command
      if inp == "exit":
        print("Exitting the game")
        sys.exit(0)

      # test if point was shot at
      if inp.upper() not in shotLog:
        if inp.upper() not in hitLog:

          # test is a given point exists on the board
          if inp.upper() in boardE.keys():

            # shoots the point, logs the shot
            if shoot(inp, boardE):
              hitLog.append(inp.upper())
            else:
              shotLog.append(inp.upper())

          else:
            print("Given point is not on the board")
            continue

        elif inp.upper() in boardE.keys():
          print("Given point was already shot at")
          continue

      elif inp.upper() in boardE.keys():
        print("Given point was already shot at")
        continue

      else:
        print("Not a valid command. Type 'help' for help")
        continue

    except TypeError:
      print("TypeError: wrong input type")
      continue

    # enemy turn
    # random shot
    TURN = "E"
    randomDifficulty()


def randomDifficulty():
  while True:
    # random point
    randpoint = random.choice(list(boardE.keys()))

    # if it was not shot at before
    if randpoint not in shotLogE:
      if randpoint not in hitLogE:

        # shoots, logs the result
        if shoot(randpoint, boardU):
          hitLogE.append(randpoint.upper())
          break
        else:
          shotLogE.append(randpoint.upper())
          break


def shoot(point, board):
  '''
  Shoots a given point on a given board, returns True is it is a hit, False if not
  '''
  point = point.upper()
  board[point].shot = True
  if board[point].ship is not None:
    board[point].ship.alivePoints.remove(board[point])
    board[point].ship.shotPoints.append(board[point])
    if not board[point].ship.alivePoints:
      if TURN == "E":
        shipKillLogE.append(board[point].ship.length)
      else:
        shipKillLog.append(board[point].ship.length)
    return True
  return False

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

  shipPoints = [ ]
  
  # lists all the 'Real' Points, sets them taken
  for point in SHIP:
    for key in board:
      if point == list(board[key].XY):       
        shipPoints.append(board[key])
        board[key].taken = True

  # pointer to a current ID value 
  tempID = shipID

  # creates the instance of the Ship class
  tempID = Point.Ship(shipID, len(SHIP), shipPoints)   

  # assigns all the ships points to the ship
  for point in SHIP:
    for key in board:
      if point == list(board[key].XY):       
        board[key].ship = tempID 

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
