#!/usr/bin/env python3
#___________________________________________________________________________________
#
#Ryan_log_test.py in python3.4
#
#Test program to test logging class module
#Configuration file support
#____________________________________________________________________________________


import sys  #for exit
import time
import os
import LogModule
import RyanModule2
import configparser

#*************Configuration File***************************************
CONFIGFILE= "Rconf.txt"
confParser = configparser.ConfigParser()

try:
    confParser.read(CONFIGFILE)
    #print(confParser.sections())  #print out configuration sections
    
    #Configuration constant verialbles______________________
    LOGFILE = confParser.get('LOGINFO','logFile')
    ROLLWHEN = confParser.get('LOGINFO','rollWhen')
    ROLLINTERVAL = confParser.getint('LOGINFO','rollInterval')
    ROLLBACKUPCOUNT = confParser.getint('LOGINFO','rollBackupCount')
    
    #_______________________________________________________
    ConfSuccess='configuration file loaded successfuly'  #logging is not defined before configuration file is read
except:
    raise

#fp = '[sect] temp: this is a value'
#configparser.write(fp)
#confParser.set('sect', 'opt', '%(opt)s')
    
    
#*************Log configuration ***************************************
LogHand=RyanModule2.LogBuilder(logFile=LOGFILE,when=ROLLWHEN,interval=ROLLINTERVAL,backupCount=ROLLBACKUPCOUNT)
LogHand.logInit()
Rlogger1 = LogHand.build(logDesc='MainProgram Log')
Rlogger2 = LogHand.build(logDesc='Exception Log')
#print( LogHand.__doc__)

Rlogger1.info('Logger initiated successfuly')
Rlogger1.info(ConfSuccess) #post configuration success to logfile


#*************MAIN PROGRAM*************************************************************
while True:
    try:
        #Enter main code here**********************************************************
        Rlogger1.info("zippp!!!!")
        Rlogger1.warning('This is a warning zip!!!')
        time.sleep(1)
    except:
        Rlogger2.warning('exiting program')
        break