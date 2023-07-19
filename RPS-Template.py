import cv2 #screencapture from webcam
from keras.models import load_model # machine learning model
import numpy as np
model = load_model('keras_model.h5')
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
    # Press q to close the window
    print(prediction) #outputs the prediction numbers into the console. Due to the while loop this will be a continuous streamed output of normalized np arrays
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
