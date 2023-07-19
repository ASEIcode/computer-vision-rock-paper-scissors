import time
import cv2 #screencapture from webcam
from keras.models import load_model # machine learning model
import numpy as np
import random as rd

model = load_model('keras_model.h5')

def countdown_timer(seconds):
    print("Get ready! Show the camera Rock, Paper or Scissors and press enter when ready. For best results, hold your hand still during the countdown...")
    start_time = time.time()
    end_time = start_time + seconds
    countdown = seconds

    while time.time() < end_time:
        print(countdown)
        countdown -= 1      
        
        # Adjust the interval based on your requirements
        current_time = time.time()
        while current_time + 1 > time.time():
            pass

def get_prediction():
    """Returns the output of the Rock Paper Scissors Keras Model"""
     
    countdown_timer(3)
    cap = cv2.VideoCapture(1)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)  

    while True:
        ret, frame = cap.read() # ret = Boolean whether the frame was successfully read / frame = stores the frame
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image (convert the values to scientific notation numbers between -1 and 1)
        data[0] = normalized_image # modifies the np array "data" in place with the new normalized numbers
        prediction = model.predict(data) # stores the prediction based on the normalize numbers in "data"
        cv2.imshow('frame', frame) # imshow() displays the specified frame in a window. The first argument names the window the second specifies the frame
        final_prediction_index = np.argmax(prediction)
        
        if final_prediction_index == 0:
            print("You chose Nothing")
            return "Nothing"
        elif final_prediction_index == 1:
            print("You chose Rock")
            return "Rock"
        elif final_prediction_index == 2:
            print("You chose Paper")
            return "Paper"
        elif final_prediction_index == 3:
            print("You chose Scissors")
            return "Scissors"     


def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return rd.choice(choices)
        
def get_user_choice():
    user_choice = get_prediction()
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

    if play_again in ["y","Y","Yes", "yes"]:
        play()
    else:
        print("\nThankyou for you playing!")

play()
