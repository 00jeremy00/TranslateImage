import pytesseract
import cv2

img = cv2.imread(r'../SampleImages/lorem.jpg', 1)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('My Pic', gray_img)

cv2.waitKey(0)

h, w, c = img.shape

print(h, w, c);


cv2.destroyAllWindows()

threshold_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(img)


f = open("textFile.txt", "w")
f.write(text)
f.close()
