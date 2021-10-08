import psutil
from time import sleep
import os

""" 
Watchdog script
restart a program if it close for malfunction.
"""

# code can have a update for accept values from parameter from console.


def isProcessRun(proccessName):
    """ check if process exist from the process list """
    processSet = set()
    
    # get list of process and make a set of process name.
    for processId in psutil.pids():    
        p = psutil.Process(processId)
        processSet.add(p.name().lower())
    
    # return True o False if process exist.
    if proccessName in processSet:
        return True
    else:
        return False

def executeProcess(proccessName):
    """ if the function is called restart the process for name gived """
    os.system(proccessName)

processName = "notepad.exe"

# infinite while loop for checking process exist and restart.
while True:
    
    # check if process exist.
    if not isProcessRun(processName):
        executeProcess(processName)
    
    # checking every 5 seconds.
    sleep(5)