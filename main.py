#A simple but hopefully efficient terminal
#Python Blackjack.
import random

deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

### deal the computer 2 cards and check if it is a black jack and display how many points the showing card is worth###

def check_winner(player_points, computer_points):
    global game_is_on
    print(f'The computer cards were {computer_cards} ({computer_points} points)')
    if player_points > computer_points:
        print(f"player wins!! you made {player_points} and the computer only {computer_points}")
        game_is_on = False
        
    elif computer_points > player_points:
        print(f"computer wins!! you made {player_points} and the computer made {computer_points}")
        game_is_on = False

    elif computer_points == player_points:
        print(f'its a tie with {player_points}')
        game_is_on = False
    
def get_computer_cards():
    computer_cards = []
    computer_cards.append(deck[random.randint(0, 12)])
    computer_cards.append(deck[random.randint(0, 12)])
    return computer_cards

def get_player_cards():
    player_cards = []
    player_cards.append(deck[random.randint(0, 12)])
    player_cards.append(deck[random.randint(0, 12)])
    return player_cards

def calculate_computer_points():
    computer_points = 0
    for i in computer_cards:
        if i == 'A' or i == 'J' or i == 'Q' or i == 'K' :
            computer_points += 10
        else:
            computer_points += i
    return computer_points
        
def calculate_player_points():
    player_points = 0
    for i in player_cards:
        if i == 'A' or i == 'J' or i == 'Q' or i == 'K' :
            player_points += 10
        else:
            player_points += i
    return player_points

game_is_on = True

while game_is_on:
    print('Welcome to the ultimate blackjack')
    
    computer_cards = get_computer_cards()
    computer_points = calculate_computer_points()
    
    player_cards = get_player_cards()
    player_points = calculate_player_points()
    
    print(f'the computer has dealt to himself {computer_cards[0]} and HIDDEN CARD')
    print(f'the computer has dealt for you {player_cards}. (Thats {player_points} points)')

    user_first_answer = input('do you wanna hit or stand? ')
    
    if user_first_answer == 'hit':
        player_cards.append(deck[random.randint(0, 12)])
        player_points = calculate_player_points()
        print(f'{player_cards} ({player_points})')
        if player_points == 21:
            print('you win')
            print(f'computer cards were {computer_cards}')
            game_is_on = False
        elif player_points > 21:
            print(f'game over.')
            print(f'computer cards were {computer_cards}')
            game_is_on = False
        else:
            second_answer = input(f'now you have {player_points}. Do you wanna hit or stand? ')
            if second_answer == 'hit':
                player_cards.append(deck[random.randint(0, 12)])
                player_points = calculate_player_points()
                print(f'{player_cards} ({player_points})')
                if player_points == 21:
                    print('you win')
                    print(f'computer cards were {computer_cards} ({computer_points})')
                    game_is_on = False
                elif player_points > 21:
                    print(f'game over.')
                    print(f'computer cards were {computer_cards} ({computer_points})')
                    game_is_on = False
                else:
                    third_answer = input(f'Damn. What are the odds. You have {player_points}. Do you wanna hit or stand?')
                    if third_answer == 'hit':
                        player_cards.append(deck[random.randint(0, 12)])
                        player_points = calculate_player_points()
                        print(f'{player_cards} ({player_points})')
                        if player_points == 21:
                            print('you win')
                            print(f'computer cards were {computer_cards} ({computer_points})')
                            game_is_on = False
                        elif player_points > 21:
                            print(f'game over.')
                            print(f'computer cards were {computer_cards} ({computer_points})')
                            game_is_on = False
                    elif third_answer == 'stand':
                        check_winner(player_points,computer_points)
            elif second_answer == 'stand':
                        check_winner(player_points,computer_points)            
    elif user_first_answer == 'stand':
        check_winner(player_points,computer_points)  

#print(f'The computer cards are {compustandter_cards} it has made {computer_points} points')
### deal the computer 2 cards, check if it is a black jack and display how many points youve made ###
### show player cards


###ask the player to hit of stand


### if hits, recalculate the points and repeat the option to hit or stand

###if stands, show the hidden computer cards, calculate how much is that worth it , and check who wins

### after the game is over, ask for player to write q for quit and r to replay