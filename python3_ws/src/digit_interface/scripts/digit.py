#!/home/julio/Escritorio/julio/doctorado/primer_anyo/digit/ros/python3_ws/py3env/bin/python

# first of all, you need to source the virtualenv. Then source the devel setup.bash file.

# ROS IMPORTS
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

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

    # initialize digit sensor with the usb serial
    d = Digit(id)
    d.connect()

    return d


'''
    main function: initialize the ros node and the publisher. Runs an infinite loop
        where reads images from the sensor and publish them in the topic.
    Arguments:
        - None
    Returns: None
'''
def main():

    # initialize digit sensor
    digit_sensor = setup_digit()

    # initialize ros node
    rospy.init_node("digit_ros_node", anonymous=True)
    # create publisher with the topic and the type of the msg
    pub = rospy.Publisher("digit/camera/image_color", Image, queue_size=10)

    # cvbridge to transform the images from np to ros type
    cvbridge = CvBridge()

    # infinite loop
    while True:

        # comment if you want
        rospy.loginfo("Publishing Digit images!")

        # get image from the sensor
        digit_img = digit_sensor.get_frame()

        # transform to ros type and publish img
        pub.publish(cvbridge.cv2_to_imgmsg(digit_img))
        # 100 hz rate of publication
        rospy.Rate(100)



if __name__ == '__main__':
    main()