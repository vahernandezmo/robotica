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
        self.setStyleSheet("background-color:#0D1117; color: #ffffff; font-family:calibri;")

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
        leftLayout  = QVBoxLayout()

        topLayout = QVBoxLayout()
        topLayout.addWidget(label)
        #topLayout.addWidget(names_label)

       

        pose1 = self.createRadioButton("Pose 1", False)
        pose1.setStyleSheet("font-size:16px;")
        pose2 = self.createRadioButton("Pose 2", False)
        pose2.setStyleSheet("font-size:16px;")
        pose3 = self.createRadioButton("Pose 3", False)
        pose3.setStyleSheet("font-size:16px;")
        pose4 = self.createRadioButton("Pose 4", False)
        pose4.setStyleSheet("font-size:16px;")
        pose5 = self.createRadioButton("Pose 5", False)
        pose5.setStyleSheet("font-size:16px;")
        

        optionsLayout = QVBoxLayout()
        poseLabel = QLabel("Escoja la posición: ")
        poseLabel.setStyleSheet("font-size:18px; font-weight:bold;")
        optionsLayout.addWidget(poseLabel)
        optionsLayout.addWidget(pose1)
        optionsLayout.addWidget(pose2)
        optionsLayout.addWidget(pose3)
        optionsLayout.addWidget(pose4)
        optionsLayout.addWidget(pose5)

        imageLayout = QVBoxLayout()
        self.imageLabel = QLabel(self)
        self.pixmap = QPixmap('images/home.png')
        self.imageLabel.setPixmap(self.pixmap)
        self.imageLabel.resize(self.pixmap.width(),
                          self.pixmap.height())
        imageLayout.addWidget(self.imageLabel)

        jointsLayout = QVBoxLayout()
        MotorLabel = QLabel("Valores articulares: ")
        MotorLabel.setStyleSheet("font-size:18px; font-weight:bold;")
        joint1Label = QLabel("Joint1")
        joint1Label.setStyleSheet("font-size:16px;")
        joint2Label = QLabel("Joint2")
        joint2Label.setStyleSheet("font-size:16px;")
        joint3Label = QLabel("Joint3")
        joint3Label.setStyleSheet("font-size:16px;")
        joint4Label = QLabel("Joint4")
        joint4Label.setStyleSheet("font-size:16px;")

        jointsLayout.addWidget(MotorLabel)
        jointsLayout.addWidget(joint1Label)
        jointsLayout.addWidget(joint2Label)
        jointsLayout.addWidget(joint3Label)
        jointsLayout.addWidget(joint4Label)
        
        leftLayout.addLayout(jointsLayout)
        leftLayout.addLayout(optionsLayout)
        
        middleLayout.addLayout(leftLayout)
        middleLayout.addLayout(imageLayout)

        outerLayout.addLayout(topLayout)
        outerLayout.addLayout(middleLayout)
        outerLayout.addStretch()


        self.setLayout(outerLayout)

        self.robot = Robot()
        
    # ----------------------------------- Slots ----------------------------------- #
    def slot(self, value):
        radioButton = self.sender()
        if radioButton.isChecked():
            self.pose = radioButton.text()
            self.robot.moveRobot(self.pose)
    
    def getPose(self):
        return self.pose

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

