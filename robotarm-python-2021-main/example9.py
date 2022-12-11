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
 

# teller = 4
# robotArm.grab()
# for x in range(4): robotArm.moveRight()
# robotArm.drop()
# for x in range(3): robotArm.moveLeft()
# for x in range(3):
#     for x in range(2, teller):
#         robotArm.grab()
#         for x in range(4): robotArm.moveRight()
#         robotArm.drop()
#         for x in range(4): robotArm.moveLeft()
#     teller += 1
#     robotArm.moveRight()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()


