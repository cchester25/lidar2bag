cmake_minimum_required(VERSION 2.8.3)
project(rospy_rviz)
 
find_package(catkin REQUIRED COMPONENTS
    message_generation
    std_msgs
    )
    
# do not wildcard install files since the root folder of the package will contain a debian folder for releasing
catkin_install_python(PROGRAMS
  script/rospy_rviz.py
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/rospy_rviz
)
install(FILES
  launch/rospy_rviz.launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/rospy_rviz
)
