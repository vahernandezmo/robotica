import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget
from moveRobot import Robot

class MainApp(QWidget):
    def __init__(self, parent = None, *args):
        super(MainApp, self).__init__(parent=parent)
        self.setMinimumSize(854,480) 
        self.setMaximumSize(1280,720)
        self.setWindowTitle("Pincher Controller")  
        self.setWindowIcon(QIcon('robot.png'))
        self.pose=""
        self.image='images/home.png'
        self.setStyleSheet("background-color:#0D1117; color: #ffffff; font-family:calibri;")
        self.joint1Value = 0.0
        self.joint2Value = 0.0
        self.joint3Value = 0.0
        self.joint4Value = 0.0

        title = """
        Robótica - Laboratorio 4
        Valentina Hernández - Felipe Gutierrez - Manuel Rojas
        """

        width = self.frameGeometry().width()
        height = self.frameGeometry().height()
        #self.widget = QWidget(self)
        

        label = QLabel(title, self)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("background:#1D2734; color: #ffffff;font-size:18px; font-family:calibri;")

        
        """
        names_label = QLabel("Valentina Hernández - Felipe Gutierrez - Manuel Rojas", self)
        names_label.setAlignment(Qt.AlignCenter)
        names_label.setStyleSheet("background:#1D2734; color: #ffffff;font-size:16px; font-family:calibri;")
        names_label.setGeometry(0,int(0.08*height),width,int(0.08*height))
        
        label.setGeometry(0,0,width,int(0.08*height))

        #self.setCentralWidget(label)
        """
        #create top level layout
        outerLayout = QVBoxLayout()
        middleLayout = QHBoxLayout()
        middleLayout.setSpacing(15)
        leftLayout  = QVBoxLayout()

        topLayout = QVBoxLayout()
        topLayout.addWidget(label)
        #topLayout.addWidget(names_label)

       

        pose1 = self.createRadioButton("Home", False)
        pose1.setStyleSheet("font-size:15px; QRadioButton::indicator" "{""border:10px solid #ffffff;""}")
        pose2 = self.createRadioButton("Pose 1", False)
        pose2.setStyleSheet("font-size:15px;")
        pose3 = self.createRadioButton("Pose 2", False)
        pose3.setStyleSheet("font-size:15px;")
        pose4 = self.createRadioButton("Pose 3", False)
        pose4.setStyleSheet("font-size:15px;")
        pose5 = self.createRadioButton("Pose 4", False)
        pose5.setStyleSheet("font-size:15px;")
        

        optionsLayout = QVBoxLayout()
        poseLabel = QLabel("Escoja la posición: ")
        poseLabel.setStyleSheet("font-size:16px; font-weight:bold;")
        optionsLayout.addWidget(poseLabel)
        optionsLayout.addWidget(pose1)
        optionsLayout.addWidget(pose2)
        optionsLayout.addWidget(pose3)
        optionsLayout.addWidget(pose4)
        optionsLayout.addWidget(pose5)

        self.imageLayout = QVBoxLayout()
        self.imageLabel = QLabel(self)
        self.pixmap = QPixmap(self.image)
        self.imageLabel.setPixmap(self.pixmap)
        self.imageLabel.resize(self.pixmap.width(),
                          self.pixmap.height())
        self.imageLayout.addWidget(self.imageLabel)

        jointsLayout = QVBoxLayout()
        MotorLabel = QLabel("Valores articulares: ")
        MotorLabel.setStyleSheet("font-size:16px; font-weight:bold;")
        self.joint1Label = QLabel(f"Joint1: {self.joint1Value}")
        self.joint1Label.setStyleSheet("font-size:15px;")
        self.joint2Label = QLabel(f"Joint2: {self.joint2Value}")
        self.joint2Label.setStyleSheet("font-size:15px;")
        self.joint3Label = QLabel(f"Joint3: {self.joint3Value}")
        self.joint3Label.setStyleSheet("font-size:15px;")
        self.joint4Label = QLabel(f"Joint4: {self.joint1Value}")
        self.joint4Label.setStyleSheet("font-size:15px;")

        jointsLayout.addWidget(MotorLabel)
        jointsLayout.addWidget(self.joint1Label)
        jointsLayout.addWidget(self.joint2Label)
        jointsLayout.addWidget(self.joint3Label)
        jointsLayout.addWidget(self.joint4Label)
        
        leftLayout.addLayout(jointsLayout)
        leftLayout.addLayout(optionsLayout)
        
        middleLayout.addLayout(leftLayout)
        middleLayout.addLayout(self.imageLayout)

        outerLayout.addLayout(topLayout)
        outerLayout.addLayout(middleLayout)
        outerLayout.addStretch()


        self.setLayout(outerLayout)

        self.robot = Robot()
        self.robot.moveRobot('Home')
        
    # ----------------------------------- Events ----------------------------------- #
    def slot(self, value):
        radioButton = self.sender()
        if radioButton.isChecked():
            self.pose = radioButton.text()
            self.robot.moveRobot(self.pose)
            self.setImage()
            
    def setImage(self):
        if self.pose == 'Home':
            self.imageLabel.setPixmap(QPixmap(self.image))
            self.getJointValues()
        elif self.pose == 'Pose 1':
            self.imageLabel.setPixmap(QPixmap('images/pose1.png'))
            self.getJointValues()
        elif self.pose == 'Pose 2':
            self.imageLabel.setPixmap(QPixmap('images/pose2.png'))
            self.getJointValues()
        elif self.pose == 'Pose 3':
            self.imageLabel.setPixmap(QPixmap('images/pose3.png'))
            self.getJointValues()
        elif self.pose == 'Pose 4':
            self.imageLabel.setPixmap(QPixmap('images/pose4.png'))
            self.getJointValues()
    
    def getPose(self):
        return self.pose
    
    def getJointValues(self, offset=80):
            self.joint1Label.setText(f"Joint1: {str(self.robot.getJointsValues()[0])}")
            self.joint2Label.setText(f"Joint2: {str(self.robot.getJointsValues()[1])}")
            self.joint3Label.setText(f"Joint3: {str(round(self.robot.getJointsValues()[2]+offset))}")
            self.joint4Label.setText(f"Joint4: {str(self.robot.getJointsValues()[3])}")

    def createRadioButton(self, label, checked):
        radiobutton = QRadioButton(self)
        radiobutton.setText(label)
        radiobutton.setChecked(checked)
        radiobutton.toggled.connect(lambda: self.slot(label))
        return radiobutton
        

if __name__ == '__main__':
    app = QApplication([])
    window = MainApp()
    window.show()
    app.exec_()

