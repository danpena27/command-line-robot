import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

import robot


class RobotTests(unittest.TestCase):
    def setUp(self):
        robot.speed = 5
        robot.led_status = 'off'
        robot.arm_pos = 'home'

    def run_with_input(self, function, commands):
        output = io.StringIO()
        with patch('builtins.input', side_effect=commands), redirect_stdout(output):
            function()
        return output.getvalue()

    def test_long_menu_session(self):
        output = self.run_with_input(robot.menu, ['bad'] * 1500 + ['5'])
        self.assertEqual(output.count('wrong selection'), 1500)
        self.assertIn('Goodbye!', output)

    def test_drive_speed_limits(self):
        self.run_with_input(robot.drive, ['t'] * 20 + ['m'])
        self.assertEqual(robot.speed, 10)
        self.run_with_input(robot.drive, ['g'] * 20 + ['m'])
        self.assertEqual(robot.speed, 0)

    def test_led_toggle(self):
        self.run_with_input(robot.leds, ['y'])
        self.assertEqual(robot.led_status, 'on')
        self.run_with_input(robot.leds, ['n'])
        self.assertEqual(robot.led_status, 'on')
        self.run_with_input(robot.leds, ['y'])
        self.assertEqual(robot.led_status, 'off')

    def test_servo_positions(self):
        for command, expected in [('l', 'left'), ('r', 'right'), ('h', 'home')]:
            self.run_with_input(robot.servo, [command, 'm'])
            self.assertEqual(robot.arm_pos, expected)

    def test_dance(self):
        with patch.object(robot.time, 'monotonic', side_effect=[0, 0, 1, 2, 3, 4, 5]), \
             patch.object(robot.time, 'sleep'), \
             patch.object(robot.random, 'choice', side_effect=['w', 'a', 'd', 's', 'x']):
            output = self.run_with_input(robot.dance, [])
        for message in ['dance, forward', 'dance, turn left', 'dance, turn right',
                        'dance, backwards', 'dancing stopped', 'dance sequence ended']:
            self.assertIn(message, output)


if __name__ == '__main__':
    unittest.main()
