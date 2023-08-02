# Computer Vision RPS
----------
### **Milestone 1**
----------
- Created the repository for the project and cloned it to myy local env. 
-------
### **Milestone 2**
-------

- Experimented with creating different Rock Paper Scissors image models using "teachablemachine". I found the best way to make it accurate was to train it on images which were side views of my hand in the poses against a blank wall background (white /cream).
 Introducing too many complex backgrounds into the training data made the resulting model quite skittish. However once I trained it on the plain background images, it was much more likely to correctly predict the correct hand gesture even when I was fully in the picture and with different things in the background to confuse it. Though it is still best with just a hand in frame on a plain background.
 - I have downloaded the the model now as keras_model.h5 and labels.txt. These files have been committed and pushed to the remote repo. 

-------
 ### **Milestone 3**
-------
 - Created a new virtual environment in Conda and installed the dependencies: opencv-python, tensorflow, and ipykernel

- Ran the RPS-Template.py script to check that the model was working. I had to update the camera number in line 5 to work with my camera:

        cap = cv2.VideoCapture(0)
        CHANGED TO
        cap = cv2.VideoCapture(1)

A requirements.txt file was added listing the installed dependencies for this new environment. 

Committed and pushed this change to the Remote Repo.

-----
### **Milestone 4**
------

manual_rps.py created

3 functions were then added to this file:


    def get_computer_choice():
        return rd.choice(CHOICES)

which uses the random module and returns a random value from this list:

    choices = ["Rock", "Paper", "Scissors"]

The second function gets input from the user (Rock, Paper or Scissors)

    def get_user_choice():
            user_choice = input("Please choose between Rock, Paper or Scissors: ")
            return user_choice

These are then called and assigned to the following variables to be used in the next function:

    cpu_choice = get_computer_choice()
    user_choice = get_user_choice()

The final of the 3 uses these variables to figure out who wins:

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

First the if statement checks if they cpu and user values are identical. If they are we Tie the game.

Secondly we check if the user has won. It does this using a dictionary of winning combos. The user_choice variable is used as a key to check whether the cpu_choice matches the value of the keyvalue pair. If it does then the user wins.

The else statement returns a loss if these first two connditions are not True. 

The above code was then abstracted into the play() function 

The play function runs the code in the above order and then calls the get_winner() function.

Finally we call the play() function so that when manual_rps.py runs the game starts.

    play()

All changes were then staged, committed and pushed.

-----
### **Milestone 5**
-----

- New Function: **Get prediction()**
        
        def get_prediction():
        
    In simple terms, this uses the webcam input and returns a prediction "Nothing", "Rock", "Paper" or "Scissors"

        countdown_timer(3)
    
    Creates a prompt for the user to press enter to start recording the frame. Counts down from the argument number provided (3) in this case. Please refer to doc string and comments for details

        cap = cv2.VideoCapture(1)

    Uses the *cv2* module to capture a Frame from the Webcam in slot 1. 
    
    *Please note:* In the RPS-Template.py file this was originally set to "0". When I did my test of the model using the template file we had to change this to port 1 to access my webcam which is my phone running through a virtual webcam client called Droidcam.

        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    
    An empty array is created ready for the normalized data from the frame to be stored in and used with our predictive model. (The data is created and assigned back to this later in the function)

    -------

    The below Code snippets are housed within a *"while True"* code block which holds and transforms a frame from the webcam and returns a prediction. The loop is needed to keep the webcam output continuously running.

        image_np = np.array(resized_frame)
    
    Transforms the frame into a numpy array and assigns it to "image_np" ready for further transformation.

        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 
    
    Normalizes the array. Converts the values to scientific notation numbers between -1 and 1. Normalised numbers are more mathematically friendly and are required for many machine learning libraries to function.

        data[0] = normalized_image
    
    As mentioned above, we assign this new array data back to the empty array we created 

        prediction = model.predict(data)
    
    Feeds the current array stored in *"data"* to our keras modal which outputs a prediction. We assign this prediction to the "*prediction*" variable.At this point this is an array of numbers which represent the probability of the image being *X* based on the index of the highest number in the array.

        0. Nothing
        1. Rock
        2. Paper
        3. Scissors

    Next we output the current frame to a display window:

        cv2.imshow('frame', frame)
    
    imshow() displays the specified frame in a window. The first argument *'frame'* names the window the second argument *frame* specifies the frame we want to display.

        final_prediction_index = np.argmax(prediction)

    Extracts the index of the highest number in th array. The key for this prediction is in the list above and also in the conditionals below:

        if final_prediction_index == 0:
            print("You chose Nothing")
            cap.release()
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

In each conditional statement we print the prediction to the terminal for the user and return the prediction for use in the game logic.

- **get_computer_choice()** function:

    Uses the random module to return a random value from the "choices" list below. This is used in the game as the computers guess each round

        choices = ["Rock", "Paper", "Scissors"]
    
    The following line gets a random item from the list and returns it:

        return rd.choice(choices)

- **get_user_choice()** function:

        def get_user_choice():
        user_choice = get_prediction()
        return user_choice

    Calls the get_prediction() function and stores it in the user_choice variable which is returned as *"user_choice"* to be used in the game.

- **play()** function:

    This function contains all of the logic to run the game, calls all of the functions we created earlier and runs then in a loop of rounds.

        computer_wins = 0 
        user_wins = 0 
        round_number = 1
    
    The above is used to keep track of CPU / User wins and the round number. They are kept outside of the main game loop for this reason.

        game_active = True

    This is used to control the state of the game and break the loop when certain conditions are met. (3 wins by either the CPU or user)

        while game_active:
    
    This will keep the game code looping through rounds until the overall win or loss condition of 3 wins is met.

        print(f"\n------------------------\nRound {round_number} >>> The Current Score is: You = {user_wins} CPU = {computer_wins} ")
    
    This block informs the user of the Score and Round number when each round starts.

        cpu_choice = get_computer_choice()
        user_choice = get_user_choice()

    Fetches and stores Rock, Paper, Scissors or Nothing from the random generator and webcam prediction model and stores them as user_choice and cpu_choice for the duration of this round.


        winning_combos = {
            "Rock": "Scissors",
            "Paper": "Rock",
            "Scissors": "Paper"
        }

    This is a dictionary of winning combinations for the user. The users prediction (*user_choice*) is fed in as a key and if the value of the pair returned matches the *cpu_choice* then the user wins the round. See the conditionals below:

        if user_choice == cpu_choice: 
            print(f"\nCPU plays {cpu_choice}. It's a tie!")
            round_number += 1 

    First we check for a draw, by seeing if cpu_choice and user_choice match.

        elif winning_combos[user_choice] == cpu_choice: 
            print(f"\nCPU plays {cpu_choice}. You won!")
            user_wins += 1 
            round_number += 1

    Next we feed *user_choice* into the dictionary as a key. The value returned is checked against the *cpu_choice*. If it matches, the user wins.

            user_wins += 1 
            round_number += 1
    This increases the round number and user wins by 1.

        else: 
            print(f"\nCPU plays {cpu_choice}. You lost!")
            computer_wins += 1 
            round_number += 1
    
    Finally if its not a win or a draw it must be a loss. So the *else* statement deals with this and adds to the *computer_wins* and *round_number*.

        if user_wins == 3:

            print(f"""\n
        Well done! You win!!!

        Final Score:

        User: {user_wins}

        CPU : {computer_wins}""")

            game_active = False 

    Next we check for 3 wins from the user. If this is True we print the message and break the loop  by setting *game_active* to *False*

        elif computer_wins == 3:
    
            print(f"""\n
        Sorry...You lose!!!

        Final Score:

        User: {user_wins}

        CPU : {computer_wins}""")

            game_active = False
    
    Or if the computer has 3 wins the same happen but with a loss messaage.

    When the loop breaks we give the user the option to continue playing. If they input one of the options on the list then the *play()* function is called and the game starts again.

        else:
        print("\nThankyou for you playing!")
        cv2.destroyAllWindows() 

    If the user enters anything other than the items on the list, then the game ends and the window is closed.

- **play()**

    The last line starts the game and runs all of the above code.
        
        play()

-----------------------------------------
### **Improvements Change Log:**

#### 02/08/2023

- Added extra elif statement to handle the error that would be displayed if user_choice returned as "Nothing"

        elif user_choice == "Nothing": # prevents an error in case of "Nothing" being returned
                print("Sorry I didnt understand your choice. Please try again...")

- Moved the whole game and all of its functions into the Rps_game Class. Added self and tweaked any mismatched logic to fit the class.

- Added winning_score to the instance initialasion to allow the user to choose the winning condition. (3 points, 5 points etc) when creating a game instance.

        class Rps_game:
        """When initialising the class. Enter a number to choose how many wins will be the winnign condition for either the CPU or the user
        All the logic for the game and methods needed are contained below and each one is explained with its own docstring and in line comments"""

        def __init__(self, winning_score) -> None:
            self.winning_score = winning_score # how many points does the user or CPU need to win the game?

### **Known issues and improvements to be made:**

Note: The below bugs are likely just down to problems with my personal hardware

1. Get the webcam window working (it currently just hangs not responding on my system though it does take input and make a prediction). I think this may be an issue with my particular hardware and software setup for my webcam.

2. At the moment the model is somehow biased towards paper and responds slowly when you change your hand gesture. (It may take up to 2 more rounds for it to regognise the changing hand gesture and it always guesses paper the first time.) I need to find out why this happens and fix it. I suspect it is the same bug which is stopping my webcam window from showing the frame 

3. Once the above is fixed, have the webcam output window overlay the terminal output, countdown etc so the game can all be played in the webcam window.


        




    




     
    