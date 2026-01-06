#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 MisonoToma
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node

from person_msgs.msg import Person

class EraSubscriber(Node):
    def __init__(self):
        super().__init__('era_subscriber')
        self.subscription = self.create_subscription(
            Person,
            'year',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        year = msg.year
        era = ""

        if 1926 <= year <= 1988:
            era = f"昭和{year-1925}年"
        elif 1989 <= year <= 2018:
            era = f"平成{year-1988}年"
        elif 2019 <= year <= 2025:
            era = f"令和{year-2018}年"
        else:
            era = "対象外"

        self.get_logger().info(f"Received: {year} → {era}")

def main(args=None):
    rclpy.init(args=args)
    node = EraSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
