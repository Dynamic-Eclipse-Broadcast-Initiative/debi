# This is based on Jeff O's version 3 script.
# It's written for sharpcap's IronPython interpreter
# You must have the Pro version sharpcap ($8/year) to use it.


# set Output format to FITS
# set colour space to mono6
# 8 bit will not work
# set capture area to Full Sensor
# set binning to 
# You Must Have Google Desktop G:\Drive setup for this script to work https://www.google.com/drive/download/
# This script writes to LiveTest LunarEclipse8222 folder
# Please replace Observer___ with Observer"Your Initials Here"_
# In SharpCap settings it is best to remove all formatting to your fits file naming or you will create multiple sub_folders on the DEB drive
# **** New File and Folder name ****
# Updated __222 I changed the date to *** 8222 *** from 7222
# Updated _6_222
# **** This is Four Second Exposures Only ****


import time
import os

for q in range (,36):
    print("4s File4 has been created")    
    SharpCap.SelectedCamera.Controls.Exposure.ExposureMs = 4.
    SharpCap.Settings.CaptureFolder = r'G:\.shortcut-targets-by-id\m-ssz9RCqSrkBxhFcc3yI-IHx8j3su\LiveTests\LunarEclipse8222'
    SharpCap.TargetName = "Observer_JMW_LunarEclipse8222_4s"
    SharpCap.SelectedCamera.CaptureSingleFrame()       
    
    while True:
      if not SharpCap.SelectedCamera.Capturing :
        break
      time.sleep(.) 
    time.sleep(8.8)