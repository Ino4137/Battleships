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
ShipFrame = [
  [5,1],
  [4,1],
  [3,2],
  [2,1]
]

def main():

  # boot operations
  generate()
  placeShips(boardU),placeShips(boardE)

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

def placeShips(board):
  '''
  Randomizes the position of the ships, makes sure they do not overlap
  '''
  ID = 0

  # for all ships 
  for l in range(4):

    beg = ShipFrame[l][0] 
    end = ShipFrame[l][1]

    # while number of ships placed is not 0
    while end != 0:
      # horizontal = 1, vertical = 0
      alignment = random.randint(0,1)

      # random starting point of the ship
      startX = random.randint(1, 10--ShipFrame[l][0])
      startY = random.randint(1, 10)

      if alignment == 1:
        start = [startX, startY]
      else:
        start = [startY, startX]

      # loops over all the points under the ship
      try:
        for unit in range(ShipFrame[l][0] + 1):
          #print("debug.unit: " + str(unit))
     
          #print("debug.1")

          # if a point is taken 
          if False == validatePoint(start, board):
            raise Exception
          else:
            beg -= 1
            start[alignment] += unit

          #print(start)

          # if all points returned True
          if ShipFrame[l][0] - unit == 0:

            # reset the assisting list of points
            shipPoints = [ ] 

            # decrement remaining count
            end -= 1

            # get a new pointer
            tempID = ID

            # once more loops over the points of the ship to get their instances
            for num in range(ShipFrame[l][0]):
              for key in board:
                if [start[alignment] + ShipFrame[l][0] - 1 - num, start[int(abs(alignment-1))]] == list(board[key].XY):
                  print(board[key].name)
                  shipPoints.append(board[key].name)
                  board[key].taken = True
                  print(shipPoints)

            # finally, crates the variable instance of Ship class
            tempID = Point.Ship(ID, ShipFrame[l][0], shipPoints)
            print(tempID.alivePoints)
            # increment ID
            ID += 1 
            #print("debug.ID = " + str(ID))

      # if a point returned False
      except Exception as e:
        logging.exception("message")

        # not decrementing the ship num, jumping to next loop in Run.py:69
        continue


      
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