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