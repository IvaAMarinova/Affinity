import sys
import webbrowser
import cv2
import time
import os
import threading
import queue
import numpy as np
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame, QHBoxLayout, QTextEdit, QTextBrowser, QLabel, QLayout, QStyle, QTimeEdit, QDateEdit, QDateTimeEdit
from PyQt5.QtMultimedia import QCameraInfo
from PyQt5.QtCore import QDate, QTime, QDateTime, QTimer
from PyQt5.QtGui import QIcon, QFont, QPalette, QMovie, QPixmap, QImage, QBrush


setStyleMain = """ QWidget{
    font-family: "Courier"; 
    background-color: black;
}"""
setStyleQte = """QTextEdit {
    font-family: "Courier"; 
    font-size: 12pt; 
    font-weight: 600; 
    text-align: right;
    border-radius: 15px;
    border :3px solid ;
    border-color: black;
    background-color: Purple;
}"""

setStyletui = """QTextBrowser {
    font-family: "Comfortaa";
    font-weight: 600; 
    text-align: left;
    border-radius: 15px;
    border :3px solid ;
    border-color: DarkPurple;
    color: lightgray;
    background-color: darkblue;
}"""
setStyleBut = """QPushButton {
    font-family: "Old London";
    font-weight: 700;
    border :3px solid ;
    border-radius: 30px;
    border-color: black;
    background-color: Purple;
    box-shadow: 0px -3px 5px;
}"""
setStyleBut_c = """QPushButton {
    border-radius : 50px; 
    border : 3px solid black;
    font-weight: 700;
    background-color: Lightblue;
}"""
setStylefr = """QFrame {
    font-family: "Comfortaa";
    font-weight: 600;
    border :3px solid ;
    border-radius: 15px;
    border-color: darkBlue;
    background-color: Black;
}"""
setStyledt = """QLabel {
    font-family: "Comfortaa";
    font-weight: 700;
    color: darkBlue;
    background-color: Black;
}"""

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.t = 'AFFY'
        self.setWindowTitle(self.t)
        self.setGeometry(200,100,700,700)
        self.setStyleSheet(setStyleMain)
        self.font = QFont()
        self.fontt = QFont()
        self.font.setPointSize(13)
        self.fontt.setPointSize(20)
        self.Date_time()
        self.Label()
        self.chatlog = QtWidgets.QTextBrowser()
        self.userinput = QtWidgets.QTextEdit()
        self.frame = QFrame(self)
        self.hide = True
        self.image_label = QtWidgets.QLabel(self)
        self.image_label.setGeometry(1400, 10, 500, 300)
        self.timer = QTimer()
        self.camera_button()
        self.timer.timeout.connect(self.viewCam)
        self.Youtube_button()
        self.Classroom_button()
        self.Tues_button()
        self.Gmail_button()
        self.Insta_button()
        self.Facebook_button()
        self.Linkedin_button()
        self.Twitter_button()
        self.chat_box_button()
        self.hide_chat()
        self.chat_box()
        self.getBotMessage()
        self.user_to_bot()
        self.bot_to_user()
        self.Gui_style_setup()
        self.show()
        
    def Gui_style_setup(self):
        self.chatlog.setStyleSheet(setStyletui)
        self.userinput.setStyleSheet(setStyleQte)
        self.userinput.setFont(self.font)
        self.chatlog.setFont(self.font)
        

    def chat_box_button(self):
        cb = QPushButton("ChatBox", self)
        cb.setGeometry(100, 850, 200, 70)
        cb.setStyleSheet(setStyleBut)
        cb.setFont(self.font)
        cb.clicked.connect(self.hide_chat)


    def camera_button(self):
        cam_b = QPushButton("Camera", self)
        cam_b.setGeometry(100, 750, 200, 70)
        cam_b.setStyleSheet(setStyleBut)
        cam_b.setFont(self.font)
        cam_b.clicked.connect(self.controlTimer)

    
    def viewCam(self):
        ret, image = self.cap.read()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channel = image.shape
        step = channel * width
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        self.image_label.setPixmap(QPixmap.fromImage(qImg))

    def controlTimer(self):
        if not self.timer.isActive():
            self.cap = cv2.VideoCapture(0)
            self.timer.start(20)
        else:
            self.timer.stop()
            self.image_label.clear()
            self.cap.release()



    def Youtube_button(self):
        cam_b = QPushButton("Youtube", self)
        cam_b.setGeometry(100, 650, 200, 70)
        cam_b.setStyleSheet(setStyleBut)
        cam_b.setFont(self.font)
        cam_b.clicked.connect(lambda: webbrowser.open('http://www.youtube.com'))


    def Classroom_button(self):
        cam_b = QPushButton("Classroom", self)
        cam_b.setGeometry(100, 550, 200, 70)
        cam_b.setStyleSheet(setStyleBut)
        cam_b.setFont(self.font)
        cam_b.clicked.connect(lambda: webbrowser.open('http://www.classroom.com'))


    def Tues_button(self):
        cam_b = QPushButton("Tues", self)
        cam_b.setGeometry(100, 450, 200, 70)
        cam_b.setStyleSheet(setStyleBut)
        cam_b.setFont(self.font)
        cam_b.clicked.connect(lambda: webbrowser.open('http://www.elsys-bg.org'))


    def Gmail_button(self):
        cam_b = QPushButton("Gmail", self)
        cam_b.setGeometry(100, 350, 200, 70)
        cam_b.setStyleSheet(setStyleBut)
        cam_b.setFont(self.font)
        cam_b.clicked.connect(lambda: webbrowser.open('http://www.gmail.com'))

    def Insta_button(self):
        cam_b = QPushButton("Insta", self)
        cam_b.setGeometry(500, 100, 100, 100)
        cam_b.setStyleSheet(setStyleBut_c)
        cam_b.setFont(self.font)
        cam_b.clicked.connect(lambda: webbrowser.open('http://www.instagram.com'))

    
    def Facebook_button(self):
        cam_b = QPushButton("Facebook", self)
        cam_b.setGeometry(650, 100, 100, 100)
        cam_b.setStyleSheet(setStyleBut_c)
        cam_b.setFont(self.font)
        cam_b.clicked.connect(lambda: webbrowser.open('http://www.facebook.com'))


    def Linkedin_button(self):
        cam_b = QPushButton("Linkin", self)
        cam_b.setGeometry(800, 100, 100, 100)
        cam_b.setStyleSheet(setStyleBut_c)
        cam_b.setFont(self.font)
        cam_b.clicked.connect(lambda: webbrowser.open('http://www.linkedin.com'))


    def Twitter_button(self):
        cam_b = QPushButton("Twitter", self)
        cam_b.setGeometry(950, 100, 100, 100)
        cam_b.setStyleSheet(setStyleBut_c)
        cam_b.setFont(self.font)
        cam_b.clicked.connect(lambda: webbrowser.open('http://www.twitter.com'))



    def hide_chat(self):
        if self.hide == True:
            self.frame.hide()
            self.hide = False
        else:
            self.frame.show()
            self.hide = True
        

    def chat_box(self):
        box = QHBoxLayout()
        self.frame.setFrameStyle(QFrame.Panel)
        self.frame.setGeometry(1400, 350, 500, 600)
        self.frame.setStyleSheet(setStylefr)
        self.frame.setLineWidth(2)

        box.addChildWidget(self.frame)

        self.userinput = QtWidgets.QTextEdit(self.frame)
        self.chatlog = QtWidgets.QTextBrowser(self.frame)
        self.userinput.move(10, 510)
        self.userinput.resize(400, 80)
        self.chatlog.move(10, 10)
        self.chatlog.resize(400, 500)

        B_enter =  QPushButton("Enter", self.frame)
        B_enter.setStyleSheet(setStyleBut)
        B_enter.setFont(self.font)
        B_enter.setGeometry(410, 520, 80, 60)
        B_enter.clicked.connect(self.user_to_bot)
        B_enter.clicked.connect(self.userinput.clear)

        box.addChildWidget(B_enter)
        box.addChildWidget(self.userinput)
        box.addChildWidget(self.chatlog)
        self.bot_to_user()


    def bot_to_user(self):
        bmsg = self.getBotMessage()
        self.chatlog.setText('Affy:' + bmsg)
        self.userinput.setFocus()


    def user_to_bot(self):
        usmg = self.userinput.toPlainText()
        self.chatlog.append('me:' + usmg)


    def getBotMessage(self):
        mes = 'hey muce'
        return mes


    def Label(self):
        pic = QLabel(self)
        pic.setGeometry(550, 300, 600, 400)
        movie = QMovie("siri2.gif")
        pic.setMovie(movie)
        movie.start()


    def Date_time(self):
        nowd = QDate.currentDate()
        nowt = QTime.currentTime()
        text = QLabel(self)
        text_now = nowd.toString('dd.MM.yyyy')
        text_now1 = nowt.toString('hh:mm')
        text.setText(text_now1 + '\n' + text_now)
        text.setGeometry(100, 100, 400, 100)
        text.setStyleSheet(setStyledt)
        text.setFont(self.fontt)
        
        

if __name__ == '__main__':
    application = QApplication(sys.argv)
    e = MainWindow()
    sys.exit(application.exec())