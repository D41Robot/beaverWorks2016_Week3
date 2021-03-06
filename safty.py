import rospy
import math
import numpy as np
from ackermann_msgs.msg import AckermannDriveStamped # steering messages
from sensor_msgs.msg import LaserScan

class SafetyNode:
	def __init__:
		rospy.Subscriber('scan', LaserScan, self.laserCallback)
		self.stop = rospy.Publisher('/vesc/ackermann_cmd_mux/input/safety', AckermannDriveStamped, queue_size=1)

	def laserCallback(self, msg):
		
		if min(msg.ranges)<.4:
			drive_cmd = AckermannDriveStamped()
			drive_cmd.drive.speed=-.1
			drive_cmd.drive.steering_angle=0
			print('Stopping car')
			self.stop.publish(drive_cmd)
