#!/usr/bin/python
import rospy
import math
import numpy as np
from ackermann_msgs.msg import AckermannDriveStamped # steering messages
from bw_week3.msg import speed as SpeedMsg
from sensor_msgs.msg import LaserScan

class SafetyNode:
	def __init__(self):
	    rospy.Subscriber('scan', LaserScan, self.laserCallback)
	    self.pid_pub = rospy.Publisher('/vesc/ackermann_cmd_mux/input/safety', AckermannDriveStamped, queue_size=1)
	    self.speedy = rospy.Subscriber("/speeds", SpeedMsg, self.speedCallback)
	    self.drive_cmd = AckermannDriveStamped()
	    self.lastSpeed = 1
	def speedCallback(self,msg):
	    self.lastSpeed = msg.speed
	def laserCallback(self, msg):
	    front = msg.ranges[480:600]
	    stop =False
	    collisions=0
            for i in range(100):
	    	if front[i] < .4:
		    collisions+=1
    	    	#else:
		 #   collisions =0
            if collisions >6:
		    stop= True
		    #break
	    if stop and self.lastSpeed>0:
		self.drive_cmd.drive.speed=0
		self.drive_cmd.drive.steering_angle=0
		print "stopping"
		self.pid_pub.publish(self.drive_cmd)
if __name__ == "__main__":
    rospy.init_node("Safety")
    Safety = SafetyNode()
    rospy.spin()
