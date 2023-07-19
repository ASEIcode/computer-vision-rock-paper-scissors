import random as rd

def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return rd.choice(choices)
        
def get_user_choice():
    user_choice = input("\nPlease choose between Rock, Paper or Scissors: ")
    return user_choice

def play():
    computer_wins = 0
    user_wins = 0
    round_number = 1
    game_active = True
    while game_active:
        print(f"\n------------------------\nRound {round_number} >>> The Current Score is: You = {user_wins} CPU = {computer_wins} ")
        cpu_choice = get_computer_choice()
        user_choice = get_user_choice()

        winning_combos = {
            "Rock": "Scissors",
            "Paper": "Rock",
            "Scissors": "Paper"
        }

        if user_choice == cpu_choice:
            print(f"\nCPU plays {cpu_choice}. It's a tie!")
            round_number += 1
        elif winning_combos[user_choice] == cpu_choice:
            print(f"\nCPU plays {cpu_choice}. You won!")
            user_wins += 1
            round_number += 1
        else:
            print(f"\nCPU plays {cpu_choice}. You lost!")
            computer_wins += 1
            round_number += 1

        if user_wins == 3: 
            print(f"""\n
    Well done! You win!!!

    Final Score:

    User: {user_wins}

    CPU : {computer_wins}""")
            game_active = False

        elif computer_wins == 3:
            print(f"""\n
    Sorry...You lose!!!

    Final Score:

    User: {user_wins}

    CPU : {computer_wins}""")
            game_active = False
            
    play_again = input("\nWould you like to play again? Y or N: ")

    if play_again in ["\ny","Y","Yes", "yes"]:
        play()
    else:
        print("\nThankyou for you playing!")

play()
