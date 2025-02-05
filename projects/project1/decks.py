#File: decks.py

# Imports
from datastructures.bag import Bag
from projects.project1.cards import Card, card_suits, card_faces

# Implimantation
class Deck:

    def __init__(self) -> None:
        """Constructor for Deck class, creates a Bag object and stores Card objects in it.
        Args:
            None
        Returns:
            None
        """
        self._deck = Bag()
        for suit in card_suits:
            for face in card_faces:
                self._deck.add(Card(face, suit))
        
if __name__ == '__main__':
    print(Deck())