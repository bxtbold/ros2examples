from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription(
    [
        Node(
            package='rclpy_pkg',
            namespace='',
            executable='pub_sub_node',
        )
    ])
