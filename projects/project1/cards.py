# File: cards.py

# Imports
from aenum import Enum

# Implimentation
class CardSuit(Enum):
    HEARTS: str = "♡"
    SPADES: str = "♠"
    CLUBS: str = "♣"
    DIAMONDS: str = "◇"

card_suits: list[str] = [suit.value for suit in CardSuit]

CardFace: dict = { # tuples: (displayed_char, score)
    'ONE' : ('1', 1),
    'TWO' : ('2', 2),
    'THREE' : ('3', 3),
    'FOUR' : ('4', 4),
    'FIVE' : ('5', 5),
    'SIX' : ('6', 6),
    'SEVEN' : ('7', 7),
    'EIGHT' : ('8', 8),
    'NINE' : ('9', 9),
    'JACK' : ('J', 10),
    'QUEEN' : ('Q', 10),
    'KING' : ('K', 10),
    'ACE' : ('A', 11, 1)
}

card_faces: list[str] = [face for face in CardFace]

class Card():

    def __init__(self, face, suit) -> None:
        """Constructor for Card class.
        Args:
            face: string? CardFace enum
            suit: string, CardSuit enum
        Returns:
            None
        """
        card_face: str = CardFace[face][0]
        card_suit: CardSuit = suit
        card_value: int = CardFace[face][1]

if __name__ == '__main__':
    print(card_suits)
    print(card_faces)