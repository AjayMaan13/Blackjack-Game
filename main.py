# This is the file containing the project code 

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

Player_cards = []
Dealer_cards = []


class Deck:

    def __init__(self):
        # this only happens once upon creation of a new Deck
        self.value_cards = {}
        # This dict is used to get values of a card by generating card: value dict
        self.all_cards = []
        # This is the main list from where we will pop elements

        for suit in suits:
            for rank in ranks:
                if rank == 'Ace':
                    self.value_cards[f'{rank} of {suit}'] = 11
                else:
                    self.all_cards.append(f'{rank} of {suit}')  # appending like-'Two of Hearts'
                    self.value_cards[f'{rank} of {suit}'] = values[rank]

    def shuffle(self):
        # Note this doesn't return anything
        random.shuffle(self.all_cards)

    def hit_one(self):
        # Note we remove one card from the list of all_cards
        return self.all_cards.pop(0)


class Player:

    def __init__(self, name, money=2000):
        self.name = name
        self.money = money
        self.all_cards = []
        pass

    def __str__(self):
        return f'Player {self.name} has balance ' + str(self.money)  # ERROR SOLVED

    def bet(self):

        while True:  # Easy way for input
            try:
                self.bet_amount = int(input("Enter your Bet amount: "))
                self.money = self.money - self.bet_amount
                return f'Your bet is {self.bet_amount}'
            except ValueError:
                print("Integer, please.")

    def add_money(self, addmoney):
        self.addmoney = addmoney
        self.money += self.addmoney


value = 0

game_on = True
game_in = True
game_in_in = True
game_in_out = True


def value_check(list1):
    global value
    value = 0  # value=0 sets value=0 when next time using the function
    for n in list1:
        value += newdeck.value_cards[n]
    return int(value)


def value_21(list1):
    if value_check(list1) > 21:
        global game_in_out, game_in_in, game_in
        game_in_in = False
        game_in = False
        game_in_out = False
        return


def value_17(list1):
    if value_check(list1) > 17:
        global game_in_out
        game_in_out = False

        return


Player_name = input('Player Enter your name: ')
player = Player(Player_name)
rounds = 1
decision_play = True
decision = ''

newdeck = Deck()
newdeck.shuffle()
print(player)
for i in range(0, 2):
    Player_cards.append(newdeck.hit_one())
    Dealer_cards.append(newdeck.hit_one())
for i in Player_cards:
    print(f'{Player_name} has card: {i}')
print(f'Dealer have 1 card {Dealer_cards[0]} and other is hidden')

while game_on:  # outer part of game containing round print and bet taking

    player.bet()
    print(f'Round {rounds} begin: ')

    while game_in:
        while game_in_in:
            value_21(Player_cards)
            decision = input(f'{Player_name} what do you want to do Hit or Stay : ')
            if decision.lower() == "hit":
                Player_cards.append(newdeck.hit_one())
                print(f'Player {Player_name} have card: {Player_cards[-1]}')

                value_21(Player_cards)

            elif decision.lower() == "stay":
                game_in_in = False

            else:
                print('Enter a valid input! Hit or stay')
        for j in Dealer_cards:
            # For displaying all dealer cards
            print(f'Dealer have card: {j}')
        while game_in_out:
            value_17(Dealer_cards)
            Dealer_cards.append(newdeck.hit_one())
            # Displaying the last added card of dealer
            print(f'Dealer have card: {Dealer_cards[-1]}')
            value_17(Dealer_cards)

        if value_check(Player_cards) > value_check(Dealer_cards):
            print(f'🎉 Congratulations {Player_name} you have won the bet 🎉')
            # When player wins he recieves 2 times the bet
            player.add_money(2 * player.bet_amount)
        else:
            game_in = False

    print('Youe have lost your bet. Try again 😔')
    while decision_play:

        decision = input('Do you want to play another round: type Yes or No')
        if decision.lower() == 'yes':
            break
        elif decision.lower() == 'no':
            game_on = False
            decision_play = False
        else:
            print('Type yes or no only: ')
    rounds += 1
    print(player)





