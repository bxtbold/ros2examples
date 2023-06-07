import rclpy

from example_interfaces.srv import AddTwoInts
from rclpy.node import Node


class ClientNodeAsync(Node):

    def __init__(self):
        super().__init__('srv_client_node')
        self.client = self.create_client(AddTwoInts, 'add_two_ints')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.send_request(1, 2)

    def send_request(self, a, b):
        request = AddTwoInts.Request()
        request.a = a
        request.b = b
        self.future = self.client.call_async(request)
        self.get_logger().info('request sent! waiting for response...')
        rclpy.spin_until_future_complete(self, self.future)
        self.get_logger().info('Result: %d' % self.future.result().sum)


def main():
    rclpy.init()
    minimal_client = ClientNodeAsync()
    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
