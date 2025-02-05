# File: multideck.py

# Imports
from projects.project1.decks import Deck
from projects.project1.cards import Card
from datastructures.bag import Bag
import random

# Implimentation

# MultiDeck class
class MultiDeck:

    def __init__(self, num_decks: int) -> None:
        """Constructor for MultiDeck class, creates a Bag 
        to stores Card objects in and a List to order the
        cards.
        
        Args:
            num_decks: how many decks should be added
        Returns:
            None
        """
        self._ordered_cards: list[Card] = []
        self._cards: Bag = Bag()
        
        #add multiple Decks
        for i in range(num_decks):
            self.add(Deck())

    def add(self, deck: Deck) -> None:
        """Method to add a Deck of cards.
        
        Args:
            deck: Deck object
        Returns: 
            None
        """
        #add cards to the Bag
        for card in deck.cards:
            self._cards.add(card)
        
        #add cards to the list for an order
        for card in self._cards:
            self._ordered_cards.append(card)
    
    @property
    def ordered_cards(self):
        """ordered cards property, list[Card]"""
        return self._ordered_cards