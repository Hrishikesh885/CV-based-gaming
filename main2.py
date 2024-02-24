# import tensorflow as tf
# import tensorflow_hub as hub

# model_name = "movenet_lightning"  # Choose the desired variant
# if "tflite" in model_name:
#     if "movenet_lightning_f16" in model_name:
#         !wget -q -O model.tflite [^1^][14]
#         input_size = 192
#     elif "movenet_thunder_f16" in model_name:
#         !wget -q -O model.tflite [^2^][15]
#         input_size = 256
#     elif "movenet_lightning_int8" in model_name:
#         !wget -q -O model.tflite [^3^][16]
#         input_size = 192
# else:
#     module = hub.load(f"https://tfhub.dev/google/movenet/singlepose/{model_name}/4")
#     input_size = 192  # Adjust based on the chosen model
# import cv2

# cap = cv2.VideoCapture(0)  # 0 for default camera (change if needed)

# while True:
#     ret, frame = cap.read()  # Read a frame from the camera
#     if not ret:
#         break  # Break the loop if no frame is captured

#     # Process the frame (e.g., resize, convert to RGB, etc.)
#     # Run inference using MoveNet on the processed frame

#     cv2.imshow("MoveNet Pose Estimation", frame)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break  # Press 'q' to exit the loop

# cap.release()
# cv2.destroyAllWindows()
