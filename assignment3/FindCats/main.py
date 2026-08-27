import cv2
image = cv2.imread("input\\cat.jpg")
grayscale_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
models = [
    "haarcascade\\haarcascade_frontalcatface.xml",
    "haarcascade\\haarcascade_frontalcatface_extended.xml"
]
detections = []
for m in models:
    det = cv2.CascadeClassifier(m)
    cats = det.detectMultiScale(grayscale_image, 1.05, 3)
    detections.extend(cats)
final = []
for (x,y,w,h) in detections:
    if not any(abs(x-X)<20 and abs(y-Y)<20 for (X,Y,W,H) in final):
        final.append((x,y,w,h))
for (x,y,w,h) in final:
    cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 2)
    cv2.putText(image,f"Count of Cats = {len(final)}",(0,25),
                cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
cv2.imshow("",image)
cv2.imwrite("output\\cat2.jpg",image)
cv2.waitKey()