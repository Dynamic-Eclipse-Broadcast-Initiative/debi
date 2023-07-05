# Capture of different exposures for number of sets of exposures,
#                                    time of run
#                                    or continuous loop of sets
# Camera in Still Mode for captures
# resets to Live mode with original exposure/gain/resolution after run
#           
# Authors:  Chris Mandrell
#           Matt Penn
#           Castor Fu
# Written: 3/20/2023
# Last Edit: 5/15/2023 CM
#####################################################################################

import time 

### List of variables to be changed by user (User Input) #########################################
path = r'C:\DEB\Totality\totality' # path for capture folder

between_set = 0.0 # time between sets of exposures in exposure List (seconds)

exposure = ( 0.4, 4.0, 40.0, 400.0, 4000.0 ) # exposure tuple (ms)

use_duration = True # Allow capture control by time
duration = 10.0 # time in seconds - full pass of exposures even if over time

use_maxcount = False # Allow capture control by # of iterations of exposure list
maxcount = 2 # number of iterations of exposures list
### WARNING!!! if use_duration and use_maxcount BOTH True capture will terminate with shortest collection
# Note: if Time and Control both False capture will run in infinite loop until manually stopped

suppress_settings_file = True # suppress camera settings data files after first iteration of captures
#####################################################################################

### Function to take images #########################################################
def Image(exposure):

    for x in exposure:
       
        SharpCap.SelectedCamera.Controls.Exposure.ExposureMs = x
        local_time = time.localtime()
        str_time = time.strftime("%H%M%S",local_time)
        SharpCap.SelectedCamera.CaptureSingleFrameTo(path+"_"+str_time+"_"+str(x)+"ms"+".tif")      
######################################################################################    

### Initial Setup ####################################################################
SharpCap.SelectedCamera = SharpCap.Cameras[0]
SharpCap.SelectedCamera.LiveView = False

#reset values for returning to live mode at end of collection
reset_exp = SharpCap.SelectedCamera.Controls.Exposure.Value
reset_area = SharpCap.SelectedCamera.Controls.Resolution.Value
reset_gain = SharpCap.SelectedCamera.Controls.Gain.Value

#Forced values 
SharpCap.SelectedCamera.Controls.Binning.Value = '1'
SharpCap.SelectedCamera.Controls.OutputFormat.Automatic = False
SharpCap.SelectedCamera.Controls.OutputFormat.Value = 'TIFF files (*.tif)'
SharpCap.SelectedCamera.Controls.ColourSpace.Value = 'MONO16'
#Opting for selecting from max of available resolutions instead of hardcoding value that might not exist
#SharpCap.SelectedCamera.Controls.Resolution.Value = '3096x2078'
SharpCap.SelectedCamera.Controls.Resolution.Value = SharpCap.SelectedCamera.Controls.Resolution.AvailableValues[0]
SharpCap.SelectedCamera.Controls.Gain.Value = '50'
######################################################################################

### Capture images ####################################################################
start = time.time()
i = 1

while True:
        
    if (i > maxcount and use_maxcount) or ((time.time()-start) > duration and use_duration):
        break
    
    Image(exposure)
    if suppress_settings_file:
        SharpCap.Settings.CreateCameraSettingsFile = False 
        
    time.sleep(between_set)
    i+=1        
#######################################################################################

### Reset SharpCap to live mode with appropriate exposure #############################
SharpCap.Settings.CreateCameraSettingsFile = True   
SharpCap.SelectedCamera.LiveView = True
SharpCap.SelectedCamera.Controls.Resolution.Value = reset_area 
SharpCap.SelectedCamera.Controls.Gain.Value = reset_gain 
SharpCap.SelectedCamera.Controls.Exposure.Value = reset_exp 
#######################################################################################


### END OF PROGRAM ####################################################################

'''
EDITS:

3/24/2023   CM  :   Fix bugs with running as Count
4/4/2023    CM  :   Add hardcoded camera settings in initial setup
                    Added reset values for Exposure/Resolution/Gain for returning to live mode
                    Moved run_name variable to User input section
                    
                  
5/15/2023   CM  :   Changed naming convention by switching to CaptureSingleFrameTo and adding editing of time
                    Removed "Time between exposure" options
                    Removed clutter around naming convention
                    change flag names to more appropriate python
                    combine three capture loops into single infinite loop
'''
