import motor
import RPi.GPIO as GPIO


if __name__ == "__main__":
    IN1Motor1 = 6
    IN2Motor1 = 5
    IN3Motor2 = 21
    IN4Motor2 = 20 
    Motor = motor.motor(IN1Motor1, IN2Motor1, IN3Motor2, IN4Motor2)
    f = open("temporalCommand.txt", "r+")
    command = f.read()
    print(command)
    f.close()

    while command != "stop":
        f = open("temporalCommand.txt", "r+")
        command = f.read()
        print(command)
        if command == "go" or command == "forward":
            Motor.Drive_forward(1)
            f.truncate(0)
            f.close()# Empty file, set to 0            
        elif command == "right":
            Motor.Turn_right(0.2)
            f.truncate(0)
            f.close()# Empty file, set to 0 
        elif command == "left":
            Motor.Turn_left(0.2)
            f.truncate(0)
            f.close()# Empty file, set to 0 
        elif command == "stop":
            Motor.Stop(1)
            f.truncate(0)
            
    GPIO.cleanup()
    f.close()
            
