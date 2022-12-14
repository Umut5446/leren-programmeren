from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')
robotArm.speed = 2

# Jouw python instructies zet je vanaf hier:
teller = 9
 
for x in range(5):
  robotArm.grab()
  for x in range(9):
    robotArm.moveRight()
  robotArm.drop()
  teller -= 2
  for x in range(teller):
    robotArm.moveLeft()
  teller -= 2

# robotArm.grab()
# for x in range(7):
#     robotArm.moveRight()
# robotArm.drop()
# for x in range(6):
#     robotArm.moveLeft()
  
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()


 