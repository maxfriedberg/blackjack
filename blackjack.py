import random
from charts import hard_chart
from charts import soft_chart
from charts import pairs_chart
from charts import sort_hand
from charts import make_move

class Cards:
    def __init__(self, numDecks):
        for x in range(numDecks):
            for y in range(4):
                self.Shoe.append('2')
                self.Shoe.append('3')
                self.Shoe.append('4')
                self.Shoe.append('5')
                self.Shoe.append('6')
                self.Shoe.append('7')
                self.Shoe.append('8')
                self.Shoe.append('9')
                self.Shoe.append('10')
                self.Shoe.append('10')
                self.Shoe.append('10')
                self.Shoe.append('10')
                self.Shoe.append('A')
        random.shuffle(self.Shoe)

    def deal(self):
        return self.Shoe.pop()
        

    Shoe = []

cards = Cards(6)

#6 decks
#Dealer stands on soft 17
#3-2 payoff for BJ

#play hand (my card 1, dealer downcard, my card 2, dealer upcard)

settled = 0

while(settled != 1):

    playerHands = []
    phand = []
    dhand = []

    phand.append(cards.deal())
    dhand.append(cards.deal())
    phand.append(cards.deal())
    dealerUpcard = cards.deal()
    dhand.append(dealerUpcard)

    playerHands.append(phand)

    move = make_move(phand, len(playerHands), dealerUpcard)

    if move == "Stand":
        print(move)
    elif move == "Hit":
        print(move)
    elif move == "Split":
        print(move)
    else:
        print(move)

    settled = settled + 1



print(playerHands)
print(dealerUpcard)
print(move)

