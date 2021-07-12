## Hawkbot机器人开发环境搭建

*Hawkbot的虚拟机开发环境搭建及操作方法在商家提供的“ROS智能机器人使用手册”中已有介绍，所以在这里主要介绍如何在Linux物理机上配置Hawkbot开发环境。*



以下教程适用于已安装好Ubuntu18.04和ROS Melodic的电脑：

- MacOS的Ubuntu安装可以参考https://www.hellotech.com/guide/for/how-to-install-linux-on-mac （注：可以登陆Ubuntu官网https://ubuntu.com/download/alternative-downloads 下载镜像，注意要选择18.04版本，在“Past releases and other flavours”中）
- ROS的安装可参考http://wiki.ros.org/melodic/Installation/Ubuntu



#### 1. 下载Hawkbot Package

- 首先需要创建工作空间catkin_ws和src文件夹，新建一个terminal并依次输入下列代码：

  ```shell
  mkdir -p catkin_ws/src          #创建catkin工作空间
  cd catkin_ws/src                #进入catkin_ws下的src目录
  ```

- 可以通过链接https://github.com/SLiu2000/Hawkbot-Setup 下载hawkbot文件夹至linux电脑端，或者可以通过百度网盘（链接: https://pan.baidu.com/s/1BYN4PW4TZ-J_O2tw77INlw  密码: 31nk）进行下载。下载完成后将hawkbot package添加进src文件夹中。

- 下载完成后cd至catkin_ws下，在terminal中输入`catkin_make`进行编译

#### 2. 进行主从配置

- 在terminal中输入

  ```shell
  gedit ~/.bashrc
  ```

  会打开一个文本编辑界面，在现有文本的末尾添加以下内容：

  ```shell
  export ROS_PARALLEL_JOBS=-j2
  source /opt/ros/melodic/setup.bash
  source ~/catkin_ws/devel/setup.bash
  
  export ROBOT_IP=10.42.0.1
  export ROS_MASTER_URI=http://$ROBOT_IP:11311
  
  export IPAddress=` ifconfig -a|grep inet|grep
  -v 127.0.0.1|grep -v inet6|awk '{print $2}'|tr -d "addr:"`
  export ROS_IP=$IPAddress
  
  echo -e "Ubuntu IP : \033[32m$ROS_IP"
  alias sshrobot='ssh pi@$ROBOT_IP'
  ```

- 保存后关闭文本编辑器，在terminal中输入下列代码更新环境：

  ```shell
  source ~/.bashrc
  ```

#### 3. 测试机器人运行情况

- 在完成上述步骤后Hawkbot的开发环境就算搭建完成了，我们可以通过teleop程序测试机器人是否可以正常使用
- 在打开机器人开关后我们需要先连接hawkbot热点：
  - WiFi 名称:HawkBot
  - WiFi 密码:hawkbot123
- 连接完成后在terminal中输入`source ~/.bashrc`，检查新显示的IP地址是否正确（10.42.0.xxx）
- 输入`roslaunch hawkbot teleop_key.launch`，如果可以正常运行并控制机器人的移动即配置且连接正常

