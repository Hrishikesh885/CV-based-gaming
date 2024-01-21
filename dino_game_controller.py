import cv2
import mediapipe as mp
import pyautogui

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

cap = cv2.VideoCapture(0)

# Set the screen resolution for pyautogui
screen_width, screen_height = pyautogui.size()
pyautogui.FAILSAFE = False  # Disable the fail-safe to move the mouse to the corner

while True:
    success, frame = cap.read()
    if not success:
        break

    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MoveNet
    results = pose.process(rgb_frame)

    # Extract landmarks and check hand position for jumping or ducking
    if results.pose_landmarks:
        left_hand = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HAND]
        right_hand = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HAND]

        # Check the vertical position of the hands
        if left_hand.y < right_hand.y:
            # Jump
            pyautogui.press('space')
        else:
            # Duck
            pyautogui.press('down')

    cv2.imshow('Dino Game Controller', frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()
