import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
import sys
from window import Ui_MainWindow
import mediapipe as mp
import cv2
import math

class Mywindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.camerabutton.clicked.connect(self.processcamera)
        self.photobutton.clicked.connect(self.processphoto)
        self.videobutton.clicked.connect(self.processvideo)

    def processcamera(self):
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # 使用默认摄像头进行展示
        self.camerainput.setText("摄像头打开")
        while True:
            # 无限循环，提取摄像头中每一帧图像
            ret, img = cap.read()    #返回布尔值ret，若是true表示此帧图像已被获取
            img = cv2.resize(img, img_shape)   #修改窗口大小
            if ret:
                hand_landmarks = findHands(img, hands, draw) # 调用findHands函数找到手的特征
                # 调用detectNumber函数来识别手势对应的数字
                if hand_landmarks:
                    detected_Number = detectNumber(hand_landmarks, img)
                    if detected_Number >= 0:
                        if detected_Number == 66:
                            cv2.putText(img, "good", (int(img_shape[0] / 2), 200), cv2.FONT_ITALIC, 5, (255, 255, 255), 10)# putText函数把数字显示到窗口
                            self.output.setText("good")  #将结果输出到交互界面上
                        elif detected_Number == 55:
                            cv2.putText(img, "rock", (int(img_shape[0] / 2), 200), cv2.FONT_ITALIC, 5, (255, 255, 255), 10)
                            self.output.setText("rock")
                        elif detected_Number == 44:
                            cv2.putText(img, "ok", (int(img_shape[0] / 2), 200), cv2.FONT_ITALIC, 5, (255, 255, 255), 10)
                            self.output.setText("ok")
                        else:
                            cv2.putText(img, str(detected_Number), (int(img_shape[0] / 2), 200), cv2.FONT_ITALIC, 5,
                                        (255, 255, 255), 10)
                            self.output.setText(str(detected_Number))
                cv2.imshow("video", img)#修改视频窗口名称
            if cv2.waitKey(1) == ord('b'):  # 按下b键退出窗口
                self.camerainput.setText("摄像头关闭")
                break

    def processphoto(self):
        filename = QFileDialog.getOpenFileNames(self, '选择图像', os.getcwd(), "All Files(*);;Text Files(*.txt)")
        filepath = filename[0][0]
        self.photoinput.setText(filepath)  #交互界面上显示路径
        cap = cv2.VideoCapture(filepath)
        ret, img = cap.read()
        img = cv2.resize(img, img_shape)
        if ret:
            hand_landmarks = findHands(img, hands, draw)# 调用findHands函数找到手的特征
            if hand_landmarks:
                detected_Number = detectNumber(hand_landmarks, img)# 调用detectNumber函数来识别手势对应的数字
                if detected_Number >= 0:
                    if detected_Number == 66:
                        cv2.putText(img, "good", (int(img_shape[0] / 2), 200), cv2.FONT_ITALIC, 5, (255, 255, 255), 10)# 把数字显示到窗口
                        self.output.setText("good")
                    elif detected_Number == 55:
                        cv2.putText(img, "rock", (int(img_shape[0] / 2), 200), cv2.FONT_ITALIC, 5, (255, 255, 255), 10)
                        self.output.setText("rock")
                    elif detected_Number == 44:
                        cv2.putText(img, "ok", (int(img_shape[0] / 2), 200), cv2.FONT_ITALIC, 5, (255, 255, 255), 10)
                        self.output.setText("ok")
                    else:
                        cv2.putText(img, str(detected_Number), (int(img_shape[0] / 2), 200), cv2.FONT_ITALIC, 5,
                                    (255, 255, 255), 10)
                        self.output.setText(str(detected_Number))
            cv2.imshow("video", img)

    def processvideo(self):
        filename = QFileDialog.getOpenFileNames(self, '选择图像', os.getcwd(), "All Files(*);;Text Files(*.txt)")
        filepath = filename[0][0]
        self.videoinput.setText(filepath)
        cap = cv2.VideoCapture(filepath)
        while True:
            # 提取摄像头中每一帧图像
            ret, img = cap.read()
            img = cv2.resize(img, img_shape)
            if ret:
                hand_landmarks = findHands(img, hands, draw) # 调用findHands函数找到手的特征
                if hand_landmarks:
                    detected_Number = detectNumber(hand_landmarks, img)# 调用detectNumber函数来识别手势对应的数字
                    if detected_Number >= 0:
                        if detected_Number == 66:
                            cv2.putText(img, "good", (int(img_shape[0] / 2), 200), cv2.FONT_ITALIC, 5, (255, 255, 255), 10) # 把数字显示到窗口
                            self.output.setText("good")
                        elif detected_Number == 55:
                            cv2.putText(img, "rock", (int(img_shape[0] / 2), 200), cv2.FONT_ITALIC, 5, (255, 255, 255), 10)
                            self.output.setText("rock")
                        elif detected_Number == 44:
                            cv2.putText(img, "ok", (int(img_shape[0] / 2), 200), cv2.FONT_ITALIC, 5, (255, 255, 255), 10)
                            self.output.setText("ok")
                        else:
                            cv2.putText(img, str(detected_Number), (int(img_shape[0] / 2), 200), cv2.FONT_ITALIC, 5,
                                        (255, 255, 255), 10)
                            self.output.setText(str(detected_Number))
                cv2.imshow("video", img)
            if cv2.waitKey(1) == ord('b'):  # 按下b键退出窗口
                break

hands = mp.solutions.hands.Hands()#获取MediaPipe中hands的初始化对象
draw = mp.solutions.drawing_utils#获取MediaPipe中draw的初始化对象
img_shape = (800, 600)

def findHands(img,hands,draw):
    """
    找出img图像中是否存在手部，如果有，将手部所有特征点画出来并连线
    :param img: 视频流中每一帧图片
    :param hands: mp的手部solution对象
    :param draw: mp的画图solution对象
    :return: 手部的所有特征landmarks
    """
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #定义轮廓画图风格
    handlmsstyle = draw.DrawingSpec(color=(0, 0, 255), thickness=3)
    handconstyle = draw.DrawingSpec(color=(255, 255, 255), thickness=3)
    #mp去寻找视频流中手部位置，并且把所有的landmarks提取出来
    results = hands.process(imgRGB)
    #如果找到手
    if results.multi_hand_landmarks:
        #出现在视频中的所有手部特征画出来
        for handLms in results.multi_hand_landmarks:
            draw.draw_landmarks(img, handLms, mp.solutions.hands.HAND_CONNECTIONS, handlmsstyle, handconstyle)
    return results.multi_hand_landmarks

def detectNumber(hand_landmarks, img):
    """
    根据手部的手势识别出不同的数字
    :param hand_landmarks: 手部特征
    :param img: 图像
    :return: 返回识别到的数字，如果没有返回-1
    """
    #取出图片的宽和高
    h, w, c=img.shape
    #找到第一只手的特征，并且提取出来
    myHand = hand_landmarks[0]
    hand_landmarks = myHand.landmark

    #找出我们所需的手指的特征点并赋给id值
    thumb_tip_id = 4
    index_finger_tip_id = 8
    middle_finger_tip_id = 12
    ring_finger_tip_id = 16
    pinky_tip_id = 20
    pinky_mcp_id = 17
    wrist_id = 0
    index_finger_mcp_id = 5

    dist_thresh = 100#阈值
    dist_thresh1 = 180
    dist_thresh2 = 30

    #把所有特征点坐标x，y提取出来
    #提取出y
    thumb_tip_y = hand_landmarks[thumb_tip_id].y * h    #拇指顶端
    index_finger_tip_y = hand_landmarks[index_finger_tip_id].y * h  #食指顶端
    middle_finger_tip_y = hand_landmarks[middle_finger_tip_id].y * h   #中指顶端
    ring_finger_tip_y = hand_landmarks[ring_finger_tip_id].y * h    #无名指顶端
    pinky_tip_y = hand_landmarks[pinky_tip_id].y * h     #尾指顶端
    pinky_mcp_y = hand_landmarks[pinky_mcp_id].y * h     #尾指的mcp点
    wrist_y = hand_landmarks[wrist_id].y * h    #手腕
    index_finger_mcp_y = hand_landmarks[index_finger_mcp_id].y * h   #食指的mcp点

    # 提出x
    thumb_tip_x = hand_landmarks[thumb_tip_id].x * w
    index_finger_tip_x = hand_landmarks[index_finger_tip_id].x * w
    middle_finger_tip_x = hand_landmarks[middle_finger_tip_id].x * w
    ring_finger_tip_x = hand_landmarks[ring_finger_tip_id].x * w
    pinky_tip_x = hand_landmarks[pinky_tip_id].x * w
    pinky_mcp_x = hand_landmarks[pinky_mcp_id].x * w
    wrist_x = hand_landmarks[wrist_id].x * w
    index_finger_mcp_x = hand_landmarks[index_finger_mcp_id].x * w

    #计算距离
    dist_thumbtoindex = math.sqrt((thumb_tip_x - index_finger_tip_x) ** 2 + (thumb_tip_y - index_finger_tip_y) ** 2)  #大拇指tip到食指tip
    dist_thumbtomiddle = math.sqrt((thumb_tip_x - middle_finger_tip_x) ** 2 + (thumb_tip_y - middle_finger_tip_y) ** 2) #大拇指tip到中指tip
    dist_thumbtoring = math.sqrt((thumb_tip_x - ring_finger_tip_x) ** 2 + (thumb_tip_y - ring_finger_tip_y) ** 2)  #大拇指tip到无名指tip
    dist_thumbtopinky = math.sqrt((thumb_tip_x - pinky_tip_x) ** 2 + (thumb_tip_y - pinky_tip_y) ** 2)      #大拇指tip到尾指tip
    dist_thumbtopinkymcp = math.sqrt((thumb_tip_x - pinky_mcp_x) ** 2 + (thumb_tip_y - pinky_mcp_y) ** 2)   #大拇指tip到尾指mcp
    dist_wristtothumb = math.sqrt((wrist_x - thumb_tip_x) ** 2 + (wrist_y - thumb_tip_y) ** 2)  # 手腕到大拇指tip
    dist_wristtoindex = math.sqrt((wrist_x - index_finger_tip_x) ** 2 + (wrist_y - index_finger_tip_y) ** 2) #手腕到食指tip
    dist_wristtomiddle = math.sqrt((wrist_x - middle_finger_tip_x) ** 2 + (wrist_y - middle_finger_tip_y) ** 2) #手腕到中指tip
    dist_wristtoring = math.sqrt((wrist_x - ring_finger_tip_x) ** 2 + (wrist_y - ring_finger_tip_y) ** 2)  #手腕到无名指tip
    dist_wristtopinky = math.sqrt((wrist_x - pinky_tip_x) ** 2 + (wrist_y - pinky_tip_y) ** 2)  #手腕到尾指tip
    dist_indextiptoindexmcp = math.sqrt((index_finger_tip_x - index_finger_mcp_x) ** 2 + (index_finger_tip_y - index_finger_mcp_y) ** 2)  #食指tip到食指mcp
    dist_thumbtiptoindextip = math.sqrt((thumb_tip_x - index_finger_tip_x) ** 2 + (thumb_tip_y - index_finger_tip_y) ** 2)
    #print(dist_thumbtoindex, dist_thumbtomiddle, dist_thumbtoring, dist_thumbtopinky, dist_thumbtopinkymcp)

    #判断并返回结果
    if dist_wristtopinky < dist_thresh and dist_wristtoring < dist_thresh and dist_wristtomiddle < dist_thresh and dist_wristtoindex < dist_thresh and dist_wristtothumb < dist_thresh:
        return 0
    elif dist_wristtopinky < dist_thresh and dist_wristtoring < dist_thresh and dist_wristtomiddle < dist_thresh and dist_wristtoindex > dist_thresh1 and dist_wristtothumb < dist_thresh:
        return 1
    elif dist_wristtopinky < dist_thresh and dist_wristtoring < dist_thresh and dist_wristtomiddle < dist_thresh and dist_wristtoindex < dist_thresh1 and dist_wristtothumb < dist_thresh:
        return 9
    elif dist_thumbtopinky < dist_thresh and dist_thumbtoindex > dist_thresh and dist_thumbtomiddle > dist_thresh and dist_thumbtoring < dist_thresh:
        return 2
    elif dist_thumbtopinky < dist_thresh and dist_thumbtoindex > dist_thresh and dist_thumbtomiddle > dist_thresh and dist_thumbtoring > dist_thresh:
        return 3
    elif dist_thumbtopinky > dist_thresh and dist_thumbtoindex > dist_thresh and dist_thumbtomiddle > dist_thresh and dist_thumbtoring > dist_thresh and dist_thumbtopinkymcp < dist_thresh:
        return 4
    elif dist_thumbtopinky > dist_thresh and dist_thumbtoindex > dist_thresh and dist_thumbtomiddle > dist_thresh and dist_thumbtoring > dist_thresh and dist_thumbtopinkymcp > dist_thresh and dist_wristtoindex > dist_thresh and dist_wristtomiddle > dist_thresh and dist_wristtoring > dist_thresh:
        return 5
    elif dist_thumbtopinky > dist_thresh and dist_wristtoindex < dist_thresh and dist_wristtomiddle < dist_thresh and dist_wristtoring < dist_thresh and dist_wristtopinky > dist_thresh:
        return 6
    elif dist_wristtopinky < dist_thresh and dist_wristtoring < dist_thresh and dist_thumbtoindex < dist_thresh and dist_thumbtomiddle < dist_thresh and dist_wristtomiddle > dist_thresh and dist_wristtoindex > dist_thresh and dist_wristtothumb > dist_thresh:
        return 7
    elif dist_wristtopinky < dist_thresh and dist_wristtoring < dist_thresh and dist_wristtomiddle < dist_thresh and dist_wristtoindex > dist_thresh and dist_thumbtoindex > dist_thresh and dist_thumbtomiddle > dist_thresh:
        return 8
    elif dist_wristtopinky < dist_thresh and dist_wristtoring < dist_thresh and dist_wristtomiddle < dist_thresh and dist_wristtoindex < dist_thresh and dist_thumbtoindex > dist_thresh and dist_thumbtomiddle > dist_thresh:
        return 66
    elif dist_wristtopinky > dist_thresh and dist_wristtoring < dist_thresh and dist_wristtomiddle < dist_thresh and dist_wristtoindex > dist_thresh and dist_thumbtoindex > dist_thresh and dist_thumbtomiddle > dist_thresh:
        return 55
    elif dist_thumbtiptoindextip < dist_thresh2 and dist_wristtoindex > dist_thresh and dist_wristtomiddle > dist_thresh and dist_wristtoring > dist_thresh:
        return 44
    else:
        return -1

if __name__== '__main__' :
    app = QApplication(sys.argv)
    myWindow = Mywindow()
    myWindow.show()
    sys.exit(app.exec_())
