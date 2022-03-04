import random


# deal a Card
def deal_card(player: list, all_cards: list):
    card = random.choice(all_cards)
    player.append(card)
    all_cards.remove(card)


# returns total amount of the player that's on the turn as INT
def total(player: list) -> int:
    total = 0
    for card in player:
        total += card.value

    return total


# show 1/2 cards as the amount of cards increases
def reveal_dealer_hand(dealerHand: list):
    out = []
    if len(dealerHand) == 2:
        out.append(dealerHand[0])
    elif len(dealerHand) > 2:
        out.append(dealerHand[0])
        out.append(dealerHand[1])
    return out


# returns own hand as string
def print_hand(Hand: list):
    out = ""

    for card in Hand:
        out += "" + card.to_string()
        out += "\n "
    return out
