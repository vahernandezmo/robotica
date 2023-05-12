"""
Allows to use the service dynamixel_command
"""
import rospy
import time
from std_msgs.msg import String
from dynamixel_workbench_msgs.srv import DynamixelCommand

__author__ = "V.Hernández, F.Gutierrez, M.Rojas"
__credits__ = ["Valentina Hernández", "Felipe Gutierrez",
    "Manuel Rojas", "Robotis"]
__email__ = "vahernandezmo@unal.edu.co"
__status__ = "Test"


class Robot():
    
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
            


    def ang2bit(self,t):
        return int(round(t*1023/(300), 0))


    def poseRobot(self, t1, t2, t3, t4, t5=0, ts = 0.5):
        t1 = self.ang2bit(t1)
        t2 = self.ang2bit(t2)
        t3 = self.ang2bit(t3)
        t4 = self.ang2bit(t4)
        t5 = self.ang2bit(t5)

        self.jointCommand('', 1, 'Goal_Position', 511+t1, 0.5)
        time.sleep(ts)
        self.jointCommand('', 2, 'Goal_Position', 511+t2, 0.5)
        time.sleep(ts)
        self.jointCommand('', 3, 'Goal_Position', 239+t3, 0.5)
        time.sleep(ts)
        self.jointCommand('', 4, 'Goal_Position', 511+t4, 0.5)
        time.sleep(ts)
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
