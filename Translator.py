import cv2 as ocv
import mediapipe as mp
import multiprocessing
import asyncio
import websockets
import os
from gtts import gTTS
mpHands = mp.solutions.hands
hands = mpHands.Hands(False, 2, 1, 0.5, 0.5)
mpDrawings = mp.solutions.drawing_utils
frames = ocv.VideoCapture(0)

fingerTips = [8, 12, 16, 20]
handColor = (255, 0, 0)
language = 'en'
isRight = True

async def main(websocket):
    counter = 0
    iloveyou_text = "I Love You!"
    iloveyou_object = gTTS(text=iloveyou_text, lang=language, slow=True)
    iloveyou_object.save("iloveyou.mp3")

    stop_text = "Stop!"
    stop_object = gTTS(text=stop_text, lang=language, slow=True)
    stop_object.save("stop.mp3")

    like_text = "Like!"
    like_object = gTTS(text=like_text, lang=language, slow=True)
    like_object.save("like.mp3")

    dislike_text = "Dislike!"
    dislike_object = gTTS(text=dislike_text, lang=language, slow=True)
    dislike_object.save("dislike.mp3")

    victory_text = "Victory!"
    victory_object = gTTS(text=victory_text, lang=language, slow=True)
    victory_object.save("victory.mp3")

    okay_text = "Okay!"
    okay_object = gTTS(text=okay_text, lang=language, slow=True)
    okay_object.save("okay.mp3")

    A_text = "A!"
    A_object = gTTS(text=A_text, lang=language, slow=True)
    A_object.save("A_sound.mp3")

    S_text = "S!"
    S_object = gTTS(text=S_text, lang=language, slow=True)
    S_object.save("S_sound.mp3")

    L_text = "L!"
    L_object = gTTS(text=L_text, lang=language, slow=True)
    L_object.save("L_sound.mp3")

    D_text = "D!"
    D_object = gTTS(text=D_text, lang=language, slow=True)
    D_object.save("D_sound.mp3")

    C_text = "C!"
    C_object = gTTS(text=C_text, lang=language, slow=True)
    C_object.save("C_sound.mp3")
    while True:

        status, images = frames.read()
        images = ocv.flip(images, 1)
        height, width, channel = images.shape
        handsDetection = hands.process(images)

        if handsDetection.multi_hand_landmarks:
            myHands = []
            handsType = []
            for hand in handsDetection.multi_handedness:
                handType = hand.classification[0].label
                handsType.append(handType)

            for handType in handsType:
                if handType == "Right":
                    handColor = (0, 0, 255)
        if handsDetection.multi_hand_landmarks:
            myHands = []
            handsType = []
            for hand in handsDetection.multi_handedness:
                handType = hand.classification[0].label
                handsType.append(handType)

            for handType in handsType:
                if handType == "Right":
                    handColor = (0, 0, 255)
                    isRight = True
                if handType == "Left":
                    handColor = (0, 255, 0)
                    isRight = False

            for handLandmarks in handsDetection.multi_hand_landmarks:
                landmarkList = []

                for id, lm in enumerate(handLandmarks.landmark):
                    landmarkList.append(lm)

                fingerFoldingStatus = []

                for tip in fingerTips:
                    x, y = int(landmarkList[tip].x * width), int(
                        landmarkList[tip].y * height
                    )
                    # ocv.circle(images, (x, y), 15, (0, 255, 0), ocv.FILLED)

                    if not ((landmarkList[tip].x > landmarkList[tip - 2].x) ^ isRight):
                        # ocv.circle(images, (x, y), 15, (0, 255, 255), ocv.FILLED)
                        fingerFoldingStatus.append(True)
                    else:
                        fingerFoldingStatus.append(False)

                if (
                    (landmarkList[4].y < landmarkList[3].y < landmarkList[2].y)
                    and (landmarkList[8].y < landmarkList[7].y < landmarkList[6].y)
                    and (landmarkList[12].y < landmarkList[11].y < landmarkList[10].y)
                    and (landmarkList[16].y < landmarkList[15].y < landmarkList[14].y)
                    and (landmarkList[20].y < landmarkList[19].y < landmarkList[18].y)
                    ):
                    ocv.putText(
                        images,
                        "STOP",
                        (20, 60),
                        ocv.FONT_HERSHEY_SIMPLEX,
                        2,
                        (0, 255, 0),
                        6,
                    )
                    counter += 1
                    if (counter == 25):
                        os.system("open stop.mp3")
                        counter = 0

                if (
                    (not (landmarkList[4].x < landmarkList[3].x < landmarkList[2].x) ^ isRight)
                    and (landmarkList[8].y < landmarkList[7].y < landmarkList[6].y)
                    and (landmarkList[12].y > landmarkList[11].y > landmarkList[10].y)
                    and (landmarkList[16].y > landmarkList[15].y > landmarkList[14].y)
                    and (landmarkList[20].y < landmarkList[19].y < landmarkList[18].y)
                    ):
                    ocv.putText(
                        images,
                        "I LOVE YOU",
                        (20, 60),
                        ocv.FONT_HERSHEY_SIMPLEX,
                        2,
                        (0, 255, 0),
                        6,
                    )
                    counter += 1
                    if (counter == 25):
                        os.system("open iloveyou.mp3")
                        counter = 0

                if (
                    (not ((landmarkList[4].x > landmarkList[2].x) ^ isRight))
                    and (landmarkList[8].y < landmarkList[7].y < landmarkList[6].y)
                    and (landmarkList[12].y < landmarkList[11].y < landmarkList[10].y)
                    and (landmarkList[16].y > landmarkList[14].y)
                    and (landmarkList[20].y > landmarkList[18].y)
                    ):
                    ocv.putText(
                        images,
                        "VICTORY",
                        (20, 60),
                        ocv.FONT_HERSHEY_SIMPLEX,
                        2,
                        (0, 255, 0),
                        6,
                    )
                    counter += 1
                    if (counter == 25):
                        os.system("open victory.mp3")
                        counter = 0

                if (
                    (not ((landmarkList[4].x < landmarkList[2].x) ^ isRight))
                    and (landmarkList[8].y > landmarkList[6].y)
                    and (landmarkList[12].y < landmarkList[11].y < landmarkList[10].y)
                    and (landmarkList[16].y < landmarkList[15].y < landmarkList[14].y)
                    and (landmarkList[20].y < landmarkList[19].y < landmarkList[18].y)
                    ):
                    ocv.putText(
                        images,
                        "OKAY",
                        (20, 60),
                        ocv.FONT_HERSHEY_SIMPLEX,
                        2,
                        (0, 255, 0),
                        6,
                    )
                    counter += 1
                    if (counter == 25):
                        os.system("open okay.mp3")
                        counter = 0

                if (
                    (landmarkList[4].y < landmarkList[3].y < landmarkList[2].y)
                    and (landmarkList[8].y > landmarkList[7].y > landmarkList[5].y > landmarkList[6].y)
                    and (landmarkList[12].y > landmarkList[11].y > landmarkList[9].y > landmarkList[10].y)
                    and (landmarkList[16].y > landmarkList[15].y > landmarkList[14].y)
                    and (landmarkList[20].y > landmarkList[19].y > landmarkList[18].y)
                    ):
                    ocv.putText(
                        images,
                        "A",
                        (20, 60),
                        ocv.FONT_HERSHEY_SIMPLEX,
                        2,
                        (0, 255, 0),
                        6,
                    )
                    counter += 1
                    if (counter == 25):
                        os.system("open A_sound.mp3")
                        counter = 0

                if (
                    (not ((landmarkList[4].x > landmarkList[2].x) ^ isRight))
                    and (landmarkList[8].y < landmarkList[7].y < landmarkList[6].y)
                    and (landmarkList[12].y > landmarkList[11].y > landmarkList[10].y)
                    and (landmarkList[16].y > landmarkList[15].y > landmarkList[14].y)
                    and (landmarkList[20].y > landmarkList[19].y > landmarkList[18].y)
                    ):
                    ocv.putText(
                        images,
                        "D",
                        (20, 60),
                        ocv.FONT_HERSHEY_SIMPLEX,
                        2,
                        (0, 255, 0),
                        6,
                    )
                    counter += 1
                    if (counter == 25):
                        os.system("open D_sound.mp3")
                        counter = 0

                if (
                    (not ((landmarkList[4].x < landmarkList[3].x < landmarkList[2].x) ^ isRight))
                    and (landmarkList[8].y < landmarkList[7].y < landmarkList[6].y)
                    and (landmarkList[12].y > landmarkList[11].y > landmarkList[10].y)
                    and (landmarkList[16].y > landmarkList[15].y > landmarkList[14].y)
                    and (landmarkList[20].y > landmarkList[19].y > landmarkList[18].y)
                    ):
                    ocv.putText(
                        images,
                        "L",
                        (20, 60),
                        ocv.FONT_HERSHEY_SIMPLEX,
                        2,
                        (0, 255, 0),
                        6,
                    )
                    counter += 1
                    if (counter == 25):
                        os.system("open L_sound.mp3")
                        counter = 0

                if (
                    (not ((landmarkList[4].x > landmarkList[2].x) ^ isRight))
                    and (landmarkList[4].y < landmarkList[2].y)
                    and ((landmarkList[6].y < landmarkList[5].y) and (landmarkList[6].y < landmarkList[8].y))
                    and ((landmarkList[10].y < landmarkList[9].y) and (landmarkList[10].y < landmarkList[12].y))
                    and (landmarkList[16].y > landmarkList[15].y > landmarkList[14].y)
                    and (landmarkList[20].y > landmarkList[19].y > landmarkList[18].y)
                ):
                    ocv.putText(
                        images,
                        "S",
                        (20, 60),
                        ocv.FONT_HERSHEY_SIMPLEX,
                        2,
                        (0, 255, 0),
                        6,
                    )
                    counter += 1
                    if (counter == 25):
                        os.system("open S_sound.mp3")
                        counter = 0

                if (
                    (not ((landmarkList[4].x < landmarkList[2].x) ^ isRight))
                    and (not ((landmarkList[8].x < landmarkList[7].x < landmarkList[6].x) ^ isRight))
                    and (not ((landmarkList[12].x < landmarkList[11].x < landmarkList[10].x) ^ isRight))
                    and (not ((landmarkList[16].x < landmarkList[15].x < landmarkList[14].x) ^ isRight))
                    and (not ((landmarkList[20].x < landmarkList[19].x < landmarkList[18].x) ^ isRight))
                    ):
                    ocv.putText(
                        images,
                        "C",
                        (20, 60),
                        ocv.FONT_HERSHEY_SIMPLEX,
                        2,
                        (0, 255, 0),
                        6,
                    )
                    counter += 1
                    if (counter == 25):
                        os.system("open C_sound.mp3")
                        counter = 0

                if all(fingerFoldingStatus):
                    if landmarkList[4].y < landmarkList[3].y < landmarkList[2].y:
                        ocv.putText(
                            images,
                            "LIKE",
                            (20, 60),
                            ocv.FONT_HERSHEY_SIMPLEX,
                            2,
                            (0, 255, 0),
                            6,
                        )
                        counter += 1
                        if (counter == 25):
                            os.system("open like.mp3")
                            counter = 0
                    if landmarkList[4].y > landmarkList[3].y > landmarkList[2].y:
                        ocv.putText(
                            images,
                            "DISLIKE",
                            (20, 60),
                            ocv.FONT_HERSHEY_SIMPLEX,
                            2,
                            (0, 255, 0),
                            6,
                        )
                        counter += 1
                        if (counter == 25):
                            os.system("open dislike.mp3")
                            counter = 0

                mpDrawings.draw_landmarks(
                    images,
                    handLandmarks,
                    mpHands.HAND_CONNECTIONS,
                    mpDrawings.DrawingSpec(handColor, 5, 2),
                    mpDrawings.DrawingSpec((255, 0, 0), 3, 2),
                )

        encode_param = [int(ocv.IMWRITE_JPEG_QUALITY), 200]
        lst[0] = ocv.imencode('.jpg', images)[1]
        await websocket.send(lst[0].tobytes())
        k = ocv.waitKey(1)
        if k == 27:
            ocv.destroyAllWindows()
            break

async def run_server():
    async with websockets.serve(main, "0.0.0.0", 1234):
        await asyncio.Future()

if __name__ == '__main__':
    manager = multiprocessing.Manager()
    lst = manager.list()
    lst.append(None)
    asyncio.run(run_server())