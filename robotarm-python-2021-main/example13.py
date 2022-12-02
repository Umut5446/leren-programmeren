from RobotArm import RobotArm

robotArm = RobotArm('exercise 13')
robotArm.randomLevel(1,7)
robotArm.speed = 5

# Jouw python instructies zet je vanaf hier:
teller = 1
robotArm.grab()
for y in range(8):
    robotArm.moveRight() 
    robotArm.drop()
    for x in range(8):    
        robotArm.moveLeft()
    robotArm.grab()
    for x in range(teller):
        robotArm.moveRight()
        teller += 1
    
 
  

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()


 