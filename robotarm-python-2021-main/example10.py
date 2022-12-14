from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')
robotArm.speed = 2

# Jouw python instructies zet je vanaf hier:
for x in range(4):
    robotArm.grab()
    for x in range(5): robotArm.moveRight()
    robotArm.drop()
    for x in range(4): robotArm.moveLeft()
robotArm.grab()
for x in range(5): robotArm.moveRight()
robotArm.drop()

# robotArm.grab()
# for x in range(7):
#     robotArm.moveRight()
# robotArm.drop()
# for x in range(6):
#     robotArm.moveLeft()
  
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()


 