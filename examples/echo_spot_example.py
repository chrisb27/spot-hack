import argparse
import sys

import bosdyn
import bosdyn.client
import bosdyn.client.util

from common.spot_connection import get_connected_robot
from common.spot_functions.echo_spot_function import EchoSpotFunction
from common.spot_functions.spot_function_execution import execute_function_for_robot


def main(argv):
    parser = argparse.ArgumentParser()
    bosdyn.client.util.add_base_arguments(parser)
    parser.add_argument(
        '-s', '--string', default='Hello, Spot!', nargs=1, help=
        'Pass a string to be echoed by Spot.'
    )
    options = parser.parse_args(argv)
    try:
        username = "example_username"
        password = "example_password"
        robot = get_connected_robot('HelloSpotClient', username, password)
        echo_spot_function = EchoSpotFunction()
        execute_function_for_robot(robot, echo_spot_function, options)
        return True
    except Exception as exc:  # pylint: disable=broad-except
        logger = bosdyn.client.util.get_logger()
        logger.error("Echoing through Spot threw an exception: %r", exc)
        return False


if __name__ == '__main__':
    if not main(sys.argv[1:]):
        sys.exit(1)
