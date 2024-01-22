import random

class DiceRoller:
    def __init__(self, sides, num_dice):
        self.sides = sides
        self.num_dice = num_dice

    def roll_dice(self):
        return [random.randint(1, self.sides) for _ in range(self.num_dice)]

    def roll_multiple_times(self, num_times):
        return [self.roll_dice() for _ in range(num_times)]

def main():
    sides = int(input("Enter the number of sides on the dice: "))
    num_dice = int(input("Enter the number of dice: "))
    num_times = int(input("Enter how many times to roll the dice: "))

    dice_roller = DiceRoller(sides, num_dice)

    results = dice_roller.roll_multiple_times(num_times)

    print(f"Results of rolling {num_dice} {sides}-sided dice {num_times} times:")
    for i, result in enumerate(results, 1):
        print(f"Roll {i}: {result}")

if __name__ == "__main__":
    main()
