#!/usr/bin/env python3
#___________________________________________________________________________________
#
# RyanModule2.py in python3.4
#
# 
# 
#____________________________________________________________________________________


import sys  #for exit
import time
import os
import logging
from logging import handlers


#******************************LogBuilder Class ********************************************
class LogBuilder:
    """ The LogBuilder module contains:
        logInit(logfile, when, interval, backupCount)
        build(logDesc).
    """
    
    def __init__(self,logFile,when,interval,backupCount):
        self.logging_level = logging.DEBUG
        self.formatter=logging.Formatter('%(asctime)s %(name)s %(levelname)s:: %(message)s')
        self.logFileV=logFile
        self.whenV=when
        self.intervalV=interval
        self.backupCountV=backupCount
    def logInit(self):
        self.RHand=handlers.TimedRotatingFileHandler(self.logFileV,self.whenV,self.intervalV,self.backupCountV)
        self.RHand.setFormatter(self.formatter)
        return(self.RHand)
    def build(self,logDesc):
        self.Rlogger = logging.getLogger(logDesc)
        self.Rlogger.addHandler(self.RHand)
        self.Rlogger.setLevel(self.logging_level)
        return(self.Rlogger)

