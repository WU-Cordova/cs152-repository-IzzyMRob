from game import Game
from character import Character
from charactertype import CharacterType

alice = Character(name="Alice", character_type=CharacterType.WARRIOR, health=100, attack_power=10)
bob = Character(name="Bob", character_type=CharacterType.MAGE, health=70, attack_power=5)

game = Game(alice, bob)
game.start_battle()