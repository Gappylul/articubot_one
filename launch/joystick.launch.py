from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    
    joy_node = Node(
        package='joy',
        executable='joy_node',
        parameters=[{
            'autorepeat_rate': 20.0,
        }]
    )

    teleop_node = Node(
        package='teleop_twist_joy',
        executable='teleop_node',
        name='teleop_node',
        parameters=[{
            'axis_linear.x': 1,
            'axis_angular.yaw': 0,
            'enable_button': 5,
            'scale_linear.x': 0.3,
            'scale_angular.yaw': 1.5,
        }]
    )

    return LaunchDescription([
        joy_node,
        teleop_node
    ])