#!/usr/bin/env python

#########################################
#Created by: Poterman
#Date: 22/09/19
#Purpose: Hello World script which handles given parameters and disallow root from running this script.
#Version: 0.0.1
#########################################

#Importing User Info
import getpass
username = getpass.getuser()

#Main
if username == root
    print ("Root user is unallowed to run this script, exiting..."")
    sleep 5
    exit 1
elif username != root
    print ("Hello username")
    sleep 5
    exit 0
