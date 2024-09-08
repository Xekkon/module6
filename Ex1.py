import random

def roll_dice():
    return random.randint(1, 6)

def main():
    roll_count = 0
    while True:
        result = roll_dice()
        roll_count += 1
        print(f"Roll {roll_count}: {result}")
        if result == 6:
            print(f"You rolled a 6 after {roll_count} attempts!")
            break

if __name__ == "__main__":
    main()