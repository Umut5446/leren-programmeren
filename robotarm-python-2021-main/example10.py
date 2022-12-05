from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')
robotArm.speed = 2 

# Jouw python instructies zet je vanaf hier:
teller = 4
robotArm.grab()
for x in range(9): robotArm.moveRight() 
robotArm.drop() 
for x in range(5): robotArm.moveLeft()
for x in range(1):
    for x in range(1, teller):
        robotArm.grab()
        for x in range(4): robotArm.moveRight()
        robotArm.drop()
        for x in range(5): robotArm.moveLeft()
    robotArm.grab()
    for x in range(4): robotArm.moveRight()
    robotArm.drop()
    teller += 1 
 


 
 
  
 
 
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()


 