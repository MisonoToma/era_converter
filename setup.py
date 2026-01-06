from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'era_converter'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        # ament 用
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        # package.xml
        ('share/' + package_name, ['package.xml']),
        # ★★★ これが重要 ★★★
        (os.path.join('share', package_name, 'launch'),
            glob('era_converter/launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='MisonoToma',
    maintainer_email='s24c1115dv@s.chibakoudai.jp',
    description='西暦を和暦（昭和・平成・令和）に変換するROS2ノード',
    license='BSD-3-Clause',
    entry_points={
        'console_scripts': [
            'era_publisher = era_converter.era_publisher:main',
            'era_subscriber = era_converter.era_subscriber:main',
        ],
    },
)
