import random
from character import Character

class Game:
    def __init__(self, player1: Character, player2: Character) -> None:
        """ Constructor for the Game class. Sets the players to instance variables.
        Args:   
            player1 (Character): The first player.
            player2 (Character): The second player.
        """
        self.p1 = player1
        self.p2 = player2

    def attack(self, attacker: Character, defender: Character) -> bool:
        """ Attacks the defender. Algorithm: 
            1. Roll a random number between 1 and 6 for the attack.
            2. Subtract the attack value from the defender's health.
            3. If the defender's health is less than or equal to 0, they are defeated.
            4. Print the result of the attack.
        Args:
            attacker (Character): The attacker.
            defender (Character): The defender. 
        Returns:
            bool: True if the defender was killed, False if otherwise
        """
        # 1
        dice_result = random.randint(1,6)
        damage_dealt = dice_result * attacker.attack_power
        # 2
        defender.health -= damage_dealt
        # 3
        if defender.health < 1:
            print(f"{attacker.name} the {attacker.character_type.value} dealt {damage_dealt} damage to {defender.name}!")
            print(f"**{attacker.name} vanquished {defender.name}!**")
            return True
        else:
            print(f"{attacker.name} the {attacker.character_type.value} dealt {damage_dealt} damage to {defender.name}!")
            print(f"  {defender.name}'s health is now {defender.health}.")        
            return False    

    def start_battle(self) -> None:
        """ Starts the battle between the two players. Algorithm: 
            1. While both players are alive, do the following:
                1.1. Player 1 attacks Player 2.
                1.2. If Player 2 is defeated, break the loop.
                1.3. Player 2 attacks Player 1.
                1.4. If Player 1 is defeated, break the loop.
            2. Print the result of the battle.
        """
        game_over = False
        while game_over == False:
            if not game_over:
                game_over = self.attack(self.p1, self.p2)
            if not game_over:
                game_over = self.attack(self.p2, self.p1)
        