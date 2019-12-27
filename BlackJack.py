import random
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Cards:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


""" card = Cards('heart', 'Six')
print(card)
print(card.rank)
print(values[card.rank])
card.__str__() """


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Cards(suit, rank))

    def __str__(self):
        deck_component = ''
        for card in self.deck:
            deck_component += card.__str__()+','+' '
        return deck_component

    def shuffle(self):
        random.shuffle(self.deck)
        # return self.deck

    def deal(self):
        card_draw = self.deck.pop()
        return card_draw


""" deck1 = Deck()
print(deck1)
deck1.shuffle()
print(deck1)
card_draw = deck1.deal()
print(card_draw)
 """


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


test_deck = Deck()
test_deck.shuffle()
test_player = Hand()
test_player.add_card(test_deck.deal())
print(test_player.value)
test_player.add_card(test_deck.deal())
# print(test_deck.deal())
print(test_player.value)
print(test_player.value)


class Chips:
    def __init__(self):
        self.balance = int(
            input('how much would you insert into your total? '))
        self.bet = 0

    def win_bet(self):
        self.balance += self.bet

    def lose_bet(self):
        self.balance -= self.bet


def take_bet(chips):

    while True:
        try:
            chips.bet = int(input('How much do you like to bet? '))
        except ValueError:
            print('Your value should be an integer')
        else:
            if chips.bet > chips.balance:
                print('Sorry, your bet is more than your balance', chips.total)
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
