 #!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute, TeleportRelative
from std_srvs.srv import Empty
import termios, sys, os
from numpy import pi

TERMIOS = termios

cmd_vel_topic = '/turtle1/cmd_vel'
teleport_ab = '/turtle1/teleport_absolute'
teleport_rel = '/turtle1/teleport_relative'

def getkey():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
    new[6][TERMIOS.VMIN] = 1
    new[6][TERMIOS.VTIME] = 0
    termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
    c = None
    try:
        c = os.read(fd, 1)
    finally:
        termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
    return c

def teleport(key):
    if key == 'abs':
        rospy.wait_for_service(teleport_ab)
        try:
            teleport_absolute = rospy.ServiceProxy(teleport_ab, TeleportAbsolute)
            teleport_abs_result = teleport_absolute(5.544445,5.544445,0)

            rospy.wait_for_service('/clear')
            clearTrajec = rospy.ServiceProxy('/clear', Empty)
            Reset = clearTrajec()
        except rospy.ServiceException as e:
            print(str(e))
    elif key == 'rel':
        rospy.wait_for_service(teleport_rel)
        try:
            teleport_relative = rospy.ServiceProxy(teleport_rel, TeleportRelative)
            teleport__relative_result = teleport_relative(0,pi)
        except rospy.ServiceException as e:
            print(str(e))


def pubVel(linear, angular):
    pub = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)
    message = Twist()
    message.linear.x = linear
    message.angular.z = angular
    pub.publish(message)

def get_action(): 
    key = getkey()
    if key == b'w' or key == b'W':
        pubVel(1,0)
    elif key == b's' or key == b'S':    
        pubVel(-1,0)
    elif key == b'd' or key == b'D':
        pubVel(0,-1)
    elif key == b'a' or key == 'A':
        pubVel(0,1)
    elif key == b'r' or key == 'R':
        teleport('abs')
    elif key == b' ':
        teleport('rel')



if __name__ == '__main__':
    
    welcome = """
    Made by: Valentina Hernandez, Felipe Gutierrez, Manuel Rojas
    --------------------------------------------------------------
    Reading from keyboard
    --------------------------------------------------------------
    Use AWSD to move the turtle
    Use 'R' to clear canvas and teleport the turtle to starting position
    Use Space Bar to rotate the turtle 180°
    Use 'q' to quit
    --------------------------------------------------------------
    """

    try:
        rospy.init_node('my_teleop_key')
        rospy.loginfo(welcome)
        rate = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():
            get_action()
            rate.sleep()

    except rospy.ROSInterruptException:
        pass


    