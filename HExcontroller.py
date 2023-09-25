from controller import Robot
import math
timestep=32

robot=Robot()

motorRPC =robot.getDevice("RPC")
motorRPF=robot.getDevice("RPF")
motorRMC= robot.getDevice("RMC")
motorRMF= robot.getDevice("RMF")
motorRAC= robot.getDevice("RAC")
motorRAF= robot.getDevice("RAF")

motorLPC= robot.getDevice("LPC")
motorLPF= robot.getDevice("LPF")
motorLMC= robot.getDevice("LMC")
motorLMF= robot.getDevice("LMF")
motorLAC= robot.getDevice("LAC")
motorLAF= robot.getDevice("LAF")

n=0

while robot.step(timestep) != -1:
    t=0
    if(n%2 == 0):
        t += 0.3
    elif(n%3 == 0):
        t-=0.3
    elif(n%6 == 1):
        t-=0.6
        
    motorRPC.setPosition(t)
    n+=1
    
    
    pass
    
    
    