from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')
robotArm.speed = 2

# Jouw python instructies zet je vanaf hier:
for x in range(8):
    robotArm.moveRight()
for x in range(9):
    robotArm.grab()
    collor = robotArm.scan() 
    if collor == 'white':
        robotArm.moveRight()
        robotArm.drop()
        for x in range(2):
         robotArm.moveLeft()
        
    else:
         robotArm.drop()
         if x < 8:
          robotArm.moveLeft()        
          print(collor)
 

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()


 