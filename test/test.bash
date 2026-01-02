#!/bin/bash -xv
# SPDX-FileCopyrightText: 2025 Kaito Shima
# SPDX-License-Identifier: BSD-3-Clause

#!/bin/bash -eu

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws

colcon build

source $dir/.bashrc

timeout 10 ros2 launch era_pkg era.launch.py > /tmp/era.log
cat /tmp/era.log | grep "平成"
