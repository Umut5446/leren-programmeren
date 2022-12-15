from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')
robotArm.speed = 2

# Jouw python instructies zet je vanaf hier:
teller = 9

for z in range(1,6):
  robotArm.grab()
  for x in range(teller):
   robotArm.moveRight()
  robotArm.drop()
  for x in range(teller -1):
   robotArm.moveLeft()
  teller -= 2

  
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()


 