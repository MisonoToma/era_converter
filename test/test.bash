#!/bin/bash -xv
# SPDX-FileCopyrightText: 2025 MisonoToma
# SPDX-License-Identifier: BSD-3-Clause

#!/bin/bash -eu

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
cd "$SCRIPT_DIR/../.."

source /opt/ros/humble/setup.bash

colcon build
source install/setup.bash

timeout 10 ros2 launch era_converter era.launch.py > /tmp/era.log

cat /tmp/era.log | grep "平成"
