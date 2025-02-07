import cv2 
import mediapipe as mp
import pyautogui
import numpy as np

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()
pyautogui.FAILSAFE = False

smoothing_window = 5
head_positions = []

LEFT_THRESHOLD = 0.45
RIGHT_THRESHOLD = 0.55

def draw_head_landmarks(frame, landmarks, frame_w, frame_h):
    connections = [
    ]
    
    for connection in connections:
        start_point = landmarks[connection[0]]
        end_point = landmarks[connection[1]]
        
        start_x = int(start_point.x * frame_w)
        start_y = int(start_point.y * frame_h)
        end_x = int(end_point.x * frame_w)
        end_y = int(end_point.y * frame_h)
        
        cv2.line(frame, (start_x, start_y), (end_x, end_y), (0, 255, 0), 2)

def draw_movement_zones(frame):
    h, w, _ = frame.shape
    cv2.line(frame, (int(w * LEFT_THRESHOLD), 0), (int(w * LEFT_THRESHOLD), h), (255, 0, 0), 2)
    cv2.line(frame, (int(w * RIGHT_THRESHOLD), 0), (int(w * RIGHT_THRESHOLD), h), (255, 0, 0), 2)
    
    cv2.putText(frame, "", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.putText(frame, "", (int(w * 0.45), 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, "", (int(w * 0.75), 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmarks_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape

    if landmarks_points:
        landmarks = landmarks_points[0].landmark
        nose_tip = landmarks[4]
        head_x = nose_tip.x

        head_positions.append(head_x)
        if len(head_positions) > smoothing_window:
            head_positions.pop(0)

        smoothed_x = np.mean(head_positions)

        draw_head_landmarks(frame, landmarks, frame_w, frame_h)
        
        draw_movement_zones(frame)
        
        # Scrolling logic with smoothed position
        if smoothed_x < LEFT_THRESHOLD:
            scroll_amount = int(-50 * (1 - smoothed_x/LEFT_THRESHOLD))  # Proportional scrolling
            pyautogui.scroll(scroll_amount)
        elif smoothed_x > RIGHT_THRESHOLD:
            scroll_amount = int(50 * (smoothed_x-RIGHT_THRESHOLD)/(1-RIGHT_THRESHOLD)) 
            pyautogui.scroll(-scroll_amount)
            
        # Visual feedback for current head position
        x = int(nose_tip.x * frame_w)
        y = int(nose_tip.y * frame_h)
        cv2.circle(frame, (x, y), 1, (0, 255, 255), -1)

    cv2.imshow('hyloo', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()