from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld=LaunchDescription()

    # Start the robot_state_publisher node
    talker_1 = Node(
        package='my_py_pkg',
        executable='talker',
        name='talker_1',
        remappings=[
            ('chatter', 'messanger')
        ],
        parameters=[
            {'param_name_1': 'koko'},
            {'param_name_2': 'lolo'}
        ]
    )

    listener_1=Node(
        package='my_py_pkg',
        executable='listener',
        name='listener_1',
        remappings=[
            ('chatter','messanger')
        ]
    )

    server_=Node(
        package='my_py_pkg',
        executable='providing_service',
        name='providing_service'
    )

    ld.add_action(talker_1)
    ld.add_action(listener_1)
    ld.add_action(server_)
    return ld