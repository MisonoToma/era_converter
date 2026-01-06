#!/bin/bash
# SPDX-FileCopyrightText: 2025 MisonoToma
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source /opt/ros/humble/setup.bash
source install/setup.bash
timeout 10 ros2 launch era_converter era.launch.py > /tmp/era_converter.log

cat /tmp/era_converter.log |
grep 'publish'
