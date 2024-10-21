import cv2 #mporting opencv Library this i to open camera and take the video
import numpy as np # to convert image to array and expand dimensions
from tensorflow.keras.models import load_model # to Load the saved model
from tensorflow.keras.preprocessing import image # to preproccess the image
model = load_model("dataset.h5") # we are loading the saved moodek
video = cv2.VideoCapture(0) # two parameters 1, bool 0 or 1, frame
index = ["A","B","C","D","E","F","G","H","I"]
index=['A','B','C','D','E','F','G','H','I']
#from playsound import playsound
while(1):
    success,frame = video.read()
    cv2.imwrite("image.jpg",frame)
    img = image.load_img("image.jpg",target_size = (64,64))
    x = image.img_to_array(img)
    x = np.expand_dims (x,axis = 0)
    pred = np.argmax(model.predict(x),axis=1)
    p = index [pred[0]]
    print("predicted letter is: "+ str(p))
    #playSound("letter"+str(str(index [p])+"is detected"))
    cv2.putText (frame, "predicted letter is "+str(p), (100, 100), cv2. FONT_HERSHEY_SIMPLEX, 1,(0,0,0), 4)
    cv2.imshow("showcasewindow", frame)
    
    if cv2.waitkey(1) & 0xFF == ord('a'):
        break
video.release()
cv2.destroyAllwindows()
