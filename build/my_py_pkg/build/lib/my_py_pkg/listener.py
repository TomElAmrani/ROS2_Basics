#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import String
from example_interfaces.srv import SetBool

class Listener(Node):
    
        def __init__(self):
            super().__init__('listener')
            self.subscription = self.create_subscription(String, 'chatter', self.listener_callback, 10)
            self.subscription  # prevent unused variable warning
            self.client=self.create_client(SetBool,'Ten_Msg_Received')
            self.get_logger().info('Listener started')
            self.i=0
    
        def listener_callback(self, msg):
            self.get_logger().info('I heard: "%s"' % msg.data)
            self.i+=1
            if self.i==10:
                self.call_service()

        def call_service(self):
                self.i=0
                request=SetBool.Request()
                request.data=True
                while self.client.wait_for_service(2.0)==False:
                    self.get_logger().warn('service not available, waiting again...')
                future=self.client.call_async(request)
                future.add_done_callback(self.future_call_back)

        def future_call_back(self,future):
            try:
                response=future.result()
            except Exception as e:
                self.get_logger().info('Service call failed %r' % (e,))
            else:
                self.get_logger().info('Service response %r' % (response,))

        
                


def main(args=None):
    rclpy.init(args=args)

    listener = Listener()

    rclpy.spin(listener)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
