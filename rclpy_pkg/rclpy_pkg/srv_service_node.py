import rclpy
import time

from example_interfaces.srv import AddTwoInts
from rclpy.node import Node


class ServiceNode(Node):

    def __init__(self):
        super().__init__('srv_service_node')
        self.srv = self.create_service(
            AddTwoInts, 'add_two_ints', self.srv_callback)

    def srv_callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(
            'Incoming request\na: %d b: %d' % (request.a, request.b))
        time.sleep(5)
        return response


def main():
    rclpy.init()
    srv_service_node = ServiceNode()
    rclpy.spin(srv_service_node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
