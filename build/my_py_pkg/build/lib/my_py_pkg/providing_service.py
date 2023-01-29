#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import String
from example_interfaces.srv import SetBool

class ProvidingServiceNode(Node):

    def __init__(self):
        super().__init__('providing_service')
        self.service=self.create_service(SetBool,'Ten_Msg_Received',self.service_callback)
        self.get_logger().info('Providing service started')
        self.i=0

    def service_callback(self,request,response):
        self.get_logger().info('Service called')
        self.i+=1
        if request.data==True:
            response.success=True
            response.message='You have received  ' + str(self.i*10)+ '  messages'
        else:
            response.success=False
            response.message='Service not working'
        return response


def main(args=None):
    rclpy.init(args=args)

    providing_service = ProvidingServiceNode()

    rclpy.spin(providing_service)

    rclpy.shutdown()



if __name__ == '__main__':
    main()