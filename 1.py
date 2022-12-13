#I'm unable to think in 0,1 matrix form 
# so i solved using opencv. 

import cv2
img = cv2.imread("iiit-test-image1.png", cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(
    img_gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imwrite("thresh.png", thresh)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
all_contours_drawn = cv2.drawContours(
    img.copy(), contours, -1, (0, 255, 0), 2)  # draw all contours
cv2.imwrite("all_contours.png", all_contours_drawn)

box_center_x = []
box_center_y = []
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    box_center_x.append(x+w/2)
    box_center_y.append(y+h/2)
print("x-coordinate of boxes: {}".format(box_center_x))
print("y-coordinate of boxes: {}".format(box_center_y))
all_box_centers_drawn = img.copy()
for i in range(len(box_center_x)):
    cv2.circle(
        all_box_centers_drawn,
        (int(box_center_x[i]), int(box_center_y[i])),2, (0 , 0, 255), 2)
cv2.imwrite("box-centers.png", all_box_centers_drawn)
