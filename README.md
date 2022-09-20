# Digit_ros_interface
In this repository, I included the DIGIT tactile sensors within a ros workspace. 

DIGITs are a type of tactile sensors designed by Meta. This type of sensor is low-cost and returns a colour image instead of a force value. If you want to know more about these sensors, you can check the original paper (https://arxiv.org/pdf/2005.14679) and my last work with them (https://www.researchgate.net/profile/Pablo-Gil-4/publication/354696829_Touch_Detection_with_Low-Cost_Visual-Based_Sensor/links/617d228aa767a03c14d02b5b/Touch-Detection-with-Low-Cost-Visual-Based-Sensor.pdf).

These sensors works with a library in python3, so I wanted to create a ros workspace compiled with python3 to include these sensors with the rest of our mobile manipulator robot.

In this repository you will find two main files/folders. The odt file contains instructions to create the ros workspace and compiled it for python3. The python3_ws folder is the catkin workspace where you will find two main packages: digit_interface and main_code. In digit_interface package I carried out a simple code to read images from the sensors and publish them in a ros topic. The main code package only contains a simple subscriber to evaluate that the digit sensor interface is working. I tested this workspace with ubuntu 20 and ros noetic and it works perfect. As the sensors works with python3, I had to create a virtual environment in order to use ros with python3.

# Commands
# To activate the python3 virtualenv
```sh 
source py3env/bin/activate
```
# ROS commands
###### terminal 1
```sh 
source devel/setup.bash
```
```sh 
roslaunch digit_interface digit.launch
```
###### terminal 2
```sh 
cd src/main_code/scripts/
```
```sh 
python read_from_digit.py
```
# To record a rosbag
```sh 
rosbag record -O name_file /digit/camera/image_color
```
# To play the rosbag in a loop
```sh 
rosbag play -l name_file.bag
```
