import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class PubSubNode(Node):

    def __init__(self):
        super().__init__('pub_sub_node')
        self.pub = self.create_publisher(String, 'pub_topic', 1)
        self.sub = self.create_subscription(String, 'sub_topic', self.callback, 1)
        self.get_logger().info('pub_sub_node has been started')

    def callback(self, msg):
        self.get_logger().info('received "%s"' % msg.data)
        # publish a message every time a message is received
        msg = String()
        msg.data = 'Hello World!'
        self.pub.publish(msg)


def main():
    rclpy.init()
    pub_sub_node = PubSubNode()
    rclpy.spin(pub_sub_node)
    pub_sub_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
