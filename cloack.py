import cv2
import numpy as np
import time

# Reading the video capture
capture_video = cv2.VideoCapture("video.mp4")

# Give the camera some time to warm up
time.sleep(1)
count = 0
background = 0

# Capturing the background
for i in range(60):
    return_val, background = capture_video.read()
    if return_val == False:
        continue

background = np.flip(background, axis=1)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_video = cv2.VideoWriter('output_video.mp4', fourcc, 30.0, (int(capture_video.get(3)), int(capture_video.get(4))))

# Reading from the video
while (capture_video.isOpened()):
    return_val, img = capture_video.read()
    if not return_val:
        break
    count += 1
    img = np.flip(img, axis=1)
    
    # Convert the image from BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Generating mask to detect red color
    lower_red = np.array([100, 40, 40])
    upper_red = np.array([100, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    lower_red = np.array([155, 40, 40])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    mask1 = mask1 + mask2

    # Refining the mask corresponding to the detected red color
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
    mask1 = cv2.dilate(mask1, np.ones((3, 3), np.uint8), iterations=1)
    mask2 = cv2.bitwise_not(mask1)

    # Generating the final output
    res1 = cv2.bitwise_and(background, background, mask=mask1)
    res2 = cv2.bitwise_and(img, img, mask=mask2)
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

    output_video.write(final_output)
    cv2.imshow("INVISIBLE MAN", final_output)
    
    # Press 'Esc' to exit
    k = cv2.waitKey(10)
    if k == 27:
        break

# Release capture and close windows
capture_video.release()
output_video.release()
cv2.destroyAllWindows()
