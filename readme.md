2022-10-21 panfeng 哈尔滨工程大学
1、带有时间戳的转换方法-moose2fullbag.py 
2、无时间戳的转换方法Bin2ros_ws//

使用前先激活环境 conda activate bin2bag





modify log:
2022-10-21:
1、原代码非顺序读取，改进为按bin文件编号顺序读取
velo_filenames = sorted(os.listdir(file_path))  # get all of them
2、原代码为发布点云格式，改进为保存为rosbag
import rosbag
compression = rosbag.Compression.NONE
bag = rosbag.Bag(filtered_bag_path, 'w',    compression=compression)
bag.write("/point_cloud",cloud,rospy.get_rostime())
print(bag)
bag.close()
3、原代码为xyz格式，改进为xyzI增加强度信息
fields = [PointField('x', 0, PointField.FLOAT32, 1),
    PointField('y', 4, PointField.FLOAT32, 1),
    PointField('z', 8, PointField.FLOAT32, 1),
    PointField('intensity', 12, PointField.FLOAT32, 1)]
cloud = pc2.create_cloud(point_cloud2.header, fields, point_data)
保存git版本
