import random as rd


def play():
    choices = ["Rock", "Paper", "Scissors"]

    def get_computer_choice():
        return rd.choice(choices)
        

    def get_user_choice():
        user_choice = input("Please choose between Rock, Paper or Scissors: ")
        return user_choice

    cpu_choice = get_computer_choice()
    user_choice = get_user_choice()

    def get_winner():

        winning_combos = {
            "Rock": "Scissors",
            "Paper": "Rock",
            "Scissors": "Paper"
        }

        if user_choice == cpu_choice:
            print(f"CPU plays {cpu_choice}. It's a tie!")
        elif winning_combos[user_choice] == cpu_choice:
            print(f"CPU plays {cpu_choice}. You won!")
        else:
            print(f"CPU plays {cpu_choice}. You lost!")
        

    get_winner()


play()
    
    
    