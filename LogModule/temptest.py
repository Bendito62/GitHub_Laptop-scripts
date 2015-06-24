#!/usr/bin/env python3
#___________________________________________________________________________________
#
#temptest.py  developed in python3
#
# This is a temp script to test code and modules
# 
#____________________________________________________________________________________

import RyanModule

#stat = RyanModule.chkLogfile()
#print(stat)
#RyanModule.initLog()
#stat = RyanModule.chkLogfile()
#print(stat)
#
#RyanModule.printWlog('this is a temp log entery', 'warning')


RyanModule.create_timed_rotating_log('timed_log.log')
for i in range(6):
    logging.info("This is a test!")
    time.sleep(75)