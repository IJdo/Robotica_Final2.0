import RPi.GPIO as GPIO
import time as time
import pinout

class motor:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.pinout = pinout.Pinout()
        self.MotorIN1 = self.pinout.IN1Motor1
        self.MotorIN2 = self.pinout.IN2Motor1
        self.PWM1 = self.pinout.PWM1
        self.MotorIN3 = self.pinout.IN3Motor2
        self.MotorIN4 = self.pinout.IN4Motor2
        self.PWM2 = self.pinout.PWM2
        self.Orientatie = 0
        
        GPIO.setup(self.MotorIN1, GPIO.OUT)
        GPIO.setup(self.MotorIN2, GPIO.OUT)
        GPIO.setup(self.PWM1, GPIO.OUT)
        self.pi_pwm1 = GPIO.PWM(self.PWM1,1000)#create PWM instance with frequency
        self.pi_pwm1.start(0)
        
        GPIO.setup(self.MotorIN3, GPIO.OUT)
        GPIO.setup(self.MotorIN4, GPIO.OUT)
        GPIO.setup(self.PWM2, GPIO.OUT)
        self.pi_pwm2 = GPIO.PWM(self.PWM2,1000)#create PWM instance with frequency
        self.pi_pwm2.start(0)  
                 
        
    def Drive_forward(self, speed, duration):        
        GPIO.output(self.MotorIN1, GPIO.LOW) #Motor1(rechts) forward laten rijden is In1 laag en In2 hoog
        GPIO.output(self.MotorIN2, GPIO.HIGH)
        GPIO.output(self.MotorIN3, GPIO.HIGH) #motor2(links) forward latenrijden is in3 hoog en in4 laag
        GPIO.output(self.MotorIN4, GPIO.LOW)
        self.pi_pwm1.ChangeDutyCycle(speed)
        self.pi_pwm2.ChangeDutyCycle(speed)
        time.sleep(duration)
        self.Stop()   
        
    def Turn_left(self, speed, duration):        
        GPIO.output(self.MotorIN1, GPIO.LOW)
        GPIO.output(self.MotorIN2, GPIO.HIGH)
        GPIO.output(self.MotorIN3, GPIO.LOW)
        GPIO.output(self.MotorIN4, GPIO.HIGH)
        self.pi_pwm1.ChangeDutyCycle(speed)
        self.pi_pwm2.ChangeDutyCycle(speed)
        time.sleep(duration)
        self.Stop()
        self.Orientatie = (self.Orientatie + 90) % 360
        print("Orientatie = " + str(self.Orientatie))
        

    def Turn_right(self, speed, duration):        
        GPIO.output(self.MotorIN1, GPIO.HIGH)
        GPIO.output(self.MotorIN2, GPIO.LOW)
        GPIO.output(self.MotorIN3, GPIO.HIGH)
        GPIO.output(self.MotorIN4, GPIO.LOW)
        self.pi_pwm1.ChangeDutyCycle(speed)
        self.pi_pwm2.ChangeDutyCycle(speed)
        time.sleep(duration)
        self.Stop()
        self.Orientatie = (self.Orientatie + 270) % 360
        print("Orientatie = " + str(self.Orientatie))
    
    def Stop(self):
        GPIO.output(self.MotorIN1, GPIO.LOW)
        GPIO.output(self.MotorIN2, GPIO.LOW)
        GPIO.output(self.MotorIN3, GPIO.LOW)
        GPIO.output(self.MotorIN4, GPIO.LOW)
        self.pi_pwm1.ChangeDutyCycle(0)
        self.pi_pwm2.ChangeDutyCycle(0)
        time.sleep(3)

    


if __name__ == "__main__":
    print ("Main")
    #IN1Motor1 = 6
    #IN2Motor1 = 5
    #PWM1 = 13    
    #IN3Motor2 = 21
    #IN4Motor2 = 20
    #PWM2 = 18
    
    Motor1 = motor()
    #Motor1 = motor(IN1Motor1, IN2Motor1, IN3Motor2, IN4Motor2, PWM1, PWM2)
    #Ultrasoon_front = robothond.Ultrasonic_sensor(26, 24)
    #Ultrasoon_right = robothond.Ultrasonic_sensor(19,16)
    #Ultrasoon_left = robothond.Ultrasonic_sensor(12,23)
    #UDP_socket = UDP.UDP_Socket('192.168.203.128', 65000) #192.168.55.128 mobiele hotspot ijdo
    #distance = Ultrasoon_front.distance()
    #distance = Ultrasoon_right.distance()
    #distance = Ultrasoon_left.distance()
    Motor1.Turn_right(100, 0.27)
    
    try:

        while True:
            break
            #Motor1.Drive_forward(100, 1)
        #for i in range(11):
            #Motor1.Drive_forward(100, 3)
#            Motor1.Turn_left(0.3)
#            Motor1.Turn_right(0.3)
            
            #distance_front = ((Ultrasoon_front.distance() + Ultrasoon_front.distance() + Ultrasoon_front.distance() + Ultrasoon_front.distance())/4)
            
            #distance_left = ((Ultrasoon_left.distance() + Ultrasoon_left.distance() + Ultrasoon_left.distance() + Ultrasoon_left.distance())/4)
           
            #distance_right = ((Ultrasoon_right.distance() + Ultrasoon_right.distance() + Ultrasoon_right.distance() + Ultrasoon_right.distance())/4)
            #time.sleep(0.01)
            #UDP_socket.pack_float(distance_front, distance_left, distance_right, 0, 1)
            
            #Motor1.Drive_forward(55)
            #time.sleep(0.14)
            
            #if distance_front <= 10:
                #Motor1.Stop()
                #time.sleep(0.2)
                #left = Motor1.Turn_left(1)
                #time.sleep(0.2)
                #distance = Ultrasoon_front.distance()
                #distance = Ultrasoon_right.distance()
                #distance = Ultrasoon_left.distance()
                #UDP_socket.pack_float(distance, left)    
            
            
    except KeyboardInterrupt:
        print("meeting gestopt")
        #UDP_socket.pack_float(distance_front, distance_left, distance_right, 0, 0)       
        GPIO.cleanup()
        
    

