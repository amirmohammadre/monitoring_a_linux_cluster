############################## Client Section ##############################

#!/usr/bin/python3

import time as tm
import socket 
import subprocess

#-----------------------------------------------------------------------------------------
"""
This function executes commands remotely on the target node
"""
def Shell():

        enum = 0

        while True:


            #This command for checking status pacemaker service 
            command_systemctl = "systemctl is-active pacemaker.service | grep -c ^a"


            #And This command get date and time
            command_datetime  =  "date +'%Y/%m/%d|%H:%M:%S'"

            
            
            proc_systemctl   = subprocess.Popen(command_systemctl, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result_systemctl = proc_systemctl.stdout.read() + proc_systemctl.stderr.read()


            proc_datetime   = subprocess.Popen(command_datetime, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result_datetime = proc_datetime.stdout.read() + proc_datetime.stderr.read()


            sock.send(result_datetime) 
            sock.send(result_systemctl)

            

            #Update interval based on second
            tm.sleep(10)


            enum += 1


            if enum == 10:
            
                break 



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(("192.168.56.1", 54321))


Shell()


sock.close()







