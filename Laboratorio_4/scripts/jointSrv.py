"""
Allows to use the service dynamixel_command
"""
import rospy
import time
from std_msgs.msg import String
from dynamixel_workbench_msgs.srv import DynamixelCommand

__author__ = "F Gonzalez, S Realpe, JM Fajardo"
__credits__ = ["Felipe Gonzalez", "Sebastian Realpe",
    "Jose Manuel Fajardo", "Robotis"]
__email__ = "fegonzalezro@unal.edu.co"
__status__ = "Test"


def jointCommand(command, id_num, addr_name, value, time):
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
        


def ang2bit(t):
    return int(round(t*1023/(300), 0))


def poseRobot(t1, t2, t3, t4, t5=0, ts = 0.5):
    t1 = ang2bit(t1)
    t2 = ang2bit(t2)
    t3 = ang2bit(t3)
    t4 = ang2bit(t4)
    t5 = ang2bit(t5)

    jointCommand('', 1, 'Goal_Position', 511+t1, 0.5)
    time.sleep(ts)
    jointCommand('', 2, 'Goal_Position', 511+t2, 0.5)
    time.sleep(ts)
    jointCommand('', 3, 'Goal_Position', 239+t3, 0.5)
    time.sleep(ts)
    jointCommand('', 4, 'Goal_Position', 511+t4, 0.5)
    time.sleep(ts)
    jointCommand('', 5, 'Goal_Position', 511+t5, 0.5)
    time.sleep(ts)


if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            # Goal_Position (0,1023)
            # Torque_Limit (0,1023)
            # jointCommand('', 1, 'Torque_Limit', 400)
            valor = int(input(f'''Ingrese la pose a la que desea ir:
            1. Home [0, 0, 0, 0, 0]
            2. P1   [-25, 15, -20, 20, 0]
            3. P2   [ 35,-35, 30, -30, 0]
            4. P3   [-85, 20, -55, 17, 0]
            5. P4   [-80, 35, -55, 45, 0]
            '''))

            if valor == 1:
                poseRobot(0, 0, 0, 0, 0)
            elif valor == 2:
                poseRobot(-25, 15, -20, 20, 0)
            elif valor == 3:
                poseRobot(35, -35, 30, -30, 0)
            elif valor == 4:
                poseRobot(-85, 20, -55, 17, 0)
            elif valor == 5:
                poseRobot(-80, 35, -55, 45, 0)
            else:
                poseRobot(-80, 35, -55, 45, 0)

    except rospy.ROSInterruptException:
        pass
