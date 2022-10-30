import motor
import Gridmap
import pinout
import Ultrasonic_sensor

class Robot_Hond:
    def __init__(self, start_x, start_y , room_width, room_height, scale):
        #Aansluitschema
        self.pinout = pinout.Pinout()
        #Map en Lokatie
        self.map = Gridmap.Gridmap(room_width, room_height, scale)
        self.start_x = start_x
        self.start_y = start_y
        self.locatie_start = self.map.grid[start_x][start_y]
        self.locatie_current = self.locatie_start
        self.locatie_last = self.locatie_current
        #motor
        self.motor = motor.motor()
        #sensors
        self.us_front = Ultrasonic_sensor.Ultrasonic_sensor(self.pinout.S1_VOOR_TRG, self.pinout.S1_VOOR_ECH)
        self.us_right = Ultrasonic_sensor.Ultrasonic_sensor(self.pinout.S2_RECHTS_TRG, self.pinout.S2_RECHTS_ECH)
        self.us_left = Ultrasonic_sensor.Ultrasonic_sensor(self.pinout.S3_LINKS_TRG, self.pinout.S3_LINKS_ECH)
        #Start lokatie feedback
        print("Locatie = (" + str(self.locatie_current.x) + "," + str(self.locatie_current.y) + ")")
        print("Orientatie = " + str(self.motor.Orientatie))
   

    def check_next_cell_visited(self):
        if (self.motor.Orientatie == 0) and self.map.grid[self.start_x + 1][self.start_y].visited is False:
            return False
        elif(self.motor.Orientatie == 90) and self.map.grid[self.start_x][self.start_y + 1].visited is False:
            return False
        elif (self.motor.Orientatie == 180) and self.map.grid[self.start_x - 1][self.start_y].visited is False:
            return False
        elif (self.motor.Orientatie == 270) and self.map.grid[self.start_x][self.start_y - 1].visited is False:
            return False
        else:
            return True
        
    def mark_next_cell_visited(self):
        if (self.motor.Orientatie == 0):
            self.map.grid[self.start_x + 1][self.start_y].visited = True
        elif (self.motor.Orientatie == 90):
            self.map.grid[self.start_x][self.start_y + 1].visited = True
        elif (self.motor.Orientatie == 180):
            pass
        elif(self.motor.Orientatie == 270):
            self.map.grid[self.start_x][self.start_y - 1].visited = True



    def mark_next_cell_front_occupant(self):
        
        if (self.motor.Orientatie == 0):
            self.map.grid[self.start_x + 1][self.start_y].occupant = True
        elif (self.motor.Orientatie == 90):
            self.map.grid[self.start_x][self.start_y + 1].occupant = True
        elif (self.motor.Orientatie == 180):
            pass
        elif(self.motor.Orientatie == 270):
            self.map.grid[self.start_x][self.start_y - 1].occupant = True

    def mark_next_cell_right_occupant(self):
        if (self.motor.Orientatie == 0):
            self.map.grid[self.start_x][self.start_y - 1].occupant = True
        elif (self.motor.Orientatie == 90):
            self.map.grid[self.start_x][self.start_y + 1].occupant = True
        elif (self.motor.Orientatie == 180):
            pass
        elif (self.motor.Orientatie == 270):
            self.map.grid[self.start_x][self.start_y - 1].occupant = True

    def check_out_of_bound(self): #efficienter maken door if not te gebruiken
            
        if(self.motor.Orientatie == 0) and ((self.start_x + 1) > self.map.last_cell.x):
            return True
        elif(self.motor.Orientatie == 90) and ((self.start_y + 1) > self.map.last_cell.y):
            return True
        elif(self.motor.Orientatie == 180) and ((self.start_x - 1) < 0):
            return True
        elif(self.motor.Orientatie == 270) and ((self.start_y - 1) < 0):
            return True
        else:
            return False

    def check_last_cell(self):
        if (self.map.last_cell is not self.locatie_current):
            return False
        else:
            return True

    def Stop(self): # stop the robot
        print("STOPPING!!!!")
        self.motor.Stop()
        self.Send_map()
        
    def Send_map(self):# map complete, show/send map
        self.map.show_map()

    def Update_lokatie(self): #alleen lokatie updaten nadat 1 cell vooruit is gereden.
        self.locatie_last = self.map.grid[self.start_x][self.start_y]
        if self.motor.Orientatie == 0: #update lokatie met 1 cell in voorwaardse richting(x-richting)
            self.start_x = self.start_x + 1
        elif self.motor.Orientatie == 90:# update locatie met 1 cell naar rechts (y-richting)
            self.start_y = self.start_y + 1
        elif self.motor.Orientatie == 180: # update lokatie met 1 cell achterwaards (negatieve x-richting)
            self.start_x = self.start_x - 1
        elif self.motor.Orientatie == 270: # update Locatie met 1 cell naar links (negatieve y- richting)
            self.start_y = self.start_y - 1
        self.locatie_current = self.map.grid[self.start_x][self.start_y]
        print("Locatie = (" + str(self.locatie_current.x) + "," + str(self.locatie_current.y) + ")")
        print("Orientatie = " + str(self.motor.Orientatie))

if __name__ == '__main__':
    robothond = Robot_Hond(0,0,150,150,30) #(self, start_x, start_y, room_width, room_height, scale)
    while(True):
        if(robothond.check_out_of_bound()):
            robothond.Send_map()
            break
        robothond.Drive_1_Cell()