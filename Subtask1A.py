#!/usr/bin/env python3
from ast import Break
from ev3dev2.motor import LargeMotor, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank
import math
import enum


motor_L = LargeMotor(OUTPUT_D)
motor_R = LargeMotor(OUTPUT_C)

wheel_unit = 2 * math.pi * 0.8503935 #circumfence of the wheel. 1 wheel unit is how many inches per rotation

distance = 60
rotations = distance / wheel_unit
drive = MoveTank(OUTPUT_C, OUTPUT_D)


def right_turn():
    drive.on_for_rotations(-60,60, 5)


def left_turn():
    drive.on_for_rotations(60,-60, 5)


def move(rotations, percentSpeed, direction): #     FORWARD = True, BACKWARD = False
    if direction == True:
        drive.on_for_rotations(percentSpeed,percentSpeed, rotations)
    else:
        drive.on_for_rotations(-1 * percentSpeed, -1 * percentSpeed, rotations)


move(1,20,True)
right_turn()
left_turn()


