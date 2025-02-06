# File: game.py

# Imports
import random
from projects.project1.multideck import MultiDeck
from projects.project1.cards import Card

# Implimentation

# Game class
class Game:

    def __init__(self, num_decks: int) -> None:
        """Initailizes the Game class.
        
        Args:
            num_decks (int): number of 52-card decks to play with
        Returns:
            None
        """
        # make and shuffle draw pile, make player and dealer variables
        self._draw_pile: list[Card] =  MultiDeck(num_decks).ordered_cards
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
            response = input("Would you like to (H)it or (S)tay?").upper()
            if response == "H": # give player card, continue loop
                self.hit()
                running = self.check_for_end()
            elif response == "S": # dealer draws, 
                self.stay()
                running = False
                self.check_for_end()
            else:
                print("Input not recognized")
        
        # playing again or not
        return self.determine_winner()
            
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
        self.dealer_draw()
        self.player_draw()
        self.dealer_draw()
        self.player_draw()
        self.show_scores()

    def show_scores(self) -> None:
        """Method to print the hands and scores of the player and dealer.
        
        Args:
            None
        Returns:
            None
        """
        # empty the displays
        self._player_display: list[list] = []
        self._dealer_display: list[list] = []
        
        for card in self._player_hand:
            self._player_display += ([card.face+card.suit])
        
        for card in self._dealer_hand:
            self._dealer_display += ([card.face+card.suit])
        
        print(f"Player Hand: {self._player_display} | Score: {self._player_score}")
        print(f"Dealer Hand: {self._dealer_display} | Score: {self._dealer_score}")

    def check_for_end(self) -> bool:
        """Method to check if the game has ended yet. If a hand is over 21
        change any Ace cards from 11 to 1, upate scores.
        
        Args:
            None
        Returns:
            Bool: True if the game is still running, False otherwise
        """
        # if neither has reached 21 the game continues
        if self._player_score <= 21 and self._dealer_score <= 21:
            return True
        
        # if the hands have aces readjust their total score to be 1 per Ace
        for card in self._player_hand:
            if card.face == "A":
                card.value = 1
                self._player_score += (card.value for card in self._player_hand)
        for card in self._dealer_hand:
            if card.face == "A":
                card.value = 1  
                self._dealer_score += (card.value for card in self._dealer_hand)
 
        # check again for both hands under 21
        if self._player_score <= 21 and self._dealer_score <= 21:
            return True
        else:
            return False
    
    def determine_winner(self) -> bool:
        """Method to determine who won the game and print the outcome.
        Prompts if the player would like to start another game.
        
        Args:
            None
        Returns:
            bool: True if a new game should start, False otherwise
        """
        if self._player_score > 21:
            print("Bust! Dealer wins :(")
        elif self._player_score == 21:
            print("BlackJack! Player won! :)")
        elif self._dealer_score == 21:
            print("BlackJack! Dealer won! :(")
        
        # determine if playing again and return bool
        restart = input("Would you like to play again? (Y/N)").upper()
        if restart == "Y":
            return True
        else: 
            return False
        
    def hit(self) -> None:
        """Method to impliment Hitting in BlackJack. Adds a card to hand and updates score.
        Prints the current scores.
        Args:
            None
        Returns:
            None"""
        self.player_draw()
        self.show_scores()
    
    def stay(self) -> None:
        """Method to draw cards for dealer until they reach 17.
        Updates and prints the curent scores.
        
        Args:
            None
        Returns:
            None
        """
        while self._dealer_score < 17:
            self.dealer_draw()
            self._dealer_score += (int(card.value) for card in self._dealer_hand)
        self.show_scores()

    def dealer_draw(self) -> None:
        """Method to add a card to the dealer's hand. Updates dealer score.
        
        Args:
            None
        Returns:
            None
        """
        card = self._draw_pile.pop(0)
        self._dealer_hand.append(card)
        self._dealer_score += card.value

    def player_draw(self) -> None:
        """Method to add a card to the player's hand. Updates player score.
        
        Args:
            None
        Returns:
            None
        """
        card = self._draw_pile.pop(0)
        self._player_hand.append(card)
        self._player_score += card.value

