#!/usr/bin/env python3



class Deck:
    def __init__(self):
        self.size = 52;
        self.suiteH = self.cards()
        self.suiteD = self.cards()
        self.suiteC = self.cards()
        self.suiteS = self.cards()
        
        self.hearts = self.suiteH
        self.diamonds = self.suiteD
        self.clubs = self.suiteC
        self.spades = self.suiteS

        #self.currentDeck
        
    def cards(self): 
        cards = {
                "a": 0,
                "1": 1,
                "2": 2,
                "3": 3,
                "4": 4,
                "5": 5,
                "6": 6,
                "7": 7,
                "8": 8,
                "9": 9,
                "10": 10,
                "j": 11,
                "q": 12,
                "k": 13
                }
        return cards

    def deal(self):
        deck = {
                "hearts" : self.hearts,
                "diamonds" : self.diamonds,
                "clubs": self.clubs,
                "spades": self.spades
                }
        deckHalf1 = {}
        deckHalf2 = {}

        for x in range(len(self.size))
        
        print(deck)
        return 0

def main():
    print("Hello World!")

    deck = Deck()
    #print(deck.hearts)
    #print(deck.diamonds)
    #print(deck.clubs)
    #print(deck.spades)

    print(deck.deal())
    return 0

if __name__ == "__main__":
    main()
