class Card():
  def __init__(self, name, suit, points):
    self.name = name
    self.suit = suit
    self.points = points

  def showPoints(self):
    print(self.points)

  def showName(self):
    print(self.name)

  def showSuit(self):
    print(self.suit)

  def showAll(self):
   return self.name + ' of ' + self.suit + ' (score: ' + str(self.points) + ')'