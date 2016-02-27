import pygame
from objs import Object
from scenario import Scenario
from smgr import SMGR
from core import Core

def main():

    #Add core
    core = Core()
    #Scenario Manager
    smg = SMGR(core)

    #Just for testing, add new Scenario
    scen = Scenario()
    scen.register(smg)

    #Add an object
    obj = Object()
    obj.register(scen)
    

    while(True):
        core.input()
        smg.process()
        smg.render()
        #   For current stagemanager, draw scenario. For objectmanager, draw each visible object

main()
