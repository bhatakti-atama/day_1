#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import random

def main():
    rospy.init_node('node_turtle_trace', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)

    
    while not rospy.is_shutdown():
        var=random.randint(-3,3)
        scale=random.randint(1,3)
        vel_msg = Twist()
        vel_msg.angular.z = var/3*scale
        vel_msg.linear.x = 2

        velocity_publisher.publish(vel_msg)
        rate.sleep()
           

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
