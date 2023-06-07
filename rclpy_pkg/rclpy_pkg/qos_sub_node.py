import rclpy

from rclpy.node import Node
from rclpy.qos import *
from std_msgs.msg import String


class QoSPubSubNode(Node):

    def __init__(self):
        super().__init__('qos_sub_node')
        qos_profile = QoSProfile(
            depth=1,
            history=QoSHistoryPolicy.KEEP_LAST,
            reliability=QoSReliabilityPolicy.RELIABLE,
        )
        self.sub = self.create_subscription(
            String, 'qos_sub_topic', self.callback, qos_profile)
        self.get_logger().info('qos_sub_node has been started')

    def callback(self, msg):
        self.get_logger().info('received "%s"' % msg.data)


def main():
    rclpy.init()
    qos_sub_node = QoSPubSubNode()
    rclpy.spin(qos_sub_node)
    qos_sub_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
