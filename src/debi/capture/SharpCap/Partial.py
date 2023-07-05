# Capture .ser files with single.png for "ser_time" seconds at 1000x1000 resolution
#
# Uses user settings for exposure and gain
# Forces resolution, binning, colour space
# Returns to users resolution
#####################################################################################

import time

ser_time = 5 #.ser collection duration in seconds at users exposure

str_date = time.strftime("%d%b%Y",time.gmtime())
path = r'C:\DEB\\'+str_date+r'\Partial' # path for main capture folder

str_time = time.strftime("%H%M%S",time.gmtime())

### Initial Setup ####################################################################
SharpCap.SelectedCamera.LiveView = False
SharpCap.Settings.UseSubFolders = False
SharpCap.Settings.CaptureFolder = path
SharpCap.TargetName = 'partial_'+str_time
#This part can be handled in settings of SharpCap
SharpCap.Settings.UseManualTemplates = True # still need this if handled in settings
SharpCap.Settings.ManualSequenceTemplate = '{TargetName}_{Exposure}'
SharpCap.Settings.ManualSingleFileTemplate = '{TargetName}_{Exposure}'
#
SharpCap.SelectedCamera = SharpCap.Cameras[0]

#reset values for returning at end of collection
reset_area = SharpCap.SelectedCamera.Controls.Resolution.Value

#Force values
SharpCap.SelectedCamera.Controls.Binning.Value = '1'
SharpCap.SelectedCamera.Controls.OutputFormat.Automatic = False
SharpCap.SelectedCamera.Controls.ColourSpace.Value = 'MONO16'
SharpCap.SelectedCamera.Controls.Resolution.Value = '1000x1000'

### Capture images ####################################################################
SharpCap.SelectedCamera.Controls.OutputFormat.Value = 'PNG file (*.png)'
SharpCap.SelectedCamera.CaptureSingleFrame()

SharpCap.SelectedCamera.LiveView = True
SharpCap.SelectedCamera.Controls.OutputFormat.Value = 'SER file (*.ser)'
SharpCap.SelectedCamera.PrepareToCapture()
SharpCap.SelectedCamera.RunCapture()
time.sleep(ser_time)
SharpCap.SelectedCamera.StopCapture()

### Reset resolution ###################################################################
SharpCap.SelectedCamera.Controls.Resolution.Value = reset_area
SharpCap.Settings.UseManualTemplates = False

# END OF PROGRAM
