#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def cmd_CB(data):
    print(data)
    # rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def sub_cmd():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('sub_cmd_test', anonymous=True)
    rospy.Subscriber("/bebop/cmd_vel", Twist, cmd_CB)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    sub_cmd()