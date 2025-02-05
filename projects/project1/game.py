# File: game.py

import random
from projects.project1.multideck import MultiDeck
from projects.project1.cards import Card

class Game:

    def __init__(self, num_decks: int) -> None:
        init_draw_pile = MultiDeck(num_decks)
        self._draw_pile: list[Card] = init_draw_pile.ordered_cards
        self.shuffle()
        self._player_hand: list[Card] = []
        self._dealer_hand: list[Card] = []
        self._player_score: int = 0
        self._dealer_score: int = 0
        self._player_display: list[list] = []
        self._dealer_display: list[list] = []
    
    def start_game(self) -> None:
        """ Starts the game. Algorithm: 
            1. While no score is above 21, do the following:
                1.1. Deal 2 cards to player and dealer.
                1.2. Allow Player to Hit or Stay.
                1.3. When Player busts/Stays, break the loop.
            2. Print the result of the battle.
        """
        # set up
        self.deal()
        
        # game loop
        running = True
        while running:
            running = self.check_for_end()
            

    def shuffle(self) -> None:
        """Method to randomize the order of cards in the 
        _draw_pile.

        Args:
            None
        Returns:
            None
        """
        random.shuffle(self._draw_pile)
    
    def deal(self) -> None:
        """Deals two cards to each player and displays the 
        current scores.

        Args: 
            None
        Returns:
            None
        """
        # alternates dealing one card to player and dealer
        self._dealer_hand.append(self._draw_pile.pop(0))
        self._player_hand.append(self._draw_pile.pop(0))
        self._dealer_hand.append(self._draw_pile.pop(0))
        self._player_hand.append(self._draw_pile.pop(0))
        self.show_scores()

    def show_scores(self):
        for card in self._player_hand:
            self._player_score += card.value
            self._player_display.append([''.join(card.face,card.suit)])
        
        for card in self._dealer_hand:
            self._dealer_score += card.value
            self._dealer_display.append([''.join(card.face,card.suit)])
        print(f"Player Hand: {self._player_display} | Score: {self._player_score}")
        print(f"Dealer Hand: {self._dealer_display} | Score: {self._dealer_score}")

    def check_for_end(self) -> bool:
        """Method to check if the game has ended yet.
        
        Args:
            None
        Returns:
            Bool: True of the game is still running, False otherwise
        """
        pass