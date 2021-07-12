#!/usr/bin/env python
import rospy
from dynamic_reconfigure.server import Server
from hawkbot.cfg import hawkbotConfig


def callback(config, level):
    rospy.logdebug(config)
    return config

if __name__ == "__main__":
    rospy.init_node("hawkbot_param_server", anonymous = True)
    srv = Server(hawkbotConfig, callback)
    rospy.spin()
