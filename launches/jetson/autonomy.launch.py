import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import PathJoinSubstitution, LaunchConfiguration, TextSubstitution
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node
from launch.conditions import LaunchConfigurationEquals

def generate_launch_description():
    launch_description = LaunchDescription()

    # Camera manager
    camera_manager_launch = \
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                PathJoinSubstitution([FindPackageShare('camera_manager'), 'launch', 'cm_autonomy.launch.py'])
            )
        )

    # Aruco Detect
    aruco_detect = \
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                'launches/components/daedalus_aruco.launch.py'
            )
        )

    # Object Detection
    object_distance = \
        Node(
            namespace='jetson',
            package='object_detect',
            executable='object_distance',
            name='object_distance_jetson'
        )

   

    launch_description.add_action(camera_manager_launch)
    launch_description.add_action(aruco_detect)
    launch_description.add_action(object_distance)
    
    return launch_description
