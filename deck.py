class Card:
    # constructor for cards
    def __init__(self, name, colour, value: int):
        self.colour = colour
        self.name = name
        self.value = value

    # returns the card as string
    def to_string(self):
        return self.colour + " " + self.name


# returns the full gamedeck with cards as Objects
def game_deck():
    colours = ["Hearts", "Clubs", "Diamonds", "Spades"]
    names = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    output = []
    for colour in colours:
        for i in range(len(names)):
            output.append(Card(names[i], colour, i + 2 if i <= 9 else 10))
        output.append(Card("Ace", colour, 11))
    return output
