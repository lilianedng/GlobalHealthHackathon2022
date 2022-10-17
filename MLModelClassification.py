import mediapipe as mp
import cv2
import numpy as np
from gtts import gTTS
import os

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
cap = cv2.VideoCapture(0)
flag_thankyou = "Not Detected"
flag_love = "Not Detected"
language = 'en'
counter = 0

thankyou_text = "Thank You!"
thankyou_object = gTTS(text=thankyou_text, lang=language, slow=True)
thankyou_object.save("thankyou.mp3")

love_text = "Love!"
love_object = gTTS(text=love_text, lang=language, slow=True)
love_object.save("love.mp3")

def calculate_angle(a,b,c):

    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)

    if angle >180.0:

        angle = 360-angle

    return angle

with mp_pose.Pose(min_detection_confidence=0.7, min_tracking_confidence=0.7) as pose:

    while cap.isOpened():
        ret, frame = cap.read()
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = pose.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        try:

            landmarks = results.pose_landmarks.landmark
            shoulder_right = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            elbow_right = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            wrist_right = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
            angle_right = calculate_angle(shoulder_right, elbow_right, wrist_right)
            shoulder_left = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            elbow_left = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            wrist_left = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
            angle_left = calculate_angle(shoulder_left, elbow_left, wrist_left)
            #cv2.putText(image, str(angle_right), tuple(np.multiply(elbow_right, [640, 480]).astype(int)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
            #cv2.putText(image, str(angle_left), tuple(np.multiply(elbow_left, [640, 480]).astype(int)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

            if (angle_right < 30):

                flag_love = "Not Detected"
                flag_thankyou = "Detected"

            if (angle_right > 30 and angle_right < 165) and (flag_thankyou == "Detected") and (flag_love == "Not Detected"):

                flag_love = "Not Detected"
                flag_thankyou = "Detected"
                cv2.putText(image, 'THANK YOU', (20,60), cv2.FONT_HERSHEY_SIMPLEX, 1, (50,25,25), 4, cv2.LINE_AA)
                counter += 1
                if (counter == 25):
                    os.system("start thankyou.mp3")
                    counter = 0

            if (angle_right > 165) and (flag_thankyou == "Detected"):

                flag_love = "Not Detected"
                flag_thankyou = "Not Detected"

            if (angle_right > 15 and angle_right < 75) and (angle_left > 15 and angle_left < 75):

                flag_love = "Detected"
                flag_thankyou = "Not Detected"
                cv2.putText(image, 'LOVE', (20,60), cv2.FONT_HERSHEY_SIMPLEX, 1, (50,25,25), 4, cv2.LINE_AA)
                counter += 1
                if (counter == 25):
                    os.system("start love.mp3")
                    counter = 0

        except:
            pass

        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS, mp_drawing.DrawingSpec(color=(250,100,50), thickness=2, circle_radius=4), mp_drawing.DrawingSpec(color=(250,50,250), thickness=2, circle_radius=4))
        cv2.imshow('Camera Stream', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
