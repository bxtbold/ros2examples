import rclpy
import sys
import time

from rclpy.node import Node
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import SingleThreadedExecutor, MultiThreadedExecutor
from std_msgs.msg import String


class ExecutorNode(Node):

    def __init__(self):
        super().__init__('exec_node')
        callback_group = ReentrantCallbackGroup()
        self.create_subscription(
            String, 'topic1', self.callback1, 1, callback_group=callback_group)
        self.create_subscription(
            String, 'topic2', self.callback2, 1, callback_group=callback_group)
        self.get_logger().info('exec_node has been started')

    def callback1(self, msg):
        self.get_logger().info('callback1 called')
        for i in range(5):
            self.get_logger().info('callback1 sleeping...')
            time.sleep(1)
        self.get_logger().info('callback1 done.')

    def callback2(self, msg):
        self.get_logger().info('callback2 called')


def main():
    # get the executor type from command line
    executor = sys.argv[-1]

    rclpy.init()
    exec_node = ExecutorNode()
    if executor == 'multi':
        exec_node.get_logger().info('multi threaded executor')
        multi_threaded_exec = MultiThreadedExecutor()
        multi_threaded_exec.add_node(exec_node)
        multi_threaded_exec.spin()
        multi_threaded_exec.shutdown()
    else:
        exec_node.get_logger().info('single threaded executor')
        rclpy.spin(exec_node)
        exec_node.destroy_node()
        rclpy.shutdown()
        ## This is equivalent to the following:
        # single_threaded_exec = SingleThreadedExecutor()
        # single_threaded_exec.add_node(exec_node)
        # single_threaded_exec.spin()
        # single_threaded_exec.shutdown()


if __name__ == '__main__':
    main()
