#pip install opencv-python
#pip install pytesseract
#pip install numpy
#pip install pyscreenshot
########################################################################################################################################

#setup part 

#gender of teacher you are attending class of
f= input("gender of teacher: ")#reply with Male/Female

#adding a delay so that you can switch windows 
import time 
time.sleep(5)

#adding a text file
# A text file is created and flushed
file = open("/Users/eemanmajumder/code_shit/abstract/Student /text/recognized.txt", "w+")
file.write("")
file.close()




#########################################################################################################################################

#screenshot part

#Getting the text image part 
import pyscreenshot as ImageGrab
import numpy as np
bbox=(429,857,1073,899)#(left_x, top_y, right_x, bottom_y)
screenshot = ImageGrab.grab(bbox=bbox, backend='mac_quartz')
screenshot.save('/Users/eemanmajumder/code_shit/abstract/Student /img/sample.png')


#########################################################################################################################################


#OCR Part

# Import required packages
import cv2
import pytesseract

# Mention the installed location of Tesseract-OCR in your system
pytesseract.pytesseract.tesseract_cmd = (r'/opt/homebrew/Cellar/tesseract/5.1.0/bin/tesseract')

# Read image from which text needs to be extracted
img = cv2.imread("/Users/eemanmajumder/code_shit/abstract/Student /img/sample.png")

# Preprocessing the image starts

#negative of image 
img_not = cv2.bitwise_not(img)
cv2.imwrite("/Users/eemanmajumder/code_shit/abstract/Student /img/img_not.png", img_not)
# Convert the image to gray scale
gray = cv2.cvtColor(img_not, cv2.COLOR_BGR2GRAY)
# Performing OTSU threshold
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

# Specify structure shape and kernel size.
# Kernel size increases or decreases the area
# of the rectangle to be detected.
# A smaller value like (10, 10) will detect
# each word instead of a sentence.
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

# Applying dilation on the threshold image
dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)

# Finding contours
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
												cv2.CHAIN_APPROX_NONE)

# Creating a copy of image
im2 = img.copy()



# Looping through the identified contours
# Then rectangular part is cropped and passed on
# to pytesseract for extracting text from it
# Extracted text is then written into the text file
for cnt in contours:
  x, y, w, h = cv2.boundingRect(cnt)
	# Drawing a rectangle on copied image
  rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
	
	# Cropping the text block for giving input to OCR
  cropped = im2[y:y + h, x:x + w]
    
# Open the file in append mode
file = open("/Users/eemanmajumder/code_shit/abstract/Student /text/recognized.txt", "a")
cv2.imwrite("/Users/eemanmajumder/code_shit/abstract/Student /img/cropped.png", im2)
# Apply OCR on the cropped image
text = pytesseract.image_to_string(img_not, lang='eng')
l=[]
l.append(text)
time.sleep(0.6)

# Appending the text into file
file.write(text)
file.write("\n")

# Close the file
file.close


########################################################################################################################################
 #list work 
def convert(lst):
    return (lst[0].split())
     

file = open("/Users/eemanmajumder/code_shit/abstract/Student /text/recognized.txt", "r")
j=file.read()
k=[]
k.append(j)
l=convert(k)
print(l)

###########################################################################################################################################
#mute/unmute part
# pip3 install mouse
from Quartz.CoreGraphics import CGEventCreateMouseEvent
from Quartz.CoreGraphics import CGEventPost
from Quartz.CoreGraphics import kCGEventMouseMoved
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseUp
from Quartz.CoreGraphics import kCGMouseButtonLeft
from Quartz.CoreGraphics import kCGHIDEventTap

def mouseEvent(type, posx, posy):
        theEvent = CGEventCreateMouseEvent(
                    None, 
                    type, 
                    (posx,posy), 
                    kCGMouseButtonLeft)
        CGEventPost(kCGHIDEventTap, theEvent)

def mousemove(posx,posy):
        mouseEvent(kCGEventMouseMoved, posx,posy);

def mouseclick(posx,posy):
        # uncomment this line if you want to force the mouse 
        # to MOVE to the click location first (I found it was not necessary).
        #mouseEvent(kCGEventMouseMoved, posx,posy);
        mouseEvent(kCGEventLeftMouseDown, posx,posy);
        mouseEvent(kCGEventLeftMouseUp, posx,posy);
###########################################################################################################################################

#sound management part 

#yes sir / yes mam sounds 
import playsound

#funtions 


from playsound import playsound
  
def playyessir():
  # for playing note.wav file
  playsound('/path/yes_sir.wav')
  print('playing sound Yes Sir')

def playyesmam():
  # for playing note.wav file
  playsound('/path/yes_mam.wav')
  print('playing sound Yes mam')


for i in l:
    while True:
      if i == 'eeman':
        if f=='Male':
          playyessir()
        else: 
          playyesmam()
    
      elif i == 'eman':
        if f=='Male':
          playyessir()
        else: 
          playyesmam()
    
      elif i == 'iman':
        if f=='Male':
          playyessir()
        else: 
          playyesmam()
      elif i == 'iman.':
        if f=='Male':
          playyessir()
        else: 
          playyesmam()
      elif i == 'Iman.':
        if f=='Male':
          playyessir()
        else: 
          playyesmam()
      else:
        break


#https://drive.google.com/file/d/1WQPOhnAXWQeW8QSvv31QzjZq2Ga-pD3Z/view?usp=sharing


