#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 MisonoToma
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class EraSubscriber(Node):
    def __init__(self):
        super().__init__('era_subscriber')
        self.subscription = self.create_subscription(
            Int32,
            'year',
            self.callback,
            10
        )

    def callback(self, msg):
        year = msg.data

        if 1926 <= year <= 1988:
            era_year = year - 1925
            era = f'昭和{era_year}年'
        elif 1989 <= year <= 2018:
            era_year = year - 1988
            era = f'平成{era_year}年'
        elif 2019 <= year <= 2026:
            era_year = year - 2018
            era = f'令和{era_year}年'
        else:
            era = '対象外'

        self.get_logger().info(f'Received: {year} → {era}')


def main():
    rclpy.init()
    node = EraSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
