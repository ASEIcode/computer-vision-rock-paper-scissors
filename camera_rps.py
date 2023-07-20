import time
import cv2 #screencapture from webcam
from keras.models import load_model # machine learning model
import numpy as np
import random as rd

model = load_model('keras_model.h5') # loads the keras model outside of the loop so that it can continuously run without restarting each round.

def countdown_timer(seconds):
    """Provides functionality to add a countdown to another function. In this case it is used to alllow the user a pause
    to prepare and chooose a new hand gesture for the next round. Prompts user to press Enter to continue and counts down from
    the number passed as an argument to the seconds parameter e.g. countdown_timer(10) would give a 10 second countdown"""

    input("\nGet ready! Show the camera Rock, Paper or Scissors and press enter when ready. For best results, hold your hand still during the countdown...")
    start_time = time.time() #stores a time to measure intervals from
    end_time = start_time + seconds # stores a second time using seconds to set an interval
    countdown = seconds # assigns seconds to countdown so it can be used below as a counter without effecting the above code

    while time.time() < end_time:
        print(countdown)
        countdown -= 1 # prints the current coundown number which starts from "seconds" and decreases with each cycle of the below nested loop        
        
        current_time = time.time()
        while current_time + 1 > time.time():
            pass # for each second that passes this loop is broken and allow the code above to run again

def get_prediction():
    """Takes the input from the Webcam via a series of screencaps, resizes it, 
    transforms it into a numpy array, normalizes it and runs this normalised array through 
    the keras machine learning model. The highest number in the array corresponds to the highest
    probability prediction with the index positions refering to: 0 = nothing, 1 = Rock, 2 = Paper, 3 = Scissors.
    We assign this highest value index to final_prediction and then use conditional statements to return
    Rock, Paper, Scissors or Nothing. See comments below for a break down of each line"""
     
    countdown_timer(3) # calls the countdown function: The user is prompted to press enter and then a 3 second countdown is given for each round
    cap = cv2.VideoCapture(1) # Captures a Frame from the Webcam in slot 1 (0 would not work on my system)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)  # normalized image array is assigned to this in the while loop below

    while True:
        ret, frame = cap.read() # cap.read() returns two things: "ret" = Boolean whether the frame was successfully read / "frame" = stores the frame
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA) # resize the frame to match the empty "data" array above
        image_np = np.array(resized_frame) #transforms the frame into a numpy array and assigns it to "image_np"
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalizes the array (convert the values to scientific notation numbers between -1 and 1)
        data[0] = normalized_image # assigns this to the empty array "data" outside of the while loop
        prediction = model.predict(data) # stores the prediction based on the normalized numbers stored in "data"
        cv2.imshow('frame', frame) # imshow() displays the specified frame in a window. The first argument names the window the second specifies the frame
        final_prediction_index = np.argmax(prediction) # extracts the index of the highest number in th array. The key for this prediction is in the conditionals below
        
        if final_prediction_index == 0:
            print("You chose Nothing") # prints the prediction to the terminal
            cap.release() # releases the current cap before we return a value
            return "Nothing"
        elif final_prediction_index == 1:
            print("You chose Rock")
            cap.release()
            return "Rock"
        elif final_prediction_index == 2:
            print("You chose Paper")
            cap.release()
            return "Paper"
        elif final_prediction_index == 3:
            print("You chose Scissors")
            cap.release()
            return "Scissors" 

         
  


def get_computer_choice():
    """Uses the random module to return a random value from the "choices" list below.
    This is used in the game as the computers guess each round"""

    choices = ["Rock", "Paper", "Scissors"]
    return rd.choice(choices)
        
def get_user_choice():
    """Calls the get_prediction() function and stores it in the user_choice variable which is returned to be used in the game"""
    user_choice = get_prediction()
    return user_choice

def play():
    """Contains all of the logic to run the game using the earlier created functions"""
    computer_wins = 0 #  stores cpu wins each round
    user_wins = 0 # stores user wins each round
    round_number = 1 # keeps track of the round number each loop
    game_active = True # perpetuates the loop until 3 wins by either CPU or User are reached
    while game_active:
        # Displays score and round number each loop
        print(f"\n------------------------\nRound {round_number} >>> The Current Score is: You = {user_wins} CPU = {computer_wins} ")
        cpu_choice = get_computer_choice()
        user_choice = get_user_choice()

        # Dictionary storing winning combo
        winning_combos = {
            "Rock": "Scissors",
            "Paper": "Rock",
            "Scissors": "Paper"
        }

        if user_choice == cpu_choice: # 1st we check to see if the user and cpu match (tie)
            print(f"\nCPU plays {cpu_choice}. It's a tie!")
            round_number += 1 # round number increased for next loop
        elif winning_combos[user_choice] == cpu_choice: # user_choice fed to dictionary as a key. If the CPU choice matches the value returned, the user wins
            print(f"\nCPU plays {cpu_choice}. You won!")
            user_wins += 1 # increase user wins by 1
            round_number += 1
        else: # if its not a tie and the user doesnt win. Then it must be a loss.
            print(f"\nCPU plays {cpu_choice}. You lost!")
            computer_wins += 1 # increase cpu wins by 1
            round_number += 1

        if user_wins == 3:  # check for 3 user wins. Print congratulatory message if true
            print(f"""\n
    Well done! You win!!!

    Final Score:

    User: {user_wins}

    CPU : {computer_wins}""")
            game_active = False # break the loop and end the game

        elif computer_wins == 3: # check for 3 cpu wins and print message if true
            print(f"""\n
    Sorry...You lose!!!

    Final Score:

    User: {user_wins}

    CPU : {computer_wins}""")
            game_active = False # break the loop and end the game
            
    play_again = input("\nWould you like to play again? Y or N: ") # Give the user an option to continue playing or exit

    if play_again in ["y","Y","Yes", "yes"]: # calls the play function again 
        play()
    else:
        print("\nThankyou for you playing!") # closes the game and destroys the webcam display window
        cv2.destroyAllWindows() 

play()
