from movement import *
from utilities import *
import constants as c
from wallaby import *
import camera as p
import createPlusPlus as cpp
import motorz as m

colorOrder = []

cpp = None

def init(icpp):
    '''For Setup:
    Make sure that both bumpers are touching the back edges of the starting box
    Point the "arm" at the opposite corner of starting box (intersection of black tape)
    Use pencil marks on table to check alignment
    Line up the block of wood with the straight line to perfect the setup'''
    # create_disconnect()
    # if not create_connect_once():
    #     print("Create not connected...")
    #     exit(0)
    # print("Create connected...")
    # create_full()
    global cpp
    cpp = icpp
    init_movement(cpp)
    if c.IS_ORANGE_BOT:
        print("I AM ORANGE")
    elif c.IS_BLUE_BOT:
        print("I AM BLUE")
    elif c.IS_GREEN_BOT:
        print("I AM GREEN!")
    else:
        print("I AM YELLOW")
        DEBUG() # Do not remove!!!
    selfTest()  #tests each function of the robot
    # p.cameraInit()
    print("Press a button to continue")
    wait_for_button()
    #wait_4_light(c.STARTLIGHT)
    # shut_down_in(119.0)
    c.START_TIME = seconds()

def selfTest(): #separated from init for the sake of legibility
    print ("Running Self Test")
    enable_servo(c.servoBotGuyArm)
    moveServo(c.servoBotGuyArm, c.botGuyArmDown, 15)
    msleep(500)
    moveServo(c.servoBotGuyArm, c.botGuyArmUp, 15)
    # open/close claw
    m.rotate_until_stalled(20)
    msleep(1000)
    m.rotate_until_stalled(-20)
    msleep(300)
    m.set_claw_open()
    # test drive
    cpp.drive_timed(20, 20, 2500)
    msleep(250)
    cpp.drive_timed(-20, -20, 2500)
    # lower ramp
    enable_servo(c.servoCrateArm)
    moveServo(c.servoCrateArm, c.crateArmDown, 10)
    enable_servo(c.servoCrateClaw)
    moveServo(c.servoCrateClaw, c.crateClawClosed, 10)
    moveServo(c.servoCrateClaw, c.crateClawStart, 10)
    moveServo(c.servoCrateArm, c.crateArmStart, 10)
    moveServo(c.servoBotGuyArm, c.botGuyArmStart, 15)
    # moveServo(c.servoBotGuyClaw, c.clawClosed, 15)
    ao()


def centerPipeRunAndBotGuyGrab():
    print ("Heading to Botguy")
    moveServo(c.servoBotGuyArm, c.botGuyArmDown)
    m.rotate_until_stalled(20)
    moveServo(c.servoBotGuyArm, c.botGuyArmStart, 15)
    cpp.rotate(25, 50)
    cpp.drive_distance(-44, 50)
    cpp.drive_distance(2,50)
    cpp.rotate(83, 50)
    cpp.drive_distance(-5,25)
    moveServo(c.servoBotGuyArm, c.botGuyArmUp, 30)
    m.claw_to_position(c.clawBotguy, 30)
    moveServo(c.servoBotGuyArm, c.botGuyArmDown, 15)
    wait_for_button()
    cpp.drive_distance(-9, 30)
    wait_for_button()
    m.claw_move(20)
    msleep(4000)
    moveServo(c.servoBotGuyArm, c.botGuyArmMid, 5)


def headToSecondBlock():
    print ("Heading to second block!")
    cpp.drive_distance(6,25)
    moveServo(c.servoBotGuyArm, c.botGuyArmStart, 5)
    cpp.rotate(90,50)
    driveTilBlackLRCliffAndSquareUp(50,50)
    cpp.rotate(55,50)
    lineFollowRightFrontTilRightBlack()
    cpp.drive_distance(3.5, 40)


def seeBlocksWithoutOrange():
    #allows robot to check color of first cube from the startbox
    s = p.checkColorWithoutOrange(colorOrder)
    print(get_object_area(c.YELLOW, 0))
    if s == c.RED:
        print("found red")
    elif s == c.YELLOW:
        print("found yellow")
    elif s == c.GREEN:
        print("found green")
    else:
        print("Did not find cube (Without Orange)")

def seeBlocks():
    #allows robot to determine color of second cube and then determine color of third cube
    s = p.checkColor(colorOrder)
    if s == c.RED:
        print("found red")
    elif s == c.YELLOW:
        print("found yellow")
    elif s == c.GREEN:
        print("found green")
    else:
        print("Did not find cube")
    p.determineOrder(colorOrder)

def getCrates(): #break this function into smaller bites... make driveToCrates, getCrates, turnAround,etc
    print "Picking up crates"
    #drives center area grabs cube and turns around to prep for botguy grab
    cpp.rotate(-90, 20)  #-90
    # drive_timed(75, 75, 1000)
    msleep(1000)
    driveTilBlackLCliffAndSquareUp(-15,-15) #end of func. 1
    # rotate_degrees(1, 50)
    moveServo(c.servoCrateArm, c.crateArmDown, 15)
    moveServo(c.servoCrateClaw, c.crateGrab, 15)
    wait_for_button()
    cpp.drive_distance(5, 40)
    # rotate(2,50)
    # msleep(500)
    # drive_timed(-100, -80, 1600)
    # drive_timed(-100, -100, 500) #400
    # drive_timed(-100, -85, 1100)
    moveServo(c.servoCrateClaw, c.crateClawClosed, 15)  # grab crates # end of func.2
    moveServo(c.servoCrateArm, c.crateArmMid, 10)
    msleep(500)
    cpp.drive_distance(8, 40)
    moveServo(c.servoCrateArm, c.crateArmMid+200, 2)
    rotate_degrees(155, 50)  #145
    msleep(1000)
    moveServo(c.servoBotGuyClaw, c.clawBotguy, 15)


def driveToYellow(): # Starts from the middle or it won't work and that's not our fault!
    print "Driving to yellow"
    if colorOrder[0] == c.YELLOW:
        goYellowFirst()
    elif colorOrder[1] == c.YELLOW:
        goYellowSecond()
    elif colorOrder[2] == c.YELLOW:
        goYellowThird()


def goYellowFirst():
    print "Yellow is in first position"
    #delivers crates when yellow block is in first zone
    rotate_degrees(90, 100)
    lineFollowLeftFrontTilRightFrontBlack(50)
    rotate_degrees(-85,100)
    driveTilFrontTophatBlack(-20,-20)
    rotate(-90,35)
    drive_distance(9,35)
    rotate(90,35)
    driveTilBlackLCliffAndSquareUp(30,30)
    drive_distance(7.5,35)


def goYellowSecond():
    print "Yellow is in second position"
    #if yellow cube is in middle area
    turnTilRightFrontBlack(20,-20)
    drive_distance(-3,100)
    rotate_degrees(87, 100)
    driveTilFrontTophatBlack(-20,-20)


def goYellowThird():
    print "Yellow is in third position"
    #if yellow cube is in third zone (farthest from startbox)
    rotate_degrees(-85, 100)
    lineFollowRightFrontTilLeftFrontBlack(50)
    rotate_degrees(85, 100)
    driveTilFrontTophatBlack(-20, -20)


def dropBlocks(): #can we break this function up?
    print "Delivering crates"
    rotate(-5,25)
    drive_distance(1.5,35)
    moveServo(c.servoCrateArm, c.crateArmDown, 10)
    moveServo(c.servoCrateClaw, c.crateClawOpen, 10)
    moveServo(c.servoCrateArm, c.crateArmDeStack, 10)
    moveServo(c.servoCrateClaw, c.crateClawClosed, 10)
    moveServo(c.servoCrateArm, c.crateArmLiftCrate, 10)
    drive_distance(-1.5,35) #backup not currently working
    rotate(90,35)
    drive_distance(11.5,25)
    rotate(-90,35)
    wait_for_button()
    drive_timed(-120, -100, 1400)
    moveServo(c.servoCrateArm, c. crateArmDown)
    moveServo(c.servoCrateClaw, c.crateClawOpen)
    drive_timed(120, 100, 1400)
    DEBUG()
    msleep(500)
    # drive_timed(-60, -60, 1500)
    rotate_degrees(35, 40)
    drive_timed(-60, -60, 1500)
    # drive_timed(75, 75, 1200)
    # rotate_degrees(35, 65) #40
    # drive_timed(-75, -75, 1400)
    moveServo(c.servoCrateArm, c.crateArmDown, 10)
    if colorOrder[0] == c.YELLOW:
        rotate_degrees(-15, 56)
    # elif colorOrder[1] == c.YELLOW:
    elif colorOrder[2] == c.YELLOW:
        rotate_degrees(-8, 56)
    drive_timed(-100, -100, 900)
    moveServo(c.servoCrateClaw, c.crateClawSlightlyOpen-200, 10)
    moveServo(c.servoCrateArm, c.crateArmUp, 10)
    drive_timed(80, 80, 2000)
