from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')
robotArm.speed = 5

# Jouw python instructies zet je vanaf hier:
for x in range(15):
    robotArm.grab()
    collor = robotArm.scan() 
    if collor == 'red':
        for x in range(10):
          robotArm.moveRight()
        robotArm.drop()
        for x in range(10):
           robotArm.moveLeft()
    else:
         robotArm.drop() 
         robotArm.moveRight()       
         print(collor)
    

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()


 