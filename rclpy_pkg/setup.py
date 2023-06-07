import os
from glob import glob
from setuptools import setup

package_name = 'rclpy_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # include all launch files
        (os.path.join('share', package_name, 'launch'),
            glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Batbold N.',
    author_email='bxtbold@protonmail.com',
    description='The package for rclpy examples',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'executor_node = rclpy_pkg.executor_node:main',
            'pub_sub_node = rclpy_pkg.pub_sub_node:main',
            'qos_sub_node = rclpy_pkg.qos_sub_node:main',
            'srv_client_node = rclpy_pkg.srv_client_node:main',
            'srv_service_node = rclpy_pkg.srv_service_node:main',
        ],
    },
)
