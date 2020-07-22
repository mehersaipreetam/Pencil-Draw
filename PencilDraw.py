import cv2

path = input('Enter the path\n')
name_image = input('Enter image name\n')

img = cv2.imread(path + '/' + name_image)
cv2.imshow('Image',img)
cv2.waitKey()

# GRAY

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Image',gray_img)
cv2.waitKey()

# INVERT

inv_img = 255 - gray_img
cv2.imshow('Inverted img', inv_img)
cv2.waitKey()
cv2.destroyAllWindows()

## BLUR

gray_img_blur = cv2.GaussianBlur(inv_img, (21, 21), 0)
cv2.imshow('Blur',gray_img_blur)
cv2.waitKey()

# BLEND

output = cv2.divide(gray_img, 255 - gray_img_blur, scale=220)
cv2.imshow('Output',output)
cv2.waitKey()
cv2.destroyAllWindows()

name_saved = input('Enter file name to be saved\n')
cv2.imwrite(path + '/' + name_saved,output)
