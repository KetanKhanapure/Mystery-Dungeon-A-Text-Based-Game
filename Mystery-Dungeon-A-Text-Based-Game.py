
import random

def start_game():
    print("Welcome to Mystery Dungeon!")
    print("Your mission: find the hidden treasure while surviving traps, monsters, and surprises!\n")
    enter_dungeon()

def enter_dungeon():
    print("The dungeon entrance looms before you. Enter?")
    choice = input("Type 'yes' to enter or 'no' to leave: ").lower()
    if choice == 'yes':
        mysterious_guide()
    elif choice == 'no':
        print("You turn back. The treasure remains hidden.")
    else:
        print("Invalid choice. Try again.")
        enter_dungeon()

def mysterious_guide():
    print("\nA hooded figure approaches. 'I can guide you,' they say. Trust them?")
    choice = input("Type 'trust' to accept or 'ignore' to continue alone: ").lower()
    if choice == 'trust':
        print("The guide gives you a glowing map. 'It shows only part of the truth,' they warn.")
        first_path()
    elif choice == 'ignore':
        print("You ignore them. Their eerie laughter fades as you move ahead.")
        first_path()
    else:
        print("Invalid choice. Try again.")
        mysterious_guide()

def first_path():
    print("\nYou reach a fork in the path: Left (flickering torches) or Right (darkness).")
    choice = input("Type 'left' or 'right': ").lower()
    if choice == 'left':
        encounter_monster()
    elif choice == 'right':
        secret_door()
    else:
        print("Invalid choice. Try again.")
        first_path()

def encounter_monster():
    print("\nA monster blocks your path! Fight, flee, or bribe?")
    choice = input("Type 'fight', 'flee', or 'bribe': ").lower()
    if choice == 'fight' and random.choice([True, False]):
        print("You defeat the monster! You find a healing potion.")
        find_treasure()
    elif choice == 'flee':
        print("You escape but stumble into a trap!")
        trap_room()
    elif choice == 'bribe' and random.choice([True, False]):
        print("The monster accepts your gold and lets you pass.")
        find_treasure()
    else:
        print("You are defeated. Game over.")

def secret_door():
    print("\nYou find a hidden door. Open it?")
    choice = input("Type 'open' to open or 'ignore' to move on: ").lower()
    if choice == 'open' and random.choice([True, False]):
        print("You find cursed treasure and are trapped forever. Game over.")
    elif choice == 'open':
        print("You find rare gems and escape! You win!")
    else:
        print("You leave the door and continue.")
        find_treasure()

def trap_room():
    print("\nYou’re trapped in a spike-filled room with a ticking timer!")
    choice = input("Type 'disarm' to disarm the trap or 'search' to find an exit: ").lower()
    if choice == 'disarm' and random.choice([True, False]):
        print("You disarm the trap and escape safely.")
        find_treasure()
    elif choice == 'search':
        print("You find a hidden exit and escape!")
        find_treasure()
    else:
        print("The trap activates. Game over.")

def find_treasure():
    print("\nAt the end of the dungeon, you find a treasure chest. Open it?")
    choice = input("Type 'open' to open or 'leave' to walk away: ").lower()
    if choice == 'open' and random.choice([True, False]):
        print("The chest contains the hidden treasure! You win!")
    elif choice == 'open':
        print("The chest was a mimic! It devours you. Game over.")
    else:
        print("You leave the chest and exit the dungeon safely.")

# Start the game
start_game()