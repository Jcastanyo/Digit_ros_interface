#!/home/julio/Escritorio/julio/doctorado/primer_anyo/digit/ros/python3_ws/py3env/bin/python

# first of all, you need to source the virtualenv. Then source the devel setup.bash file.

# ROS IMPORTS
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import time
import cv2

# DIGIT LIBRARY
from digit_interface import Digit

'''
    setup_digit function: reads the sensor id from the launch file and initializes the sensor.
    Arguments:
        - None
    Returns: object class of the sensor library.
'''
def setup_digit():

    # get sensor id from launch file
    id = rospy.get_param("/sensor_id")
    id55, id45 = id.split("_")[0], id.split("_")[1]

    # initialize digit sensor with the usb serial
    d55 = Digit(id55)
    d45 = Digit(id45)
    d55.connect()
    d45.connect()

    return d55, d45, id55, id45


'''
    main function: initialize the ros node and the publisher. Runs an infinite loop
        where reads images from the sensor and publish them in the topic.
    Arguments:
        - None
    Returns: None
'''
def main():

    # initialize digit sensor
    d55, d45, id55, id45 = setup_digit()

    # initialize ros node
    rospy.init_node(f"digit_ros_node", anonymous=True)
    # create publisher with the topic and the type of the msg
    pub55 = rospy.Publisher(f"digit55/camera/image_color", Image, queue_size=10)
    pub45 = rospy.Publisher(f"digit45/camera/image_color", Image, queue_size=10)

    # cvbridge to transform the images from np to ros type
    cvbridge = CvBridge()

    # infinite loop
    while True:

        # comment if you want
        rospy.loginfo("Publishing Digit images!")

        # get image from the sensor
        digit55_img = d55.get_frame()
        digit45_img = d45.get_frame()

        cv2.imshow("digit55", digit55_img)
        cv2.imshow("digit45", digit45_img)
        cv2.waitKey(1)

        # create the ros msg for the images and fill with all the info
        image_msg55 = Image()
        image_msg55.header.stamp = rospy.Time.from_sec(time.time())
        image_msg55.header.frame_id = "digit_camera"
        image_msg55.height = (digit55_img.shape)[0]
        image_msg55.width = (digit55_img.shape)[1]
        image_msg55.step = digit55_img.strides[0]
        image_msg55.data = digit55_img.flatten().tolist()
        image_msg55.encoding = "bgr8"

        
        image_msg45 = Image()
        image_msg45.header.stamp = rospy.Time.from_sec(time.time())
        image_msg45.header.frame_id = "digit_camera"
        image_msg45.height = (digit45_img.shape)[0]
        image_msg45.width = (digit45_img.shape)[1]
        image_msg45.step = digit45_img.strides[0]
        image_msg45.data = digit45_img.flatten().tolist()
        image_msg45.encoding = "bgr8"

        # transform to ros type and publish img
        #pub.publish(cvbridge.cv2_to_imgmsg(digit_img))
        pub55.publish(image_msg55)
        pub45.publish(image_msg45)
        # 100 hz rate of publication
        rospy.Rate(100)



if __name__ == '__main__':
    main()
