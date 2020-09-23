#!/usr/bin/env python3

#imports
import shutil
import os

#move to working dir
os.chdir("/home/student/mycode/")

#copy fileA to fileB
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

#copy dirA to dirB dirB is created if it didnt already exist
shutil.copytree("5g_research/", "5g_research_backup/")
