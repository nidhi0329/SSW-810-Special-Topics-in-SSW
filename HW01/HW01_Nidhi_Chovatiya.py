""" Nidhi Chovatiya
    CWID: 10457344
    HW01 - Implement an interactive rock, paper, scissors game between human and computer
"""
from random import choice

def get_human_move() -> str:
    """ Ask the user for R, P, S, or Q.  
        Loop until given a valid input 
    """
    while True:
        user_input: str = input("Please choose 'R', 'P', 'S' or 'Q' to quit: ")

        if user_input.lower() == "r":
            return "rock"
        elif user_input.lower() == "p":
            return "paper"
        elif user_input.lower() == "s":
            return "scissors"
        elif user_input.lower() == "q": 
            return "quit"
        else:
            print("Error! Please enter a valid input.") 

def get_computer_move() -> str:
    """ return the computer's random choice using random.choice """
    move: str = choice(['rock', 'paper', 'scissors'])
    return move

def play_game() -> bool:
    human: str = get_human_move()
    if human == 'quit':  # human wants to quit
        return False

    computer: str = get_computer_move()

# compare the input of human and computer to decide the output
    print(f"Your coice: {human}")
    print(f"Computer choice: {computer}")
    #Condition for the output is Tie
    if human == computer: 
        print(f"Result is: Both chose the same option. So, it's a Tie!")

    #Condition for the human is lost and computer is win
    elif human == "rock" and computer == "paper":
        print(f"Result is: {computer} beats {human} - I win!")
    elif human == "paper" and computer == "scissors":
        print(f"Result is: {computer} beats {human} - I win!")
    elif human == "scissors" and computer == "rock":
        print(f"Result is: {computer} beats {human} - I win!")
        

    #Condition for the human is win and computer is lost
    elif human == "rock" and computer == "scissors":
        print(f"Result is: {human} beats {computer} - You win!")
    elif human == "scissors" and computer == "paper":
        print(f"Result is: {human} beats {computer} - You win!")
    elif human == "paper" and computer == "rock":
        print(f"Result is: {human} beats {computer} - You win!")

    # play again
    return True  

def main() -> None:
    """ Play multiple games until the human asks to stop """
    again: bool = True
    while again:
        again = play_game()

    print("Thanks for playing!")

if __name__ == "__main__":
    main()