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

# not an enum because duplicate values make aliases that just refer back to the first
# you can stop it from aliasing with but then you cant iterate through the enum
# unique() means only one name for any value, opposite of what we need
# NamedConstant works but you can't iterate through it
# NoAlias works ut you cant lookup by value

# 13 faces stored in a dictionary + turned into a list of strings
CardFace: dict = { # tuples: (face, value)
    'TWO' : ('2', 2),
    'THREE' : ('3', 3),
    'FOUR' : ('4', 4),
    'FIVE' : ('5', 5),
    'SIX' : ('6', 6),
    'SEVEN' : ('7', 7),
    'EIGHT' : ('8', 8),
    'NINE' : ('9', 9),
    'TEN' : ('10', 10),
    'JACK' : ('J', 10),
    'QUEEN' : ('Q', 10),
    'KING' : ('K', 10),
    'ACE' : ('A', 11)
}

card_faces: list[str] = [face for face in CardFace]

# Card class
class Card():

    def __init__(self, face, suit) -> None:
        """Constructor for Card class.
        
        Args:
            face: string, a CardFace dict key
            suit: string, in CardSuit enum
        Returns:
            None
        """
        self._card_face: str = CardFace[face][0] # display to players
        self._card_suit: CardSuit = suit # display to players
        self._card_value: int = CardFace[face][1] # sum for score

    @property
    def face(self):
        """Card face property, string"""
        return self._card_face
    
    @property
    def suit(self):
        """Card suit property, string"""
        return self._card_suit
    
    @property
    def value(self):
        """Card value property, int"""
        return self._card_value

    @value.setter
    def value(self, value: int):
        """Card value setter, int"""
        self._card_value = value

if __name__ == '__main__':
    pass
    #print(card_suits)
    #print(card_faces)