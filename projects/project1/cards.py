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


class CardFace(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    JACK = 10
    QUEEN = 10
    KING = 10
    ACE = 11

card_faces: list[int] = [face.value for face in CardFace]
"""
card_faces: dict = {
    'ONE':1, 
    'TWO':2, 
    'THREE':3, 
    'FOUR':4, 
    'FIVE':5, 
    'SIX':6, 
    'SEVEN':7,
    'EIGHT':8,
    'NINE':9,
    'TEN':10,
    'JACK':10,
    'QUEEN':10,
    'KING':10,
    'ACE':10
    }
"""
class Card():

    def __init__(self, face, suit) -> None:
        card_face: CardFace = face.

        card_suit: CardSuit = suit
        card_value: int = face.value

if __name__ == '__main__':
    print(card_suits)
    print(card_faces)