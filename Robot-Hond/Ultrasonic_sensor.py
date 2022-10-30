import RPi.GPIO as GPIO
import time
#import UDP

class Ultrasonic_sensor:
    def __init__(self, Trigger_pin, Echo_pin):
        #GPIO Mod(board/BCM)
        GPIO.setmode(GPIO.BCM)
        #pin numbers board/BCM
        self.GPIO_TRIGGER = Trigger_pin
        self.GPIO_ECHO = Echo_pin
        #set pin direction
        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)
        
    def distance(self):
        GPIO.output(self.GPIO_TRIGGER, True)
        time.sleep(0.00001) #wait 10 micro seconds  
        GPIO.output(self.GPIO_TRIGGER, False) 
        StartTime = time.time()
        StopTime = time.time()
    
        while GPIO.input(self.GPIO_ECHO) == 0:
            StartTime = time.time()
        
        while GPIO.input(self.GPIO_ECHO) == 1:
            StopTime = time.time()
    
        TimeElapsed = StopTime - StartTime
        distance = (TimeElapsed * 34300) / 2
        time.sleep(0.01)
    
        return distance



if __name__== "__main__":
    Ultrasoon_front = Ultrasonic_senor(26, 24)
    UDP_socket = UDP.UDP_Socket('192.168.55.128', 65000) 
    #192.168.178.186 is adress pi, 192.168.178.178 is pc(wifi ijdo thuis)
    try:
        while True:
            print("hallo")
            dist = Ultrasoon_front.distance()
            UDP_socket.pack_float(dist)
            time.sleep(1)
    except KeyboardInterrupt:
        print("meeting gestopt")
        GPIO.cleanup()
    

#try:
#    while True:
 #       print("hallo")
  #      dist = distance()
   #     message = pack('1f', dist)
    #    sock.sendto(message, server_address)
        
        #print("gemeten afstand = %0.1f cm" % distance())
     #   time.sleep(0.5)
            
#except KeyboardInterrupt:
 #   print("gebruiker heeft meting gestopt")
  #  GPIO.cleanup()