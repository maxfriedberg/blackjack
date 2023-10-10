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

        

    Shoe = []

cards = Cards(6)

#6 decks
#Dealer stands on soft 17
#3-2 payoff for BJ

#attribute 4 arrays to player to respresent max number of hands
#deal to player and dealer

#if split, move to next array, else next dealt




