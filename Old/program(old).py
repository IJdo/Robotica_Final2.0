import RPi.GPIO as GPIO
import time as time
import robothond
import UDP
import motor
import trackinsensor
#motor pinouts
IN1Motor1 = 6
IN2Motor1 = 5
PWM1 = 13
IN3Motor2 = 21
IN4Motor2 = 20
PWM2 = 18
#trackingsenor pinouts
P1_LINKS = 25
P2_MIDDEN = 17
P3_RECHTS = 27
#ultrasonic pinouts
S1_VOOR_TRG = 26
S1_VOOR_ECH = 24
S2_RECHTS_TRG = 19
S2_RECHTS_ECH = 16
S3_LINKS_TRG = 12
S3_LINKS_ECH = 23
#UDP
UDP_HOST = '192.168.3.128'
UDP_PORT = 65000
#Voicecontrol file
FILE_NAME = "temporalCommand.txt"
    

if __name__ == "__main__":
    Motor1 = motor.motor(IN1Motor1, IN2Motor1, IN3Motor2, IN4Motor2, PWM1, PWM2)
    Trackingsensor = trackinsensor.tracking_sensor(P1_LINKS,P2_MIDDEN,P3_RECHTS, Motor1)
    Ultrasoon_front = robothond.Ultrasonic_sensor(S1_VOOR_TRG, S1_VOOR_ECH)
    Ultrasoon_right = robothond.Ultrasonic_sensor(S2_RECHTS_TRG,S2_RECHTS_ECH)
    Ultrasoon_left = robothond.Ultrasonic_sensor(S3_LINKS_TRG,S3_LINKS_ECH)
    UDP_socket = UDP.UDP_Socket(UDP_HOST, UDP_PORT)    
    f = open(FILE_NAME, "r+")
    command = f.read()
    f.close()
    try:
        while command != "stop":
            f = open(FILE_NAME, "r+")
            command = f.read()
            if command == "go":
        #while True:
                distance_front = ((Ultrasoon_front.distance() + Ultrasoon_front.distance()
                                   + Ultrasoon_front.distance() + Ultrasoon_front.distance())/4)
            
                distance_left = ((Ultrasoon_left.distance() + Ultrasoon_left.distance()
                                  + Ultrasoon_left.distance() + Ultrasoon_left.distance())/4)
           
                distance_right = ((Ultrasoon_right.distance() + Ultrasoon_right.distance()
                                   + Ultrasoon_right.distance() + Ultrasoon_right.distance())/4)
            #time.sleep(0.01)
                UDP_socket.pack_float(distance_front, distance_left, distance_right, Motor1.Odometry, 1)    
                Trackingsensor.track_line_2()
                if (GPIO.input(Trackingsensor.midden) == 1 and GPIO.input(Trackingsensor.rechts) == 1 and GPIO.input(Trackingsensor.links) == 1):
                    Motor1.Stop()
                    time.sleep(0.5)
                    Motor1.Drive_forward(100)
                    Motor1.Stop()
                    time.sleep(0.5)
                
                if (Ultrasoon_left.distance() > Ultrasoon_right.distance()):
                    #while (Trackingsensor.midden == 0):
                    Motor1.Turn_left(80, 0.6)
                    print(Motor1.Odometry)
            else:
                print("no command given")
            #Trackingsensor.find_line()
        UDP_socket.pack_float(distance_front, distance_left, distance_right, 0, 0)
        GPIO.cleanup()
        f.truncate(0)
        print("demo afgelopen")
            
    except KeyboardInterrupt:
        print("meeting gestopt")
        f.truncate(0)
        UDP_socket.pack_float(distance_front, distance_left, distance_right, 0, 0)
        GPIO.cleanup()
            
            
        
        
    
    
    
    
    

    
    
    
    

