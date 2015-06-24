
#___________________________________________________________________________________
#
#RyanModule.py  developed in python3
#
# This is a module containing a collection of functions defeloped by Ryan
# 
#____________________________________________________________________________________

import time
import datetime
import logging
from logging.handlers import TimedRotatingFileHandler
import os

def chkLogfile():
    day=(str(datetime.datetime.now().strftime("%m-%d-%y")))
    status = os.path.exists('ryanLog_'+day+'.log')
    print(status, ': '+'ryanLog_'+day+'.log')
    return(status)
    
def initLog():
    stat=chkLogfile()
    day=(str(datetime.datetime.now().strftime("%m-%d-%y")))
    if stat==False:
        #Logging Configuration
        logging.basicConfig(level=logging.INFO, filename='ryanLog_'+day+'.log')
    return         


def printWlog(data,logLevel='inf'):
    
    print(data)
    
    if logLevel == 'inf':
        logging.info(str(time.asctime(time.localtime()))+' : '+ data)
        return
    elif logLevel == 'warning':
        logging.warning(str(time.asctime(time.localtime()))+' : '+ data)
        return
    elif logLevel == 'critical':
        logging.critical(str(time.asctime(time.localtime()))+' : '+ data)
        return
    elif logLevel == 'error':
        logging.error(str(time.asctime(time.localtime()))+' : '+ data)
        return
    elif logLevel == 'debug':
        logging.debug(str(time.asctime(time.localtime()))+' : '+ data)
        return
    elif logLevel == 'exception':
        logging.exception(str(time.asctime(time.localtime()))+' : '+ data)
        return
    else:
        logging.info(str(time.asctime(time.localtime()))+' : '+ data)
        return

#----------------------------------------------------------------------
def create_timed_rotating_log(path):
    """"""
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)
 
    handler = TimedRotatingFileHandler(path,when="m",interval=1,backupCount=5)
    logger.addHandler(handler)
    return(logger)




#def test():
#    pringWlog('test data', )

#########################################################################################
#if__name__ == '__main__': test()