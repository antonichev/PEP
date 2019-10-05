from player import Player
from deck import Deck

print('Welcome to BlackJack game!')
print('=' * 50)

userName = input('Introduce yourself: ')
print('OK,', userName, 'let\'s begin')

print('*' * 19, 'GAME RULES', '*' * 19)
#TODO: Add game rules
print('*' * 50)

dealer = Player('Dealer')
player = Player(userName)

deck = Deck()

shuffles = 5
mainScore = 21

while shuffles >= 0:
  deck.shuffleDeck()
  shuffles -= 1

def askForMore():
  while True:
    answer = input('Would You like to take one more card? ([y]es/[n]o)').lower()
    if answer == 'yes' or answer == 'y':
      return True
    elif answer == 'no' or answer == 'n':
      return False
    else:
      print('Your answer is not clear...')

while True:
  playerCard = deck.nextCard()
  dealerCard = deck.nextCard()

  dealerPoints = dealer.addCart(dealerCard)
  playerPoints = player.addCart(playerCard)

  print(dealer.name, 'got', dealerCard.showAll(), 'Total points: ', dealerPoints)
  print(player.name, 'got', playerCard.showAll(), 'Total points: ', playerPoints, '\n')

  answer = askForMore()

  if not answer:
    dealerScore = abs(mainScore - dealer.points())
    playerScore = abs(mainScore - player.points())

    if dealerScore == playerScore:
      print('-*-*-*- DRAW -*-*-*-', '\n')
    elif dealerScore > playerScore:
      player.win()
    else:
      player.lose()

    break