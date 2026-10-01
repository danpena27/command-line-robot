'''
Author: Daniel Pena Arias
Date: 10/01/2026
Original coursework: 11/02/2025
Program: Robot Control Program
Description: A text-based program to simulate robot movements.
'''
#import modules
import time 
import random 

speed = 5
led_status = 'off' #leds stay off when robot boots up
arm_pos = 'home' #starts with arm at home positonn

#menu that allows the user to enter an action and call a function
def menu():
    while True:
        print('robot main menu')
        print('select 1 to drive robot') 
        print('select 2 to control LEDs') #user selects 2 then led() function is started
        print('select 3 to control servo')#user selects 3 ``then servo() function
        print('select 4 for to see robot dance')#user selects 4 then dance() function
        print('select 5 to Quit robot') #user selects 5 quits robot program
        select = input('make a selection: ')

        if select == '1':
            drive()
        elif select == '2':
            leds()
        elif select == '3':
            servo()
        elif select == '4':
            dance()
        elif select == '5':
            print('Goodbye!')
            return
        else:
            print('wrong selection, try again')
#dive function that allows the user to contorl the robot
def drive():
    global speed 
    print('drive controls')
    print('w/a/d/s/x: forward, turn left,  turn right, back, stop')
    print('t/g: speed up/speed down')
    print('m: return to Main Menu')
    while True:
        select = input('drive: ')
        if select == 'w':
            print('moving forward')
        elif select == 'a':
            print('turning left')
        elif select == 'd':
            print('turning right')
        elif select == 's':
            print('moving backward')
        elif select == 'x':
            print('robot stopped')
        # Speed adjustments
        elif select == 't':
            if speed < 10:
                speed += 1
                print('speed increased.')
            else:
                print('maximum speed reached')
        elif select == 'g':
            if speed > 0:
                speed -= 1
                print('lowering speed')
            else:
                print('robot has stopped')
        elif select == 'm':
            return #returns to menu
        else:
            print('wrong selection, try again')

#led light function that lets the user turn them on or off
def leds():
    global led_status 
    print('led controls')
    if led_status == 'on':
        reply = input('leds are on. turn off? (y/n)')
        if reply == 'y':
            led_status = 'off'
            print('leds off')
        else:
            print('leds stay on.')
    else:
        reply = input('leds are OFF. turn on? (y/n)')
        if reply == 'y':
            led_status = 'on'
            print('leds on')
        else:
            print('leds stay off')

#dance function that allows user to make the robot dance randomly
def dance():
    print('dance sequence starting')
    dance_moves = ['w', 'a', 'd', 's', 'x']
    startTime = time.monotonic()
    
    while time.monotonic() - startTime < 5.0:
        move = random.choice(dance_moves) #Randomly selects moves for it's dance
        if move == 'w':
            print('dance, forward')
        elif move == 'a':
            print('dance, turn left')
        elif move == 'd':
            print('dance, turn right')
        elif move == 's':
            print('dance, backwards')
        elif move == 'x':
            print('dancing stopped')
        time.sleep(0.5)
    print('dance sequence ended')

def servo():
    global arm_pos
    print('servo controls')
    print('select l to move arm to the left')
    print('select r to move arm to the right')
    print('select h to move the servo arm back to home position')
    print('select m to go to the main menu')

    while True:
        select = input('servo positon: ')
        if select == 'l':
            arm_pos = 'left'
            print('servo arm moves left')
        elif select == 'r':
            arm_pos = 'right'
            print('servo arm moves right')
        elif select == 'h':
            arm_pos = 'home'
            print('servo moves home')
        elif select == 'm':
            return #return to main menu
        else:
            print('wrong input, try again')
if __name__ == '__main__':
    menu()
