import cv2
import mediapipe as mp
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
from threading import Thread

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

camera = cv2.VideoCapture(0)

class VideoHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == '/video_feed':
            self.send_response(200)
            self.send_header('Content-type', 'multipart/x-mixed-replace; boundary=frame')
            self.end_headers()
            self.generate_frames()

    def generate_frames(self):
        while True:
            success, frame = camera.read()
            if not success:
                break

            # Convert the frame to RGB
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Process the frame with MoveNet
            results = pose.process(rgb_frame)

            # Extract landmarks and draw markings
            if results.pose_landmarks:
                for landmark in results.pose_landmarks.landmark:
                    height, width, _ = frame.shape
                    cx, cy = int(landmark.x * width), int(landmark.y * height)
                    cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)

            # Convert the frame back to BGR
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            # Encode the frame as JPEG
            _, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()

            self.wfile.write(b'--frame\r\n')
            self.wfile.write(b'Content-Type: image/jpeg\r\n\r\n')
            self.wfile.write(frame_bytes + b'\r\n')

if __name__ == '__main__':
    server = TCPServer(('0.0.0.0', 8000), VideoHandler)

    def run_server():
        server.serve_forever()

    server_thread = Thread(target=run_server)
    server_thread.start()
