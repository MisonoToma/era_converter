#!/bin/bash
# SPDX-FileCopyrightText: 2025 MisonoToma
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build

source /opt/ros/humble/setup.bash 2>/dev/null || true
source install/setup.bash

timeout 10 ros2 launch era_converter era.launch.py > /tmp/era_converter.log 2>&1

grep '昭和' /tmp/era_converter.log
grep '平成' /tmp/era_converter.log
grep '令和' /tmp/era_converter.log
