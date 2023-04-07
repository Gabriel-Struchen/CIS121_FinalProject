#Black Jack Game
"""
1.Comments and legible code 
    -- Do to everything as you go
2.Loops and selection statments     
    -- Used to help determine if more games are played (play again?)
        and to determine point values of cards during the game
3.I/O Files
    -- Used to track the players money (starting amount and running total)
4.Collections
    -- storing the cards left in the deck, and what is on the table for the player
5.Functions
    -- Used for the player to be able to select what to do
        hit,split,stand,surrender,double-down
6.Classes
    -- Setup for the deck of cards and how to determine what card is what
"""
import random
import FinalProject_Functions
"""
card setup
In BlackJack, an Ace can be either a 1 or 11 (for score)
we must intialize a 1 as also being an Ace
"""
class Card:
    def __init__ (self,value,suit):
        self.suit  = suit
        self.value = int(value)
        
    def __str__ (self):
        faces = ['Jack','Queen','King','Ace'] #11 = Jack, 12 = Queen, 13 = King, 14 = Ace
        if self.value <= 10 and self.value >= 2:
            return '{} of {}'.format(self.value,self.suit)
        elif self.value == 1:   
            return 'Ace of {}'.format(self.suit)
        else:
            return '{} of {}'.format(faces[self.value-11],self.suit)

class Card_group:
    def __init__ (self,cards = []):
        self.cards = cards
    def shuffle(self):
        random.shuffle(self.cards)  #shuffle the deck
    def deal(self):
        return self.cards.pop(0)    #remove the top card from the deck and deal it to the player

class Standard_deck(Card_group):    #Create all 52 cards in deck
    def __init__ (self):
        self.cards = []
        for s in ['Hearts','Diamonds','Clubs','Spades']:
            for v in range (1,14):
                self.cards.append(Card(v,s))

class Player:   #Player is a class that stores what cards the player has in their hand
    def __init__ (self,hand = [],points = 0):
        self.hand = hand
        self.points = points

    def __str__ (self):
        return f"Player's Hand: {[str(card) for card in self.hand]}, Points: {self.points}"

    def update_points (self):
        self.points = sum([card.value if card.value <= 10 else 10 for card in self.hand])
        num_aces = sum([card.value == 1 for card in self.hand])
        if num_aces > 0 and self.points + 10 <= 21:
            self.points += 10

class Dealer:
    def __init__ (self,hand = [],points = 0):
        self.hand = hand
        self.points = points

    def __str__ (self):
        return f"Dealer's Hand: {[str(card) for card in self.hand]}, Points: {self.points}"

    def update_points (self):
        self.points = sum([card.value if card.value <= 10 else 10 for card in self.hand])
        num_aces = sum([card.value == 1 for card in self.hand])
        if num_aces > 0 and self.points + 10 <= 21:
            self.points += 10

deck = Standard_deck()  #setup what deck is being used
deck.shuffle()          #shuffle the deck

player = Player()
dealer = Dealer()

for i in range(2):
    player.hand.append(deck.deal()) #deal a card to the player
    player.update_points()

    dealer.hand.append(deck.deal()) #deal a card to the dealer
    dealer.update_points()

print(player,"\n")  #print off what cards are in the player's hand

print(dealer,"\n")  #print off what cards are in the dealer's hand

if player.points == 21:
    print("Natural Blackjack!")
else:



    while True:
        options = "1 Hit \n2 Stand\n3 Split\n4 Double-Down\n5 Surrender"    #players options
        print(options,"\n")

        player_choice = input("Enter your choice (1-5): ")      #player makes a decision

        if player_choice == "1":
            FinalProject_Functions.Hit(player,deck)
        elif player_choice == "2":
            break
        else:
            print("Invalid Option: Try Again")
        '''
        elif player_choice == "3":
            #write split function
        elif player_choice == "4":
            #bet double the money
        elif player_choice =="5":
            #get half money back
        '''
        if player.points > 21:
            print("\nBust: You lose\n")
            break
        elif player.points == 21:
            print("\nBlackJack!\n")
            break
    
    if player.points > 21:
        None
    else:
        FinalProject_Functions.dealerAI(dealer,player,deck)
        if dealer.points > 21 or dealer.points < player.points:
            print("Player Wins!\n")
        elif dealer.points > player.points:
            print("Dealer Wins!\n")
        else:
            print("Push!: Money Back")



