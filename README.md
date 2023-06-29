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
