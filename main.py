from cvzone.PoseModule import PoseDetector
import cv2
import socket

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
#success, img = cap.read()
#h, w, _ = img.shape
detector = PoseDetector()
posList = []
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddressPort = ("127.0.0.1", 5052)

while True:
    # Get image frame
    success, img = cap.read()
    # Find the hand and its landmarks
    img = detector.findPose(img)  # with draw
    # hands = detector.findHands(img, draw=False)  # without draw
    lmList, bboxInfo = detector.findPosition(img)

    if bboxInfo:
       if lmList and len(lmList) > 2:  # Check if lmList is not empty and has at least 3 elements
            lmString = ''
            for lm in lmList:
                if len(lm) > 2:  # Check if lm has at least 3 elements
                    lmString += f'{lm[1]},{img.shape[0] - lm[2]},{lm[0]},'
            posList.append(lmString)

            sock.sendto(str.encode(str(posList)), serverAddressPort)

    # Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)
