import random


def deal_card(player: list, all_cards: list):
    """
    This function takes in a list of cards and returns a string of the cards in the list
    
    :param player: list
    :type player: list
    :return: a string.
    """
    card = random.choice(all_cards)
    player.append(card)
    all_cards.remove(card)



def total(player: list) -> int:
    """
    The function `total` takes a list of cards as an argument and returns the sum of the values of those
    cards
    
    :param player: list
    :type player: list
    :return: The total value of the cards in the player's hand.
    """
    total = 0
    for card in player:
        total += card.value

    return total


def reveal_dealer_hand(dealerHand: list):
    """
    Given a list of cards in the dealer's hand, return a list of the cards that are face up
    
    :param dealerHand: list of cards in the dealer's hand
    :type dealerHand: list
    :return: The first two cards in the dealer's hand.
    """
    out = []
    if len(dealerHand) == 2:
        out.append(dealerHand[0])
    elif len(dealerHand) > 2:
        out.append(dealerHand[0])
        out.append(dealerHand[1])
    return out


def print_hand(Hand: list):
    """
    Prints the cards in a hand
    
    :param Hand: a list of Card objects
    :type Hand: list
    :return: A string of the cards in the hand.
    """
    out = ""

    for card in Hand:
        out += "" + card.to_string()
        out += "\n "
    return out

