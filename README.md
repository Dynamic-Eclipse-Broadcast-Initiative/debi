# debi
Dynamic Eclipse Broadcast Initiative

## Quick Start

If you are already familiar with using git through something like VS Code, or Git Desktop,
you can get the code from [https://github.com/Dynamic-Eclipse-Broadcast-Initiative/debi.git](here).
```
winget install --id Git.Git -e --source winget
git clone https://github.com/Dynamic-Eclipse-Broadcast-Initiative/debi.git
```
to fetch the scripts to your system.

Once you've fetched the scripts, you can update them with `git pull`


The target platform is Microsoft Windows.

## File Organization

We've set this up to produce a python 'package' called 'debi' which should
be a vehicle for installing things via pip (or maybe conda?).  However,
this doesn't necessarily provide a good way to get to the sharpcap files.

These will need to be put somewhere more accessible, through some other
mechanism. Maybe a customization of the setuptools installation.

