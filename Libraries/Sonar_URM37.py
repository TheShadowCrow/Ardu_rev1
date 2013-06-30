import time
import RPi.GPIO as GPIO

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(24,GPIO.IN) 

def read():
    start = time.time()
    while GPIO.input(24)==1:
        start = time.time()

    while GPIO.input(24)==0:
        stop = time.time()

    # Calculate pulse length
    elapsed = stop-start 
    distance = int(elapsed * 1000000 /50)
    return distance
    

if __name__ == "__main__":
    Sonar_setup()
    while True:
        print Distance_read()