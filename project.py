import random

def roll_dice():
    value = random.randint(1, 6)
    dice_faces = {
        1: ("-----", "|   |", "| o |", "|   |", "-----"),
        2: ("-----", "|o  |", "|   |", "|  o|", "-----"),
        3: ("-----", "|o  |", "| o |", "|  o|", "-----"),
        4: ("-----", "|o o|", "|   |", "|o o|", "-----"),
        5: ("-----", "|o o|", "| o |", "|o o|", "-----"),
        6: ("-----", "|o o|", "|o o|", "|o o|", "-----")
    }
    for line in dice_faces[value]:
        print(line)
    print(f"🎲 You rolled a {value}!\n")

def toss_coin():
    result = random.choice(["Heads", "Tails"])
    print(f"🪙 The coin landed on: {result}!\n")

def main():
    print("🎮 Welcome to Dice Roll & Coin Toss Game!")
    while True:
        print("What would you like to do?")
        print("1. Roll a Dice"