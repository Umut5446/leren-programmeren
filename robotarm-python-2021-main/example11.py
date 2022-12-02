from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')
robotArm.speed = 2

# Jouw python instructies zet je vanaf hier:
for x in range(9):
    robotArm.grab()
    collor = robotArm.scan() 
    if collor == 'white':
        for x in range(1):
          robotArm.moveRight()
        robotArm.drop()
        robotArm.moveRight()
    else:
         robotArm.drop()
         robotArm.moveRight()        
         print(collor)
 

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()


 