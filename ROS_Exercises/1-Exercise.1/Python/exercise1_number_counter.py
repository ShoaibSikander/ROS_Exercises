#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64

counter = 0

def callback_number(msg):
    rospy.loginfo("Message received : ")
    rospy.loginfo(msg)
    global counter
    counter += 1
    rospy.loginfo("Counter : ")
    rospy.loginfo(counter)
    msg_new = Int64()
    msg_new.data=counter
    pub.publish(msg_new)

if __name__ == '__main__':
    rospy.init_node('number_counter')
    sub=rospy.Subscriber("/number", Int64, callback_number)
    pub = rospy.Publisher("/number_count", Int64, queue_size=10)
    rospy.spin()
