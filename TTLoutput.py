import RPi.GPIO as GPIO
import time

#setup OUT pin for RPi as pin 7 (capturing device) and pin 12 (lamp)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False) #prevents annoying warnings from popping up
GPIO.setup(12, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)

#module for no background collection
def Pulse(numTimes, cycleTime, onTime, offTime):
    for i in range(0, numTimes):
        GPIO.output(12, False)
        GPIO.output(7, False)
        if int(i/numTimes*100) < 100: #used for progress report
            print("Running... {}%".format(int(i/numTimes*100)), end="\r")
        time.sleep(onTime)
        GPIO.output(12, True)
        GPIO.output(7, True)
        time.sleep(offTime-onTime)
        GPIO.output(12,False)
        GPIO.output(7, False)
        time.sleep(cycleTime-offTime)
    print("Running... {}%".format(100)) #shows 100% complete when done

#module with background collecting before each measurement
def BackgroundPulse(numTimes, cycleTime, onTime, offTime):
    for i in range(0, numTimes):
        GPIO.output(12, False)
        GPIO.output(7, False)
        if int(i/numTimes*100) < 100: #used for progress report
            print("Running... {}%".format(int(i/numTimes*100)), end="\r")
        time.sleep(onTime)
        GPIO.output(7, True)
        time.sleep(offTime-onTime)
        GPIO.output(7, False)
        time.sleep(cycleTime-offTime+onTime)
        GPIO.output(7, True)
        GPIO.output(12, True)
        time.sleep(offTime-onTime)
        GPIO.output(7, False)
        GPIO.output(12, False)
        time.sleep(cycleTime-offTime)
    print("Running... {}%".format(100)) #shows 100% when complete
     

iterations = input("Enter total number of times to output pulse: ")
cycleT = input("Enter total time for each on/off cycle (seconds): ")
onT = input("Enter time in cycle to turn ON device(s): ")
offT = input("Enter time in cycle to turn OFF device(s): ")
needBackground = input("Do you wish to collect background data before each sample? (y/n): ")

if needBackground == "y" or needBackground == "Y":
    BackgroundPulse(int(iterations), float(cycleT), float(onT), float(offT))
elif needBackground == "n" or needBackground == "N":
    Pulse(int(iterations), float(cycleT), float(onT), float(offT))
else:
    print("Invalid input!")

