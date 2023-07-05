# SharpCap ASI178 Demo Notes ReadMe #

This ReadMe file details the included two SharpCap Python scripts
(test automation  fits.py and test automation  tiffs.py) and one
SharpCap Sequence file (SharpCapDemoSequence.scs).

IMPORTANT: These files were tailored for Bill Kloeppings laptop.
These files must be modified to be usable on other systems.
Modifications can be easily performed from within SharpCap.

## Description of files ##
*test automation  fits.py* sets the file output format to
.fits files and specifies the SharpCap capture folder destination
(on the local drive) then starts taking a continual sequence of 4
exposures  one each at 1.3 ms, 13 ms, 130 ms and 1300 ms; setting
the target file name to indicate the set exposure prior to capturing
each image.

*test automation  tiffs.py* sets the file output format to
tiff files and specifies the SharpCap capture folder destination
(to a remote G: drive) and then takes four images, one each at 1.3
ms, 13 ms, 130 ms and 1300 ms; setting the target file name to
indicate the set exposure prior to capturing each image. After the
4 images have been taken the script renames the SharpCap capture
folder destination to the local drive location used in the test
automation fits.py script and then the script terminates.

The ‘SharpCapDemoSequence.scs’ sequence file does the following:
- Opens the ZWO ASI178MM camera
- Loads the camera profile ‘Lunar Eclipse (ZWO ASI178MM)’
- Sets the Color Space to ‘Mono16’
- Sets the Resolution to 3096x2080 (full resolution)
- Sets the Gain to 0
- Sets the Binning to 1
- Sets Time Stamp Frames to ON
- Sets Output Format to FITS files (*.fits)
- Sets the camera to ‘Still Mode’
- Repeats the following sequence 5 times:
  * Runs the script ‘test automation – fits.py’ for 1 minute
  * Delay for 2 seconds
  * Runs the script ‘test automation – tiffs.py’
- When the sequence (5 iterations) is complete the Alert sound is
  played and the sequence terminates.

When the sequence is executed in SharpCap it will take one minutes
worth of high speed .fits images of the 4 exposures (roughly 80-88
images in total) and stores them on the local drive then takes 4
.tiff images at the same 4 exposures and stores them on the remote
drive (e.g.  Google drive) and then will repeat the sequence the
set number of times (5).

## Modifying the files to your system ##
1. Modify the test automation  fits.py script by opening it in the
    SharpCap script console and change the following:
  - Change the SharpCap.Settings.CaptureFolder line to replace
    “r’C:\Users\...” to point to a folder on YOUR local drive
  - Optionally: Change the SharpCap.TargetName values to whatever you want the file
    names to be titled.
  - Save the script when modification is complete
2. Modify the ‘test automation – tiffs.py’ script by opening it in the SharpCap script console and
   change the following:
  - Change the SharpCap.Settings.CaptureFolder line to replace “r”G:\My Drive\...” to
    point to a folder on the Deb Google drive that you want to use.
    Note that this assumes that you have mapped the Deb Google drive
    to your system.
  - Optionally: Change the SharpCap.TargetName values to whatever you want the file
    names to be titled.
  - Change the last SharpCap.Settings.CaptureFolder line at end of script to replace
    “r’C:\Users\...” to point to the same folder on YOUR local drive that you specified in
    the ‘test automation – fits.py’ script
  - Save the script when modification is complete
3. Modify the ‘SharpCapDemoSequence.scs’ file by opening it in the
    SharpCap Sequence Editor (Sequence-Edit...) and change the following:
  - Change the Load Camera Profile to point to the profile on
    YOUR system that you wish to use. Click on the Load Camera
    Profile line in the Sequence and a list of available profiles
    on your system is provided in the right hand Selected Step
    Properties panel drop down. Note that you must have the ASI178
    connected to your computer for the available profiles to be
    listed.
  - Change the ‘Repeat 5 times’ line to repeat however many times you wish the
    sequence to run. (Click on the Repeat box in the Sequence and then change the
    Repeat Count in the Selected Step Properties panel on the right)
  - Change the location of the two python scripts to specify the full location of where
    the scripts reside on YOUR system.(Click on the ‘Run the python script...’ line in the
    Sequence then hit the ‘...’ box in the Selected Step Properties panel on right to
    specify the location of the appropriate script to use.)
  - Save the Sequence when modification is complete.

Test your modifications to ensure you haven’t made any errors.

Hope this information helps you to adapt these files to your system setup.
