#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 MisonoToma
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class EraPublisher(Node):
    def __init__(self):
        super().__init__('era_publisher')
        self.publisher_ = self.create_publisher(Int32, 'year', 10)
        self.year = 1926
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = Int32()
        msg.data = self.year
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publish: {self.year}')
        self.year += 1
        if self.year > 2025:
            self.year = 1926

def main(args=None):
    rclpy.init(args=args)
    node = EraPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
