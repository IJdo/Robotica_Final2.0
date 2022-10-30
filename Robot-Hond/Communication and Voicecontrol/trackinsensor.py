import RPi.GPIO as GPIO
import time
import motor

class tracking_sensor:
    def __init__(self, p1, p2, p3, motor1):
        GPIO.setmode(GPIO.BCM)
        self.links = p1
        self.midden = p2
        self.rechts = p3
        self.motor = motor1
        GPIO.setup(self.links, GPIO.IN)
        GPIO.setup(self.midden, GPIO.IN)
        GPIO.setup(self.rechts, GPIO.IN)
        
    def track_line(self):
        print(GPIO.input(self.links),GPIO.input(self.midden), GPIO.input(self.rechts))
        #if (GPIO.input(self.midden) == 1 and GPIO.input(self.rechts) == 1 and GPIO.input(self.links) == 1):
            #self.motor.Stop()
            #self.motor.correct_left(0.05, 60)
            #time.sleep(0.005)
        #elif (
           # self.motor.Stop()
        if GPIO.input(self.rechts) == 0:
            self.motor.correct_left(55)
            time.sleep(0.005)
        elif GPIO.input(self.links) == 0:           
            #print("corrigeer rechts")
            self.motor.correct_right(50)
            time.sleep(0.005)
        
        else:
            self.motor.Drive_forward(55)
            time.sleep(0.005)
            
    def track_line_2(self):
        print(GPIO.input(self.links),GPIO.input(self.midden), GPIO.input(self.rechts))
        #if (GPIO.input(self.midden) == 0 and GPIO.input(self.rechts) == 0 and GPIO.input(self.links) == 0):
            #self.motor.Stop()
            #if distance_left>distance_right:
             #   self.motor.Turn_left(60)
            
            #elif distance_right>distance_left:
             #   self.motor.Turn_right(0.6, 60)
                
            
        if (GPIO.input(self.rechts) == 0 and GPIO.input(self.links) == 1):
            self.motor.correct_left(60)
            time.sleep(0.01)
              
        elif (GPIO.input(self.rechts) == 1 and GPIO.input(self.links) == 0):
            self.motor.correct_right(60)
            time.sleep(0.01)
            
        else: #(GPIO.input(self.rechts) == 0 and GPIO.input(self.links) == 0 and GPIO.input(self.midden) == 1):
            self.motor.Drive_forward(60)
            time.sleep(0.01)
        #elif (GPIO.input(self.midden) == 0 and GPIO.input(self.rechts) == 0 and GPIO.input(self.links) == 0):
            #self.motor.correct_left(60)
            
    def track_line_3(self):
        while (GPIO.input(self.rechts) == 1 and GPIO.input(self.links) == 0):
            self.motor.correct_left(60)
        while (GPIO.input(self.rechts) == 0 and GPIO.input(self.links) == 1):
            self.motor.correct_right(60)
        self.motor.Drive_forward(60)
        
            
            
            
            
    def find_line(self):
        print(GPIO.input(self.links),GPIO.input(self.midden), GPIO.input(self.rechts))
        if (GPIO.input(self.midden) == 0 and GPIO.input(self.rechts) == 0 and GPIO.input(self.links) == 1):
            self.motor.Turn_left(0.6, 55)
        elif (GPIO.input(self.midden) == 0 and GPIO.input(self.rechts) == 1 and GPIO.input(self.links) == 0):
            self.motor.Turn_right(0.6, 55)
    

if __name__ == "__main__":
    print ("Main")
    IN1Motor1 = 6
    IN2Motor1 = 5
    PWM1 = 13
    IN3Motor2 = 21
    IN4Motor2 = 20
    PWM2 = 18
    
    
    Motor1 = motor.motor(IN1Motor1, IN2Motor1, IN3Motor2, IN4Motor2, PWM1, PWM2)
    trackingsensor = tracking_sensor(25,17,27, Motor1)
    #Motor1.Turn_left(1)
    try:
        while True:            
            trackingsensor.track_line_2()
            #trackingsensor.find_line()
            
        
    except KeyboardInterrupt:
        print("meeting gestopt")
        GPIO.cleanup()
            
            