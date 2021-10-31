import cv2
import pytesseract

img = cv2.imread(r'../SampleImages/lorem.jpg', 0)

h, w = img.shape

ret, thresh1 = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
print(thresh1)
boxes = pytesseract.image_to_boxes(img) 
for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (255, 255, 255), 1)

cv2.imshow('img', img)
cv2.waitKey(0)
