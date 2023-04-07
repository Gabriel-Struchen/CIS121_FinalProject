#dealer AI
def dealerAI(dealer,player,deck):
    for i in range(7):
        if dealer.points >= 17:
            None

        elif dealer.points <= 16:
            dealer.hand.append(deck.deal())
            dealer.update_points()
            print("Dealer Hits")
            print(dealer)
            '''
        elif dealer.points <= player.points:
            dealer.hand.append(deck.deal())
            dealer.update_points()
            print("Dealer Hits")
            print(dealer,"\n")
            '''
def Hit(player,deck):
    player.hand.append(deck.deal())
    player.update_points()
    print(player)
