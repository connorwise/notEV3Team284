#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_C, OUTPUT_D, MoveTank
import math


laps = 4                                                                                                        #FIXME INPUT BEFORE DEMO
lengths = .5 * laps

motor_L = LargeMotor(OUTPUT_D)
motor_R = LargeMotor(OUTPUT_C)

wheel_unit = 2 * math.pi * 0.8503935 #circumfence of the wheel. 1 wheel unit is how many inches per rotation

rotations = lengths / wheel_unit
drive = MoveTank(OUTPUT_C, OUTPUT_D)


def right_turn():
    drive.on_for_rotations(-60,60, 5)                                                                           #FIXME make sure you have the angle for rotation stuff


def left_turn():
    drive.on_for_rotations(60,-60, 5)                                                                           #FIXME


def move(rotations, percentSpeed, direction): #     FORWARD = True, BACKWARD = False
    if direction == True:
        drive.on_for_rotations(percentSpeed,percentSpeed, rotations, True) #Brake is on                          TEST WITHOUT BRAKES
    else:
        drive.on_for_rotations(-1 * percentSpeed, -1 * percentSpeed, rotations, True)#Brake is on                ^^^^^^^^^^^^^^^^^^^

for i in range(laps):
    move(rotations, 60, True)
    right_turn()                                                                                                 #FIXME Input the angle
    move(rotations, 60, True)
