import random

def user():
    print("Welcome to Stone,paper,Scissors Game!")
    while True:
        userchoice=input("Enter your choice(stone,paper,scissors):").lower().strip()
        if userchoice in ['stone','paper','scissors']:
            print("you chose:",userchoice)
            return userchoice
        else:
            print("invalid choice,enter your choice from (stone,paper,scissors)")
             
def computer():
    a=['stone','paper','scissors']
    computerchoice=random.choice(a)
    print("computer chose:",computerchoice)
    return computerchoice
def winner(userChoice,computerChoice):
     if userChoice==computerChoice:
          return "It is a Tie"
         
     elif(userChoice=='stone' and computerChoice=='scissors')or(userChoice=='scissors' and computerChoice=="paper")or(userChoice=='paper' and computerChoice=='stone'):
          return "Hurray...You Win!!!" 
     else:
          return "Computer Wins!!!"


def stonepaperscissors():
        userChoice = user()
        computerChoice=computer()
        print(winner(userChoice,computerChoice))
        playagain=input("Do you want to play again:(yes,no):").lower().strip()
        if playagain !=("yes" or "y"):
            print("Thanks for playing this game..")
        else:
             stonepaperscissors()
              

stonepaperscissors()






