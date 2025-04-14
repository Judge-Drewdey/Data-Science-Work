import random

deck = {'A of Spades':[1,11], 'A of Clubs':[1,11], 'A of Diamonds':[1,11], 'A of Hearts':[1,11],'2 of Spades':2, '2 of Clubs':2,
        '2 of Diamonds':2, '2 of Hearts':2,'3 of Spades':3, '3 of Clubs':3, '3 of Diamonds':3, '3 of Hearts':3, '4 of Spades':4,
        '4 of Clubs':4, '4 of Diamonds':4, '4 of Hearts':4, '5 of Spades':5, '5 of Clubs':5, '5 of Diamonds':5, '5 of Hearts':5,
        '6 of Spades':6, '6 of Clubs':6, '6 of Diamonds':6, '6 of Hearts':6, '7 of Spades':7, '7 of Clubs':7, '7 of Diamonds':7,
        '7 of Hearts':7, '8 of Spades':8, '8 of Clubs':8, '8 of Diamonds':8, '8 of Hearts':8,'9 of Spades':9, '9 of Clubs':9,
        '9 of Diamonds':9, '9 of Hearts':9, '10 of Spades':10, '10 of Clubs':10, '10 of Diamonds':10, '10 of Hearts':10,
        'J of Spades':10, 'J of Clubs':10, 'J of Diamonds':10, 'J of Hearts':10,'Q of Spades':10, 'Q of Clubs':10, 'Q of Diamonds':10,
        'Q of Hearts':10, 'K of Spades':10, 'K of Clubs':10, 'K of Diamonds':10, 'K of Hearts':10}

play = 'y'
while play == 'y':
    new_deck = deck.copy()

    #Deal two cards to dealer
    dealer_hand = random.sample(list(deck.keys()),2)

    #Remove those cards from the deck and display cards
    for card in dealer_hand:
        new_deck.pop(card)
    print("The Dealer's face up card is: ", dealer_hand[0])

    #Deal two cards to user
    user_hand = random.sample(list(deck.keys()),2)

    #Remove those cards from the deck and display cards
    for card in user_hand:
        new_deck.pop(card)
    print('')
    print('Your cards are: ', user_hand, '.')

    dealer_value = 0
    ace_value = 0

    #Find value of dealers hand
    for c in dealer_hand:
        if c[0] != 'A':
            dealer_value += deck[c]

        elif (11 + dealer_value) < 21:
            ace_value = 11
            dealer_value += ace_value
        else:
            ace_value = 1
            dealer_value += ace_value

    #Decide if dealer should hit
    while dealer_value < 17:
        hit_card = random.sample(list(deck.keys()), 1)
        if hit_card[0][0] != 'A':
            dealer_value += deck[hit_card[0]]

        elif (11 + dealer_value) < 21:
            ace_value = 11
            dealer_value += ace_value

        else:
            ace_value = 1
            dealer_value += ace_value


    # Declare user value
    user_value = 0
    # Loop though hand and deal with Aces
    for c in user_hand:
        if c[0] != 'A':
            user_value += deck[c]
        else:
            print('')
            ace_value = input('What would you like this Ace to be(1/11)?')
            if ace_value == '1':
                user_value += 1
            elif ace_value == '11':
                user_value += 11
            else:
                retry_message = 99
                while retry_message != 1 and retry_message != 11:
                    retry_message = int(input('Invalid Value. Would you like to try again? Options are 1 and 11'))
                user_value += retry_message
    print('')
    print('Your current value is: ', user_value)
    print('')
    hit = input('Would you like to hit? (y/n)')
    while hit == 'y' and user_value < 21:
        hit_card = random.sample(list(deck.keys()), 1)
        if hit_card[0][0] != 'A':
            user_value += deck[hit_card[0]]
        else:
            print('')
            ace_value = input('What would you like this Ace to be(1/11)?')
            if ace_value == '1':
                user_value += 1
            elif ace_value == '11':
                user_value += 11
            else:
                retry_message = 99
                while retry_message != 1 and retry_message != 11:
                    retry_message = int(input('Invalid Value. Would you like to try again? Options are 1 and 11'))
                user_value += retry_message
                print('')
        print('Your current value is: ', user_value)
        print('')
        if user_value < 21:
            hit = input('Would you like to hit? (y/n)')
    print('')
    print('You have: ',user_value)
    print('')



    if user_value > 21:
        print('You Lose!')
    elif user_value <= 21 and dealer_value == user_value:
        print('The dealer has: ', dealer_value)
        print('')
        print('Push')

    elif user_value <= 21 and dealer_value <= 21 and user_value > dealer_value:
        print('The dealer has: ', dealer_value)
        print('')
        print('You Win!')
    elif user_value <= 21 and dealer_value <= 21 and user_value < dealer_value:
        print('The dealer has: ', dealer_value)
        print('')
        print('You Lose!')
    else:
        print('The dealer has: ', dealer_value)
        print('')
        print('You Win')
    print('')

    play == input('Do you want to play again? (y/n)')
    print('')
    print('')
