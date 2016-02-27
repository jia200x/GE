import pygame
from objs import Object
from scenario import Scenario
from smgr import SMGR
def main():
    #Init
    #Scenario Manager
    smg = SMGR()

    #Just for testing, add new Scenario
    scen = Scenario()
    scen.register(smg)
    smg.add_scenario(scen)

    #Add an object
    obj = Object()
    obj.register(scen)

    while(True):
        pass
        #Input
        #Process
        #Output:
        #   For current stagemanager, draw scenario. For objectmanager, draw each visible object

main()
