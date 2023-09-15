import random

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

hard_chart = {
    5: {"2": "Hit", "3": "Hit", "4": "Hit", "5": "Hit", "6": "Hit", "7": "Hit", "8": "Hit", "9": "Hit", "10": "Hit", "A": "Hit"},
    6: {"2": "Hit", "3": "Hit", "4": "Hit", "5": "Hit", "6": "Hit", "7": "Hit", "8": "Hit", "9": "Hit", "10": "Hit", "A": "Hit"},
    7: {"2": "Hit", "3": "Hit", "4": "Hit", "5": "Hit", "6": "Hit", "7": "Hit", "8": "Hit", "9": "Hit", "10": "Hit", "A": "Hit"},
    8: {"2": "Hit", "3": "Hit", "4": "Hit", "5": "Hit", "6": "Hit", "7": "Hit", "8": "Hit", "9": "Hit", "10": "Hit", "A": "Hit"},
    9: {"2": "Hit", "3": "Double", "4": "Double", "5": "Double", "6": "Double", "7": "Hit", "8": "Hit", "9": "Hit", "10": "Hit", "A": "Hit"},
    10: {"2": "Double", "3": "Double", "4": "Double", "5": "Double", "6": "Double", "7": "Double", "8": "Double", "9": "Double", "10": "Hit", "A": "Hit"},
    11: {"2": "Double", "3": "Double", "4": "Double", "5": "Double", "6": "Double", "7": "Double", "8": "Double", "9": "Double", "10": "Double", "A": "Hit"},
    12: {"2": "Hit", "3": "Hit", "4": "Stand", "5": "Stand", "6": "Stand", "7": "Hit", "8": "Hit", "9": "Hit", "10": "Hit", "A": "Hit"},
    13: {"2": "Stand", "3": "Stand", "4": "Stand", "5": "Stand", "6": "Stand", "7": "Hit", "8": "Hit", "9": "Hit", "10": "Hit", "A": "Hit"},
    14: {"2": "Stand", "3": "Stand", "4": "Stand", "5": "Stand", "6": "Stand", "7": "Hit", "8": "Hit", "9": "Hit", "10": "Hit", "A": "Hit"},
    15: {"2": "Stand", "3": "Stand", "4": "Stand", "5": "Stand", "6": "Stand", "7": "Hit", "8": "Hit", "9": "Hit", "10": "Hit", "A": "Hit"},
    16: {"2": "Stand", "3": "Stand", "4": "Stand", "5": "Stand", "6": "Stand", "7": "Hit", "8": "Hit", "9": "Hit", "10": "Hit", "A": "Hit"},
    17: {"2": "Stand", "3": "Stand", "4": "Stand", "5": "Stand", "6": "Stand", "7": "Stand", "8": "Stand", "9": "Stand", "10": "Stand", "A": "Stand"},
    18: {"2": "Stand", "3": "Stand", "4": "Stand", "5": "Stand", "6": "Stand", "7": "Stand", "8": "Stand", "9": "Stand", "10": "Stand", "A": "Stand"},
    19: {"2": "Stand", "3": "Stand", "4": "Stand", "5": "Stand", "6": "Stand", "7": "Stand", "8": "Stand", "9": "Stand", "10": "Stand", "A": "Stand"},
    20: {"2": "Stand", "3": "Stand", "4": "Stand", "5": "Stand", "6": "Stand", "7": "Stand", "8": "Stand", "9": "Stand", "10": "Stand", "A": "Stand"}
}

soft_chart = {
    "A, 2": {"2": "Hit", "3": "Hit", "4": "Hit", "5": "Double", "6": "Double", "7": "Hit", "8": "Hit", "9": "Hit", "10": "Hit", "A": "Hit"},
    "A, 3": {"2": "Hit", "3": "Hit", "4": "Hit", "5": "Double", "6": "Double", "7": "Hit", "8": "Hit", "9": "Hit", "10": "Hit", "A": "Hit"},
    "A, 4": {"2": "Hit", "3": "Hit", "4": "Double", "5": "Double", "6": "Double", "7": "Hit", "8": "Hit", "9": "Hit", "10": "Hit", "A": "Hit"},
    "A, 5": {"2": "Hit", "3": "Hit", "4": "Double", "5": "Double", "6": "Double", "7": "Hit", "8": "Hit", "9": "Hit", "10": "Hit", "A": "Hit"},
    "A, 6": {"2": "Hit", "3": "Double", "4": "Double", "5": "Double", "6": "Double", "7": "Hit", "8": "Hit", "9": "Hit", "10": "Hit", "A": "Hit"},
    "A, 7": {"2": "Stand", "3": "Double", "4": "Double", "5": "Double", "6": "Double", "7": "Stand", "8": "Stand", "9": "Hit", "10": "Hit", "A": "Hit"},
    "A, 8": {"2": "Stand", "3": "Stand", "4": "Stand", "5": "Stand", "6": "Stand", "7": "Stand", "8": "Stand", "9": "Stand", "10": "Stand", "A": "Stand"},
    "A, 9": {"2": "Stand", "3": "Stand", "4": "Stand", "5": "Stand", "6": "Stand", "7": "Stand", "8": "Stand", "9": "Stand", "10": "Stand", "A": "Stand"},
    "2, A": {"2": "Hit", "3": "Hit", "4": "Hit", "5": "Double", "6": "Double", "7": "Hit", "8": "Hit", "9": "Hit", "10": "Hit", "A": "Hit"},
    "3, A": {"2": "Hit", "3": "Hit", "4": "Hit", "5": "Double", "6": "Double", "7": "Hit", "8": "Hit", "9": "Hit", "10": "Hit", "A": "Hit"},
    "4, A": {"2": "Hit", "3": "Hit", "4": "Double", "5": "Double", "6": "Double", "7": "Hit", "8": "Hit", "9": "Hit", "10": "Hit", "A": "Hit"},
    "5, A": {"2": "Hit", "3": "Hit", "4": "Double", "5": "Double", "6": "Double", "7": "Hit", "8": "Hit", "9": "Hit", "10": "Hit", "A": "Hit"},
    "6, A": {"2": "Hit", "3": "Double", "4": "Double", "5": "Double", "6": "Double", "7": "Hit", "8": "Hit", "9": "Hit", "10": "Hit", "A": "Hit"},
    "7, A": {"2": "Stand", "3": "Double", "4": "Double", "5": "Double", "6": "Double", "7": "Stand", "8": "Stand", "9": "Hit", "10": "Hit", "A": "Hit"},
    "8, A": {"2": "Stand", "3": "Stand", "4": "Stand", "5": "Stand", "6": "Stand", "7": "Stand", "8": "Stand", "9": "Stand", "10": "Stand", "A": "Stand"},
    "9, A": {"2": "Stand", "3": "Stand", "4": "Stand", "5": "Stand", "6": "Stand", "7": "Stand", "8": "Stand", "9": "Stand", "10": "Stand", "A": "Stand"}
}

pairs_chart = {
    "2, 2": {"2": "Split", "3": "Split", "4": "Split", "5": "Split", "6": "Split", "7": "Split", "8": "Hit", "9": "Hit", "10": "Hit", "A": "Hit"},
    "3, 3": {"2": "Split", "3": "Split", "4": "Split", "5": "Split", "6": "Split", "7": "Split", "8": "Hit", "9": "Hit", "10": "Hit", "A": "Hit"},
    "4, 4": {"2": "Hit", "3": "Hit", "4": "Hit", "5": "Split", "6": "Split", "7": "Split", "8": "Hit", "9": "Hit", "10": "Hit", "A": "Hit"},
    "5, 5": {"2": "Double", "3": "Double", "4": "Double", "5": "Double", "6": "Double", "7": "Double", "8": "Double", "9": "Double", "10": "Hit", "A": "Hit"},
    "6, 6": {"2": "Split", "3": "Split", "4": "Split", "5": "Split", "6": "Split", "7": "Hit", "8": "Hit", "9": "Hit", "10": "Hit", "A": "Hit"},
    "7, 7": {"2": "Split", "3": "Split", "4": "Split", "5": "Split", "6": "Split", "7": "Split", "8": "Hit", "9": "Hit", "10": "Hit", "A": "Hit"},
    "8, 8": {"2": "Split", "3": "Split", "4": "Split", "5": "Split", "6": "Split", "7": "Split", "8": "Split", "9": "Split", "10": "Split", "A": "Split"},
    "9, 9": {"2": "Split", "3": "Split", "4": "Split", "5": "Split", "6": "Split", "7": "Stand", "8": "Split", "9": "Split", "10": "Stand", "A": "Stand"},
    "10, 10": {"2": "Stand", "3": "Stand", "4": "Stand", "5": "Stand", "6": "Stand", "7": "Stand", "8": "Stand", "9": "Stand", "10": "Stand", "A": "Stand"},
    "A, A": {"2": "Split", "3": "Split", "4": "Split", "5": "Split", "6": "Split", "7": "Split", "8": "Split", "9": "Split", "10": "Split", "A": "Split"}
}

playerHands = []
dealerHand = []


def playHand(cards_object):
    playerCard1 = cards_object.Shoe.pop()
    dealerDownCard = cards_object.Shoe.pop()
    playerCard2 = cards_object.Shoe.pop()
    dealerUpCard = cards_object.Shoe.pop()

    print("Player Cards: ", playerCard1, playerCard2)
    print("Dealer Upcard: ", dealerUpCard)

    playerHands.append([playerCard1, playerCard2])
    dealerHand.append([dealerDownCard, dealerUpCard])

    string_hand = playerCard1 + playerCard2

    if string_hand == "A10" or string_hand == "10A":
        #blackjack
        decision = "Stand"
    elif playerCard1 == playerCard2:
        #use pairs chart
        hand = playerCard1 + ", " + playerCard2
        decision = pairs_chart[hand][dealerUpCard]
    elif playerCard1 == 'A' or playerCard2 == 'A':
        #use soft chart
        hand = playerCard1 + ", " + playerCard2
        decision = soft_chart[hand][dealerUpCard]
    else:
        #use hard chart
        hand = int(playerCard1) + int(playerCard2)
        decision = hard_chart[hand][dealerUpCard]

    print(decision)
