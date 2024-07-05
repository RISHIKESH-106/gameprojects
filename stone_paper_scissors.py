import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (stone/paper/scissors): ").lower().strip()
        if user_choice in ['stone', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice! Please enter 'stone', 'paper', or 'scissors'.")

def get_computer_choice():
    choices = ['stone', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'stone' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'stone') or (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def stone_paper_scissors():
    print("Welcome to the Stone, Paper, Scissors game!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print(determine_winner(user_choice, computer_choice))
        
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    stone_paper_scissors()


