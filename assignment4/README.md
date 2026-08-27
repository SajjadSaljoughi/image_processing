# Assignment 4

In this section, I created many projects on Basic Math Operations with OpenCV Library and Numpy Library

## Animal Face

- 🐒🐶🐺🦁🐯🦬🐮🐪 : Created Animal Face.
in input file , i put 12 face of animal .
You can change result by change this code (in Line 6):
```
animal = cv2.imread("input/animal{1-12}.jpg", cv2.IMREAD_UNCHANGED)
```
1 - 12 means : you can change it to any number from 1 to 12 . 
for example :
```
animal = cv2.imread("input/animal12.jpg", cv2.IMREAD_UNCHANGED)
```
## Background Estimation

- 🚗 : Remove the cars in film and result is empyt road without cars !

## Black Hole

- 🕳️ : in this section , First reduce the noise of any picture 
and then create a picture of Black Hole from 20 input image

## Face Morphing

- 👨🏻➡️🧔🏻 : Change the image to another image

## Find Secret Text

- 🤫 : Find Secret Image from 2 input image . Thats Funny!

## Sketch Image

- ✏️ : Created Sketch Image from an image , I Love it 😍

## Virtual Decoration

- 🏢 : Created Virtual Decoration 

## How to Install
Run Following Command : 
```
pip install -r requirement.txt
```
## How to Run
After Install , You can Run Following Command in Terminal to see the result :
```
python main.py
```
❗Important

you should be go to The Folder and Run that Command . Don't Forget it .

You Can Run This Command to Go the any Folder (Example : cd "AnimalFace"):
```
cd "folder-name"
```

In End , You Can Back to the Main Folder by Run this Command :
```
cd ..
```
## Result

### Animal Face
![Animal Face](AnimalFace/output/animal_face.jpg)

### Background Estimation
![Background Estimation](BackgroundEstimation/output/background.png)

### Black Hole
![Black Hole](BlackHole/output/result.jpg)

### Face Morphing
![Face Morphing](FaceMorphing/output/face_morphing.jpg)

### Find Secret Text
![Find Secret Text](FindSecretText/output/result.jpg)

### Sketch Image
![Sketch Image](SketchImage/output/result.jpg)

### Virtual Decoration
![Virtual Decoration](VirtualDecoration/output/result.jpg)