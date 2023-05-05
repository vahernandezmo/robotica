"""
Allows to use the service dynamixel_command 
"""
import rospy
import time
from std_msgs.msg import String
from dynamixel_workbench_msgs.srv import DynamixelCommand

__author__ = "F Gonzalez, S Realpe, JM Fajardo"
__credits__ = ["Felipe Gonzalez", "Sebastian Realpe", "Jose Manuel Fajardo", "Robotis"]
__email__ = "fegonzalezro@unal.edu.co"
__status__ = "Test"

def jointCommand(command, id_num, addr_name, value, time):
    #rospy.init_node('joint_node', anonymous=False)
    rospy.wait_for_service('dynamixel_workbench/dynamixel_command')
    try:        
        dynamixel_command = rospy.ServiceProxy('/dynamixel_workbench/dynamixel_command', DynamixelCommand)
        result = dynamixel_command(command,id_num,addr_name,value)
        rospy.sleep(time)
        return result.comm_result
    except rospy.ServiceException as exc:
        print(str(exc))

def poseRobot(t1,t2,t3,t4,t5=0):
        t1=min([t1,])
        t1=max([t1,])
        t2=min([t2,])
        t2=max([t2,])
        t3=min([t3,])
        t3=max([t3,])
        t4=min([t4,])
        t4=max([t4,])
        
        jointCommand('', 1, 'Goal_Position', 150+t1, 0.5)
        time.sleep(2)
        jointCommand('', 2, 'Goal_Position', 150+t2, 0.5)
        time.sleep(2)
        jointCommand('', 3, 'Goal_Position', 70+t3, 0.5)
        time.sleep(2)
        jointCommand('', 4, 'Goal_Position', 150+t4, 0.5)
        time.sleep(2)
        jointCommand('', 4, 'Goal_Position', 150+t5, 0.5)
        time.sleep(2)
        
if __name__ == '__main__':
    try:
        # Goal_Position (0,1023)
        # Torque_Limit (0,1023)
        # jointCommand('', 1, 'Torque_Limit', 400)
        valor=input(f'''Ingrese la pose a la que desea ir:
        1. Home [0, 0, 0, 0, 0]
        2. P1   [-25, 15, -20, 20, 0]
        3. P2   [ 35,-35, 30, -30, 0]
        4. P3   [-85, 20, -55, 17, 0]
        5. P4   [-80, 35, -55, 45, 0]
        ''')
        match valor:
            case 1:
                poseRobot(0, 0, 0, 0, 0)
            case 2:
                poseRobot(-25, 15, -20, 20, 0)
            case 3:
                poseRobot(35,-35, 30, -30, 0)
            case 4:
                poseRobot(-85, 20, -55, 17, 0)
            case 5:
                poseRobot(-80, 35, -55, 45, 0)
            case _:
                poseRobot(-80, 35, -55, 45, 0)

    except rospy.ROSInterruptException:
        pass
