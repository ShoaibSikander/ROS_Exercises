#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64
from random import randint

if __name__ == '__main__':
	rospy.init_node("number_publisher")
	pub = rospy.Publisher("/number", Int64, queue_size=20)

	rospy.set_param("/number_publish_frequency", 1)
	publish_frequency = rospy.get_param("/number_publish_frequency")
	rate = rospy.Rate(publish_frequency)
	
	while not rospy.is_shutdown():
		msg = Int64()
		rand = randint(0, 9)
		msg.data = rand
		pub.publish(msg)
		rate.sleep()
	rospy.loginfo("Node was stopped!!!")
