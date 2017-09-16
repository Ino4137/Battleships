class Ship:
  def __init__(self, ID, length, alivePoints, shotPoints=[]):
    self.ID = ID
    self.length = length
    self.alivePoints = alivePoints
    self.shotPoints = shotPoints

class Point:
  def __init__(self, name, XY, taken=False, flagged=False, shot=False, ship = None):
    self.name = name 
    self.XY = XY
    self.taken = taken # redundant, i'm only using .ship anyway
    self.flagged = flagged # if i'm ever to implement a certain feature
    self.shot = shot

    # 42 is default value, do not ask why
    self.ship = ship


class PointU(Point):
  pass

class PointE(Point):
  pass

