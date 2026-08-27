import cv2
sticker_face = 0
face_detector = cv2.CascadeClassifier("haarcascade\\haarcascade_frontalface_default.xml")
eye_detector = cv2.CascadeClassifier("haarcascade\\haarcascade_eye_tree_eyeglasses.xml")
lip_detector = cv2.CascadeClassifier("haarcascade\\haarcascade_smile.xml")
while True:
    image = cv2.imread("input\\woman.jpg")
    height = image.shape[0]
    width = image.shape[1]
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 4)
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]
        if sticker_face == 0:
            ...
        if sticker_face == 1:
            sticker = cv2.imread("input\\emoji_clean.png")
            sticker = cv2.resize(sticker, (w, h))
            sticker_gray = cv2.cvtColor(sticker, cv2.COLOR_BGR2GRAY)
            _, mask = cv2.threshold(sticker_gray, 245, 255, cv2.THRESH_BINARY_INV)
            mask_inv = cv2.bitwise_not(mask)
            roi = image[y:y+h, x:x+w]
            bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
            fg = cv2.bitwise_and(sticker, sticker, mask=mask)
            final = cv2.add(bg, fg)
            image[y:y+h, x:x+w] = final
            cv2.imwrite("output\\emoji.jpg",image)
        elif sticker_face == 2:
            eyes = eye_detector.detectMultiScale(roi_gray)
            i = 1
            for (ex,ey,ew,eh) in eyes:
                if i == 1:
                    left_eye = cv2.imread("input\\tiger_eye_image_left.jpg")
                    left_eye = cv2.resize(left_eye, (ew, eh))
                    roi_color[ey:ey+eh,ex:ex+ew] = left_eye
                elif i == 2:
                    right_eye = cv2.imread("input\\tiger_eye_image_right.jpg")
                    right_eye = cv2.resize(right_eye, (ew, eh))
                    roi_color[ey:ey+eh,ex:ex+ew] = right_eye
                i += 1
            lips = lip_detector.detectMultiScale(roi_gray,1.2)
            for (lx,ly,lw,lh) in lips:
                lip = cv2.imread("input\\tiger_lip_image.jpg")
                lip = cv2.resize(lip, (lw,lh))
                roi_color[ly:ly+lh,lx:lx+lw] = lip
            cv2.imwrite("output\\tiger_woman.jpg",image)
        elif sticker_face == 3:
            small_face_image = cv2.resize(roi_color,(18,18))
            big_face_image = cv2.resize(small_face_image,(w,h),interpolation=cv2.INTER_NEAREST)
            image[y:y+h, x:x+w] = big_face_image
            cv2.imwrite("output\\chessboard_woman.jpg",image)
        elif sticker_face == 4:
            mirrored = cv2.flip(image, 1)
            image[:,width//2:width] = mirrored[:,width//2:width]
            cv2.imwrite("output\\mirrored_woman.jpg",image)
    cv2.imshow("result", image)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('1'):
        sticker_face = 1
    elif key == ord('2'):
        sticker_face = 2
    elif key == ord('3'):
        sticker_face = 3
    elif key == ord('4'):
        sticker_face = 4
    elif key == ord('0'):
        sticker_face = 0
