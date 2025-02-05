# File: multideck.py

# Imports
from projects.project1.decks import Deck
from projects.project1.cards import Card
import random

# Implimentation
class MultiDeck:

    def __init__(self, num_decks) -> None:
        """Constructor for MultiDeck class, creates a List and stores Card objects in it.
        Args:
            Decks (Optional): Deck objects
        Returns:
            None
        """
        self._draw_pile: list[Card] = []
        for i in range(num_decks):
            self.add(Deck())

    def add(self, deck) -> None:
        for card in deck._deck:
            self._draw_pile.append(card)

    def shuffle(self) -> None:
        random.shuffle(self._draw_pile)