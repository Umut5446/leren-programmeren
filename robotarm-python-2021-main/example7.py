from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')
robotArm.speed = 4

# Jouw python instructies zet je vanaf hier:
for y in range(5):
    robotArm.moveRight() 
    for x in range(6):
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
  

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()


 