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

 ### **Milestone 3**

 - Created a new virtual environment in Conda and installed the dependencies: opencv-python, tensorflow, and ipykernel

- Ran the RPS-Template.py script to check that the model was working. I had to update the camera number in line 5 to work with my camera:

        cap = cv2.VideoCapture(0)
        CHANGED TO
        cap = cv2.VideoCapture(1)

A requirements.txt file was added listing the installed dependencies for this new environment. 

Committed and pushed this change to the Remote Repo.

### **Milestone 4**

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