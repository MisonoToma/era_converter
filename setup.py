from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'era_converter'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='MisonoToma',
    maintainer_email='s24c1115dv@s.chibakoudai.jp',
    description='西暦変換',
    license='BSD-3-Clause',
    entry_points={
        'console_scripts': [
            'era_publisher = era_converter.era_publisher:main',
            'era_subscriber = era_converter.era_subscriber:main',
        ],
    },
)
