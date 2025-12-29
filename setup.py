from setuptools import find_packages, setup

package_name = 'era_converter'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Misono Toma',
    maintainer_email='s24c1115dv@s.chibakoudai.jp',
    description='西暦変換',
    license='TODO: License declaration',

    entry_points={
        'console_scripts': [
            'era_node = era_converter.era_publisher:main',
        ],
    },
)
