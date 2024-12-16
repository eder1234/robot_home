cmake_minimum_required(VERSION 3.0.2)
project(robot_home)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  cv_bridge
  sensor_msgs
)

catkin_package(

)

include_directories(

)

catkin_install_python(PROGRAMS
  scripts/webcam_publisher.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
