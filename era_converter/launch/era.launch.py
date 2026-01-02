#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 MisonoToma
# SPDX-License-Identifier: BSD-3-Clause
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='era_converter',
            executable='era_publisher',
            name='era_publisher'
        ),
        Node(
            package='era_converter',
            executable='era_subscriber',
            name='era_subscriber'
        )
    ])
