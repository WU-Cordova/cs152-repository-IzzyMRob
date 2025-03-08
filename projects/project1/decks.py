#File: decks.py

# Imports
from projects.project1.cards import Card, card_suits, card_faces
from datastructures.bag import Bag

# Implimantation

# Deck class
class Deck:

    def __init__(self) -> None:
        """Constructor for Deck class, creates a Bag object and stores 52 Card objects in it.
        
        Args:
            None
        Returns:
            None
        """
        self._cards: Bag = Bag()
        
        # add one of every card
        for suit in card_suits:
            for face in card_faces:
                self._cards.add(Card(face, suit))

    @property
    def cards(self):
        """Deck cards property, Bag"""
        return self._cards