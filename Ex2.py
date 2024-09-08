import random

def roll_dice(sides):
    return random.randint(1, sides)

sides = int(input("Enter the number of sides on your dice: "))

roll_count = 0
while True:
    result = roll_dice(sides)
    roll_count += 1
    print(f"Roll {roll_count}: {result}")

    if result == sides:
        print(f"You rolled the maximum number ({sides}) after {roll_count} attempts!")
        break