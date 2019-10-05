class Player():
  def __init__(self, name):
    self.name = name
    self.cards = []

  def points(self):
    totalPoints = 0

    for i in self.cards:
      totalPoints += i.points

    return totalPoints

  def addCart(self, card):
    self.cards.append(card)
    return self.points()

  def win(self):
    print('Game Over')
    print('Congrats!!!', self.name, 'YOU ARE WINNER!!!')

  def lose(self):
    print('Game Over')
    print('Regrets', self.name, 'better luck next time!')