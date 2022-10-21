#!/usr/bin/env python2
# coding=utf-8
 
import os
import numpy as np
import rospy
import rosbag
from sensor_msgs.msg import CameraInfo, Imu, PointField, NavSatFix
from visualization_msgs.msg import *
from sensor_msgs.msg import PointCloud2
from sensor_msgs import point_cloud2 as pc2
import pcl.pcl_visualization
 
 
def get_data():
    file_name = list()
 
    file_path = rospy.get_param('file_path', "")  # 获取一个全局参数
    velo_filenames = sorted(os.listdir(file_path))  # get all of them
    for filename in velo_filenames:
        filename = os.path.join(file_path, filename)
        if filename.split('.')[-1] == "bin":
            # print(filename.split('/')[-1])
            file_name.append(filename.split('/')[-1])
    # print(file_name)
    return file_name
 
 
def main():

    rospy.init_node("point_cloud", anonymous=True)
 
    rate = rospy.Rate(10)
 
    pub_cloud = rospy.Publisher("/point_cloud", PointCloud2, queue_size=100)
 
    point_cloud2 = PointCloud2()
    point_cloud2.header.frame_id = "/velodyne"
 
    file_path = rospy.get_param('file_path', "")  # 获取一个全局参数
    filtered_bag_path = rospy.get_param('filtered_bag_path')
    file_name = get_data()
    compression = rosbag.Compression.NONE

    bag = rosbag.Bag(filtered_bag_path, 'w',    compression=compression)
    # while True:
    for file in file_name:
        point_data = np.fromfile((file_path + file), dtype=np.float32, count=-1).reshape([-1, 4])
        # point_data = point_data[:10]
        fields = [PointField('x', 0, PointField.FLOAT32, 1),
            PointField('y', 4, PointField.FLOAT32, 1),
            PointField('z', 8, PointField.FLOAT32, 1),
            PointField('intensity', 12, PointField.FLOAT32, 1)]
        cloud = pc2.create_cloud(point_cloud2.header, fields, point_data)
        # cloud = pc2.create_cloud_xyz32(point_cloud2.header, point_data[:, :3])
        bag.write("/point_cloud",cloud,rospy.get_rostime())

        pub_cloud.publish(cloud)

        # 控制发布频率
        rate.sleep()
    print(bag)
    bag.close()

if __name__ == "__main__":    
    main()    
