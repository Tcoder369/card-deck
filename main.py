import random

class Card:
  def __init__(self, number, shape):
    self.number = number
    self.shape = shape
    if self.number == 1:
      self.number = 'Ace'
    elif self.number == 11:
      self.number = 'Jack'
    elif self.number == 12:
      self.number = 'Queen'
    elif self.number == 13:
      self.number = 'King'
  
  def __repr__(self):
    if self.shape == 1:
      return str(self.number) + ' of harts'
    elif self.shape == 2:
      return str(self.number) + ' of diamonds'
    elif self.shape == 3:
      return str(self.number) + ' of spades'
    elif self.shape == 4:
      return str(self.number) + ' of clubs'

class Deck:
  def __init__(self):
    self.cards = []
    for i in range(1,5):
      for x in range (1,14):
        card = Card(x , i)
        self.cards.append(card)
  
  def __repr__(self):
    return str(self.cards)

  def pick(self):
    return random.choice(self.cards)

  def shuffle(self):
   deck = 52
   cards = []
   for i in range(deck):
     choice = random.choice(self.cards)
     cards.append(choice)
     self.cards.remove(choice)
   self.cards = cards 
   return self.cards

  def sort(self):
    cards = []
    for i in range(1,5):
      for x in range(1, 14):
        card = Card(x, i)
        cards.append(card)
    self.cards = cards
    return self.cards

  def cut_even(self, num_cuts):
    cut_every = 52/num_cuts
    cuts = []
    for i in range(int(num_cuts)):
      cuts.append(self.cards[:int(cut_every)])
      del self.cards[0:int(cut_every)]
    if len(self.cards) > 0:
     for i in self.cards:
       cuts[-1].append(i)
    self.cards = cuts
    return self.cards

  def cut_random(self, num_cuts):
    piles = []
    cuts1= []
    for i in range(int(num_cuts-1)):
      cuts1.append(random.randrange(52))
    
    cuts1.sort() 
    
    for m in cuts1:
      if cuts1.index(m) != 0:
        first = cuts1[cuts1.index(m)-1]
        last = int(m)
        piles.append(self.cards[first:last])
      else:
        piles.append(self.cards[:m])
    piles.append(self.cards[cuts1[-1]:])
    
    self.cards = piles
    return self.cards

new = Deck()
