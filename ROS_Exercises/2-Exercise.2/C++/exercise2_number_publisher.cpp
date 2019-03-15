#include <ros/ros.h>
#include <std_msgs/Int64.h>

int main (int argc, char **argv)
{
	ros::init(argc, argv, "number_publisher", ros::init_options::AnonymousName);
	ros::NodeHandle nh;
	ros::Publisher pub = nh.advertise<std_msgs::Int64>("/number", 10);

	nh.setParam("/number_publish_frequency", 1);
	double publish_frequency;
	nh.getParam("/number_publish_frequency", publish_frequency);
	ros::Rate rate(publish_frequency);

	while (ros::ok()) {
		std_msgs::Int64 msg;
		int iRand = rand() % 10;
		msg.data = iRand;
		pub.publish(msg);
		rate.sleep();
	}
}
