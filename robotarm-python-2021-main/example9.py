from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')
robotArm.speed = 2

# Jouw python instructies zet je vanaf hier:

for x in range(1, 5):   
    print(x)
    for z in range(x): 
        robotArm.grab()
        for y in range(4):
            robotArm.moveRight()
        robotArm.drop()
        for y in range(4):
            robotArm.moveLeft()
    robotArm.moveRight()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()


