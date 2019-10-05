from card import Card
import random

class Deck():
  def __init__(self):
    names = {'TWO' : 2, 'THREE' : 3, 'FOUR' : 4,
             'FIVE' : 5, 'SIX' : 6, 'SEVEN' : 7,
             'EIGHT' : 8, 'NINE' : 9, 'TEN' : 10,
             'JACK' : 10, 'QUEEN' : 10, 'KING' : 10,
             'ACE' : 1}

    suits = ('HEARTS', 'DIAMONDS', 'SPADES', 'CLUBS')

    cards = []

    i = 0
    while i < 4:
      for key in names:
        for suit in suits:
          card = Card(key, suit, names[key])
          cards.append(card)
      i += 1

    self.cards = cards

  def shuffleDeck(self):
    random.shuffle(self.cards)

  def nextCard(self):
    firstCard = self.cards.pop(0)
    return firstCard
