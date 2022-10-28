2022-10-21 panfeng 
ros架构下，激光雷达bin文件或者csv文件（有无时间戳均可）转为rosbag格式。

1、bin文件带有时间戳的转换方法-moose2fullbag.py 
2、bin文件以及csv无时间戳的转换方法All2ros_ws//
 -----------------------------运行前的准备-------------------------------------
创建虚拟环境conda create --name yourEnv python=2.7  //
使用前先激活环境 conda activate yourEnv
cd root/All2ros_ws/
安装当前环境依赖文件：pip install -r requirements.txt//之后运行前就不用再安装了

--------------------------------运行-----------------------------------------
1、如果你的激光雷达数据集带有时间戳信息timestamps.txt
       cd root/All2ros_ws/ 
       修改moose2fullbag.py中的路径velo_path 到带有时间戳文件所在，修改velo_data_dir 到存放激光雷达bin文件所在文件夹，修改    bag = rosbag.Bag("filtered.bag", 'w',    compression=compression) 中的"filtered.bag"到想要存储rosbag的地方。
       python moose2fullbag.py
2、如果你的激光雷达数据集没有时间戳信息timestamps.txt
        修改file_path中的路径到你存放激光雷达bin或者csv数据的路径下
        修改filtered_bag_path中的路径到你存放激光雷达bag数据的路径下
        修改file_type 为数据的文件类型 bin或者csv
        cd root/All2ros_ws/ 
        source devel/setup.bash
        roslaunch rospy_rviz rospy_rviz.launch


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
保存git版本v1
2022-10-28
4、添加csv格式转换功能
