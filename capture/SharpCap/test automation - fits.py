# This script is written for SharpCap's IronPython interpreter
# You must have the Pro version sharpcap ($18/year) to use this script.
#
import time
import os
SharpCap.SelectedCamera.Controls.OutputFormat.Value= "FITS files (*.fits)"
SharpCap.Settings.CaptureFolder = r'C:\Users\bill\Desktop\tests'

for q in range (0,360): 
#
	SharpCap.TargetName = "test_1.3ms"
	SharpCap.SelectedCamera.Controls.Exposure.ExposureMs = 1.3
	SharpCap.SelectedCamera.CaptureSingleFrame()
	SharpCap.TargetName = "test_13ms"
	SharpCap.SelectedCamera.Controls.Exposure.ExposureMs = 13.0
	SharpCap.SelectedCamera.CaptureSingleFrame()
	SharpCap.TargetName = "test_130ms"
	SharpCap.SelectedCamera.Controls.Exposure.ExposureMs = 130.0
	SharpCap.SelectedCamera.CaptureSingleFrame()
	SharpCap.TargetName = "test_1300ms"
	SharpCap.SelectedCamera.Controls.Exposure.ExposureMs = 1300
	SharpCap.SelectedCamera.CaptureSingleFrame()       
