"""
Allows to use the service dynamixel_command
"""
import rospy
import time
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from dynamixel_workbench_msgs.srv import DynamixelCommand
import numpy as np
import math
from spatialmath.base import *

__author__ = "V.Hernández, F.Gutierrez, M.Rojas"
__credits__ = ["Valentina Hernández", "Felipe Gutierrez",
               "Manuel Rojas", "Robotis"]
__email__ = "vahernandezmo@unal.edu.co"
__status__ = "Test"


class Robot():
    def __init__(self):

        self.jointValues = []

    def jointCommand(self, command, id_num, addr_name, value, time):
        # rospy.init_node('joint_node', anonymous=False)
        rospy.wait_for_service('dynamixel_workbench/dynamixel_command')
        try:
            dynamixel_command = rospy.ServiceProxy(
                '/dynamixel_workbench/dynamixel_command', DynamixelCommand)
            result = dynamixel_command(command, id_num, addr_name, value)
            rospy.sleep(time)
            return result.comm_result
        except rospy.ServiceException as exc:
            print(str(exc))

    def ang2bit(self, t):
        return int(round(t*1023/(300), 0))

    def poseRobot(self, t1, t2, t3, t4, t5=0, ts=0.5):
        t1 = self.ang2bit(t1)
        t2 = self.ang2bit(t2)
        t3 = self.ang2bit(t3)
        t4 = self.ang2bit(t4)
        t5 = self.ang2bit(t5)

        self.jointCommand('', 1, 'Goal_Position', 511+t1, 0.5)
        #time.sleep(ts)
        self.jointCommand('', 2, 'Goal_Position', 205+t2, 0.5)
        #time.sleep(ts)
        self.jointCommand('', 3, 'Goal_Position', 511+t3, 0.5)
        #time.sleep(ts)
        self.jointCommand('', 4, 'Goal_Position', 511+t4, 0.5)
        #time.sleep(ts)
        self.jointCommand('', 5, 'Goal_Position', 511+t5, 0.5)
        time.sleep(ts)
        
    def moveRobot(self, valor):
        if valor == "Home":
            self.poseRobot(0, 0, 0, 0, 0)
        elif valor == "Pose 1":
            self.poseRobot(-25, 15, -20, 20, 0)
        elif valor == "Pose 2":
            self.poseRobot(35, -35, 30, -30, 0)
        elif valor == "Pose 3":
            self.poseRobot(-85, 20, -55, 17, 0)
        elif valor == "Pose 4":
            self.poseRobot(-80, 35, -55, 45, 0)
        else:
            self.poseRobot(-80, 35, -55, 45, 0)

    def getJointsValues(self):
        self.listener()
        return self.jointValues

    def callback(self, data):
        self.jointValues = data.position
        # print(data.position)
        self.jointValues = np.round(np.rad2deg(self.jointValues), 2)
        # print(f"[Joints] {self.jointValues}")

    def listener(self):
        rospy.init_node('joint_listener', anonymous=True)
        rospy.Subscriber("/dynamixel_workbench/joint_states",
                         JointState, self.callback)
        rospy.sleep(0.1)

    def InvKine(self, x, y, z):
        L0 = 40.0
        L1 = 105.0
        L2 = 105.0
        L3 = 65.0

        px = x
        py = y
        pz = z

        t1 = math.atan2(py, px)
        c1 = math.cos(t1)
        s1 = math.sin(t1)

        rota = trotx(-math.pi/2) @ trotz(-math.pi/2)
        T_desired = np.array([
            [c1, -s1, 0, 1],
            [s1, c1, 0,  1],
            [0, 0, 1,  1],
            [0, 0, 0, 1]
        ])@rota

        P04 = np.array([px, py, pz])

        P03 = P04-np.array([L3*c1, L3*s1, 0])
        # print(T_desired)
        print(P03, P04)
        cosT3 = (P03[0]**2+P03[1]**2+(P03[2]-L0)**2-L1**2-L2**2)/(2*L1*L2)
        print(P04)
        print(cosT3)
        t3 = math.atan2(-math.sqrt(1-cosT3**2), cosT3)

        s3 = math.sin(t3)
        alpha = math.atan2(P03[2]-L0, math.sqrt(P03[0]**2+P03[1]**2))
        beta = math.atan2(L2*s3, L1+L2*cosT3)
        t2 = alpha-beta
        """
        if t2 < -65*(math.pi)/180:
                #t3 = -t3
                s3=math.sin(t3)
                alpha=math.atan2(P03[2]-L0,math.sqrt(P03[0]**2+P03[1]**2))
                beta=math.atan2(L2*s3,L1+L2*cosT3)
                t2 = alpha-beta
            """

        T01 = trotz(t1)@transl(0.0, 0.0, L0)@trotx(-math.pi/2)
        T12 = trotz(t2)@transl(L1, 0.0, 0.0)
        T23 = trotz(t3)@transl(L2, 0.0, 0.0)
        T03 = T01@T12@T23

        t4 = -t3-t2
        return (math.degrees(t1), math.degrees(t2), math.degrees(t3), math.degrees(t4))

    def leer_parejas_csv(self, nombre_archivo):
        parejas = []
        print(nombre_archivo)
        with open(nombre_archivo, 'r') as archivo_csv:
            contenido = archivo_csv.read().strip().split('\n')
            for linea in contenido:
                y, x, z = linea.split(',')
                pareja = (float(x)*10, float(y)*10, float(z)*10)
                parejas.append(pareja)
        return parejas

    def draw(self, nombre_archivo):
        puntos = self.leer_parejas_csv(nombre_archivo)
        q_articulares = []
        for punto in puntos:
            q = self.InvKine(punto[0], punto[1], punto[2])
            q_articulares.append(q)
        for qi in q_articulares:
            self.poseRobot(qi[0], qi[1], qi[2], qi[3],-105)

    def pickMarker(self, pickup=True):
        if pickup:
            self.poseRobot(0, 70-60, 48-150, 242-150, 100)
            time.sleep(2)
            self.poseRobot(230-150, 75-60, 33-150, 250-150, 100)
            self.poseRobot(230-150, 80-60, 62-150, 225-150, 100)
            self.poseRobot(230-150, 80-60, 62-150, 225-150, -105)
            time.sleep(2)
            self.poseRobot(230-150, 90-60, 80-150, 230-150, -105)
            self.poseRobot(0, 0, 0, 0, -105)
        else:
            self.poseRobot(232-150, 90-60, 80-150, 230-150, -105)
            time.sleep(2)
            self.poseRobot(232-150, 90-60, 50-150, 225-150, -105)
            time.sleep(2)
            self.poseRobot(232-150, 90-60, 50-150, 225-150, 100)
            self.poseRobot(232-150, 75-60, 33-150, 250-150, 100)
            self.poseRobot(0, 0, 0, 0, 0)

    def goHome(self):
        self.poseRobot(0,0,0,0,0)
        time.sleep(0.1)
        self.poseRobot(0, 30, 0, 10, -105)
        time.sleep(1)
        self.poseRobot(0, 0, 0, 0, -105)

    def stop(self):
        raise rospy.ServiceException