import cv2

def histogram(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    result = []
    rows, cols = gray.shape
    for pixel in range(256):
        _sum = 0
        for row in range(rows):
            for col in range(cols):
                if gray[row][col] == pixel:
                    _sum += 1
        result.append(_sum)
    return result


