from deck import Deck


deck = Deck()
deck.shuffle()

x = deck.issue_card()
print(x)
print(len(deck.cards))
x = deck.issue_card()
print(x)
print(len(deck.cards))
x = deck.issue_card()
print(x)
print(len(deck.cards))