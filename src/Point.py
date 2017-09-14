class Point:
  def __init__(self, name, XY, taken=False, flagged=False, shot=False):
    self.name = name
    self.XY = XY
    self.taken = taken
    self.flagged = flagged
    self.shot = shot

class PointU(Point):
  pass

class PointE(Point):
  pass

class Ship:
  def __init__(self, ID, length, alivePoints, shotPoints=[]):
    self.ID = ID
    self.length = length
    self.alivePoints = alivePoints
    self.shotPoints = shotPoints