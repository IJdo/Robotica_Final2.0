import RPi.GPIO as io
import time as time
io.setmode(io.BCM)

in1_pin = 6
in2_pin = 5
pwm1_pin = 13

io.setup(in1_pin, io.OUT)
io.setup(in2_pin, io.OUT)
io.setup(pwm1_pin, io.OUT)

pi_pwm = io.PWM(pwm1_pin,1000)		#create PWM instance with frequency
pi_pwm.start(0)				#start PWM of required Duty Cycle
io.output(in1_pin, True)    
io.output(in2_pin, False)
try:
    while True:
        print("test")
        pi_pwm.ChangeDutyCycle(10)
        time.sleep(0.5)
        pi_pwm.ChangeDutyCycle(20)
        time.sleep(0.5)
        pi_pwm.ChangeDutyCycle(30)
        time.sleep(0.5)
        pi_pwm.ChangeDutyCycle(40)
        time.sleep(0.5)
        pi_pwm.ChangeDutyCycle(50)
        time.sleep(0.5)
        pi_pwm.ChangeDutyCycle(100)
        time.sleep(0.5)
except KeyboardInterrupt:
        print("meeting gestopt")
        io.cleanup()
 