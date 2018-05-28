from movement import *
from utilities import *
import constants as c
from wallaby import *
import camera as p


colorOrder = []

def init():
    '''For Setup:
    Make sure that both bumpers are touching the back edges of the starting box
    Point the "arm" at the opposite corner of starting box (intersection of black tape)
    Use pencil marks on table to check alignment
    Line up the block of wood with the straight line to perfect the setup'''
    create_disconnect()
    if not create_connect_once():
        print("Create not connected...")
        exit(0)
    print("Create connected...")
    create_full()
    if c.IS_ORANGE_BOT:
        print("I AM ORANGE")
    elif c.IS_BLUE_BOT:
        print("I AM BLUE")
    else:
        print("I AM YELLOW!")
        DEBUG() # Do not remove!!!
    selfTest()
    p.cameraInit()
    print("Press right button to continue")
    wait_for_button()
    #wait_4_light(c.STARTLIGHT)
    shut_down_in(119.0)
    print("Running the robot.")
    c.START_TIME = seconds()

def selfTest():
    #tests all motors and servos
    # raise arm
    print ("Running Self Test")
    testArm()
    resetArm(30, 2000)
    # open/close claw
    enable_servo(c.servoBotGuyClaw)
    moveServo(c.servoBotGuyClaw, c.clawClosed, 15)
    moveServo(c.servoBotGuyClaw, c.clawStart, 15)
    # test drive
    drive_timed(100, 100, 2500)
    msleep(250)
    drive_timed(-100, -100, 2500)
    # lower ramp
    enable_servo(c.servoHayArm)
    moveServo(c.servoHayArm, c.hayArmDown, 10)
    enable_servo(c.servoHayClaw)
    moveServo(c.servoHayClaw, c.hayClawClosed, 10)
    moveServo(c.servoHayClaw, c.hayClawOpen, 10)
    moveServo(c.servoHayArm, c.hayArmUp, 10)
    # lower the arm
    moveArm(c.armStartbox, 30)
    ao()

def getOutOfstartBox ():
    rotate_degrees(-28, 100)
    drive_timed(-100, -100, 3000)
    rotate_degrees(90, 100)
    timedLineFollowRightFront(250, 4.85)


def seeBlocks():
    s = p.checkColor(colorOrder)
    print(get_object_area(c.YELLOW, 0))
    if s == c.RED:
        print("found red")
    elif s == c.YELLOW:
        print("found yellow")
    elif s == c.GREEN:
        print("found green")
    else:
        print("Did not find cube")

def goToSecondBlock():
    timedLineFollowRightFront(200, 3.2)

def getCrates():
    rotate_degrees(-90,200)
    drive_timed(75,75, 2000)
    msleep(1000)
    driveTilBlackLCliffAndSquareUp(-75,-75)
    moveServo(c.servoHayArm, c.hayArmDown, 10)
    moveServo(c.servoHayClaw, c.hayClawOpen, 10)
    msleep(250)
    drive_timed(-100, -100, 400)
    resetArm(30, 2000)
    drive_timed(-65, -75, 1450)
    moveServo(c.servoHayClaw, c.hayClawClosed, 10)
    msleep(500)
    driveTilBlackLCliffAndSquareUp(250,250)
    moveServo(c.servoHayArm, c.hayArmCarry, 10)
    rotate_degrees(180, 100)
    resetArmLowPosition()
    msleep(1000)
    moveArm(c.armBotguyPickUp, 8)
    moveServo(c.servoBotGuyClaw, c.clawBotguy, 10)

def getBotGuy():
    moveArm(c.armBotguyPickUp, 20)
    driveTilBlackLCliffAndSquareUp(250,250)
    moveServo(c.servoBotGuyClaw, c.clawbotguyArea, 10)
    msleep(500)
    drive_timed(100, 100, 500)
    msleep(100)
    drive_timed(100, 100, 1500)
    moveServo(c.servoBotGuyClaw, c.clawClosed, 10)
    driveTilBlackLCliffAndSquareUp(-100, -100)
    drive_timed(-100, -100, 1500)
    msleep(1000)


def gotoSecondBlock():
    moveArm(c.armUpbotguy, 40)
    rotate_degrees(-80, 100)



def seeBlocks2():
    s = p.checkColor(colorOrder)
    print(get_object_area(c.YELLOW, 0))
    if s == c.RED:
        print("found red")
    elif s == c.YELLOW:
        print("found yellow")
        dropBlocksFirst()
    elif s == c.GREEN:
        print("found green")
    else:
        print("Did not find cube")

def goToBlock3():
    timedLineFollowRightFrontBlocks(200, 3)


def seeBlocks3():
    s = p.checkColor(colorOrder)
    print(get_object_area(c.YELLOW, 0))
    if s == c.RED:
        print("found red")
    elif s == c.YELLOW:
        print("found yellow")
    elif s == c.GREEN:
        print("found green")
    else:
        print("Did not find cube")
    p.determineOrder(colorOrder)


def dropBlocksFirst():
    rotate_degrees(70 , 150)
    moveServo(c.servoHayArm, c.hayArmDown, 10)
    moveServo(c.servoHayClaw, c.hayClawOpen, 10)
    drive_timed(-75, -75, 750)


