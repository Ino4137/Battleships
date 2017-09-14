import Point

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

def main():
  Board.generate()

class Board:

  @staticmethod
  def generate():
    '''
    Generates both boards as dictionaries pointing to class instances
    '''
    boardU = {} 
    boardE = {}
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

if __name__ == '__main__':
	main()