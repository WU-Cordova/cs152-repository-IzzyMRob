# File: cards.py

# Imports
from aenum import Enum

# Implimentation

# Four suits stored in an enum + turned into a list of strings
class CardSuit(Enum):
    HEARTS: str = "♡"
    SPADES: str = "♠"
    CLUBS: str = "♣"
    DIAMONDS: str = "◇"

card_suits: list[str] = [suit.value for suit in CardSuit]

# 13 faces stored in a dictionary + turned into a list of strings
CardFace: dict = { # tuples: (displayed_char, score, *secondary score)
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

# Card class
class Card():

    def __init__(self, face, suit) -> None:
        """Constructor for Card class.
        
        Args:
            face: string, CardFace dict key
            suit: string, CardSuit enum
        Returns:
            None
        """
        self._card_face: str = CardFace[face][0]
        self._card_suit: CardSuit = suit
        self._card_value: int = CardFace[face][1]

    @property
    def face(self):
        """card face property, string"""
        return self._card_face
    
    @property
    def suit(self):
        """card suit property, string"""
        return self._card_suit
    
    @property
    def value(self):
        """card value property, int"""
        return self._card_value

if __name__ == '__main__':
    pass
    #print(card_suits)
    #print(card_faces)