#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 MisonoToma
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from person_msgs.msg import Person

class EraPublisher(Node):
    def __init__(self):
        super().__init__('era_publisher')
        self.publisher_ = self.create_publisher(Person, 'year', 10)
        self.year = 1926
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = Person()
        msg.name = 'year'
        msg.age = self.year
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
