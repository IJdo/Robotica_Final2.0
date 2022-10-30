import Robothond
#kamer_width = 150
#kamer_height = 150
#start_x = 0
#stat_y = 0
#resolutie = 30
#vooruitrijden snelheid 60
#vooruitrijden tijd 0.75

if __name__ == "__main__":
    Robot = Robothond.Robot_Hond(0,0,150,150,30)
    
    while(1):
        #check of de huidige cell de laatste Cell is
        if(Robot.check_last_cell()):
            Robot.Stop()
            break
        #check of de volgende Cell in de huidige richting nog binnen de map past
        if(Robot.check_out_of_bound()):
            if (Robot.motor.Orientatie == 0) or (Robot.motor.Orientatie == 270):
                Robot.motor.Turn_left(100, 0.27)
            elif (Robot.motor.Orientatie == 180) or (Robot.motor.Orientatie == 90):
                Robot.motor.Turn_right(100, 0.27)
            else:
                Robot.Stop()
                break
        
        if(Robot.us_front.distance() > 15):
            if not (Robot.check_next_cell_visited()):
                Robot.mark_next_cell_visited()
            Robot.motor.Drive_forward(100,0.35)
            Robot.Update_lokatie()
        elif(Robot.us_right.distance() > 15):
            Robot.mark_next_cell_front_occupant()
            Robot.motor.Turn_right(100, 0.27)
            if not (Robot.check_next_cell_visited()):
                Robot.mark_next_cell_visited()
            Robot.motor.Drive_forward(60,0.75)
            Robot.Update_lokatie()
        elif (Robot.us_left.distance()> 15):
            Robot.mark_next_cell_front_occupant()
            Robot.motor.rotation = ((Robot.motor.Orientatie + 270)%360)
            Robot.mark_next_cell_front_occupant()
            Robot.motor.rotation = ((Robot.motor.Orientatie - 270)%360)
            Robot.motor.Turn_left(100, 0.27)
            if not (Robot.check_next_cell_visited()):
                Robot.mark_next_cell_visited()
            Robot.motor.Drive_forward(60,0.75)
            Robot.Update_lokatie()
            
        else:
            Robot.mark_next_cell_front_occupant()
            Robot.motor.rotation = ((Robot.motor.Orientatie + 270)%360) #Cell rechts van huidige Cell
            Robot.mark_next_cell_front_occupant()
            Robot.motor.rotation = ((Robot.motor.Orientatie - 180)%360)#Cell links van huidige Cell
            Robot.mark_next_cell_front_occupant()
            Robot.motor.rotation = ((Robot.motor.Orientatie - 90)%360) #Orginele lokatie
            #180 graden draaien
            Robot.motor.Turn_left(100, 0.27)
            Robot.motor.Turn_left(100, 0.27)
            Robot.motor.Drive_forward(60, 0.75)
            Robot.Update_lokatie()
            
            