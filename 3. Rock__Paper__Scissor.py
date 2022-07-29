import random

user_wins = 0
comp_wins = 0
draw = 0

options = ["rock", "paper", "scissor"]

while True:
    user_input = input("Type Rock/Paper/Scissor or Q to quit:  ").lower()
    if user_input == 'q':
        break
    if user_input not in options:
        continue

    random_num = random.randint(0,2)
    computer_picked = options[random_num]
    print(f"Computer picked: {computer_picked}")

# If two values are equal, declare a tie!
    if user_input == computer_picked:
        print("It's a Tie")
        draw += 1

# Check for all possibilities when computer chose "Rock"
    if computer_picked == 'rock':
        if user_input == 'paper':
            print("You Won!")
            user_wins += 1
        elif user_input == 'scissor':
            print("You Lost")
            comp_wins += 1

# Check for all possibilities when computer chose "Paper"
    if computer_picked == 'paper':
        if user_input == 'scissor':
            print("You Won!")
            user_wins += 1
        elif user_input == 'rock':
            print("You Lost")
            comp_wins += 1

# Check for all possibilities when computer chose "Scissor"
    if computer_picked == 'scissor':
        if user_input == 'rock':
            print("You Won!")
            user_wins += 1
        elif user_input == 'paper':
            print("You Lost")
            comp_wins += 1

print(f"\t\t\t\t You won {user_wins} times")
print(f"\t\t\t\t Computer won {comp_wins} times")
print(f"\t\t\t\t Tie: {draw}")
print("------Goodbye------")