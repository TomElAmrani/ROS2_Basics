#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import String
from my_robot_interfaces.msg import TargetCoordinates
from my_robot_interfaces.srv import SetLed

class Talker(Node):

    def __init__(self):
        super().__init__("talker")
        self.declare_parameter('param_name_1', 'default_value')
        self.declare_parameter('param_name_2', 'default_value')
        #ros2 run my_pkg my_node --ros-args -p example_param:=example_value
        self.param_name_1=self.get_parameter('param_name_1').value
        self.param_name_2=self.get_parameter('param_name_2').value
        self.publisher_ = self.create_publisher(String, 'chatter' , 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        self.get_logger().info('Talker started')
        self.get_logger().info('Node name is %s' % self.param_name_1)

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)
    talker = Talker()
    rclpy.spin(talker)
    rclpy.shutdown()

if __name__ == '__main__':
    main()