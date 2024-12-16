#!/usr/bin/env python

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

def publish_image():
    # Initialize the node
    rospy.init_node('webcam_publisher', anonymous=True)
    # Create a publisher
    pub = rospy.Publisher('/webcam/image_raw', Image, queue_size=10)
    # Set the publishing rate
    rate = rospy.Rate(30)  # 30Hz
    # Create a CvBridge
    bridge = CvBridge()
    # Initialize video capture
    cap = cv2.VideoCapture(0)  # 0 for default webcam

    while not rospy.is_shutdown():
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            rospy.logerr("Could not grab frame")
            continue
        # Display the frame
        cv2.imshow('Webcam', frame)
        cv2.waitKey(1)
        # Convert the image to a ROS message
        try:
            ros_image = bridge.cv2_to_imgmsg(frame, "bgr8")
        except CvBridgeError as e:
            rospy.logerr(e)
            continue
        # Publish the image
        pub.publish(ros_image)
        # Sleep to maintain the publishing rate
        rate.sleep()

    # When done, release the capture
    cap.release()
    # Destroy OpenCV windows
    cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        publish_image()
    except rospy.ROSInterruptException:
        pass
