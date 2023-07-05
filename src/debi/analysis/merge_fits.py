#!/usr/bin/env python

import glob
import sys

from  astropy.io import fits
import cv2 as cv
import numpy as np
import re

# FITS cards
FC_BAYERPAT = 'BAYERPAT'
FC_BITPIX = 'BITPIX'
FC_EXPTIME = 'EXPTIME'
FC_FILTPAT = 'FILT-PAT'

def fitsread(name) -> (cv.Mat, fits.header.Header):
    """Open a path to a fits file, for use with OpenCV.

    Args:
        name: str, file-like or pathlib.Path (like fits.io.open)
            File to be opened.

    Returns:
        Tuple of matrix and header
    """
    hdul = fits.open(name)
    if len(hdul) != 1:
        raise NotImplemented("Only supports single FITS HDU for now.")
    primary = hdul[0]

    # With raw images we may have bayer patterns to register.
    # For now we support only the sharpcap monochrome format.
    return (cv.Mat(primary.data), primary.header)


# This is designed to work with the FITS files generated
# by Sharpcap as a sequence of multiple exposures.

# So we start with a FITS file with only one HDU

def merge_fits(fitsnames, outjpeg, gamma=4.0):
    """Create an HDR jpeg from a list of fits files using OpenCV Debevec merge."""
    image_list = []
    exp_list = []
    for f in fitsnames:
        (image, header) = fitsread(f)
        # XXX assumes monochrome for now.
        rescaled = primary.data/256
        truncated = rescaled.astype('uint8')
        datau8 = cv.Mat(truncated)
        # cvtColor generates a warning: "processing of multi-channel arrays might be changed in the future"
        cvin = cv.cvtColor(datau8, cv.COLOR_GRAY2BGR)
        image_list.append(cvin)
        exp_list.append(primary.header['EXPTIME'])
    exposure_times = np.array(exp_list, dtype=np.float32)
    merge_images(image_list, exposure_times, outjpeg, gamma)

def merge_tifs(tifnames, outjpeg, gamma=4.0):
    """Merge sharpcap-captured TIFF files into an HDR jpeg."""
    image_list = []
    exp_list = []
    for f in tifnames:
        image_list.append(cv.imread(f))
        m = re.search(r'([0-9.]*)ms', f)
        if not m:
            raise ValueError(f'Exposure Time not matched: {f}')
        exp_list.append(float(m.group(1)))
    exposure_times = np.array(exp_list, dtype=np.float32)
    merge_images(image_list, exposure_times, outjpeg, gamma)


def merge_images(image_list, exposures, outfile, gamma):
    """Merge an image list / exposure list into a single image.

    image_list: list of CV_U8 BGR images,  consistent with OpenCV.
    exposure_list: ndarray of exposure times, np.float32
    outfile: text filename of destination image (e.g. jpeg)
    gamma: nonlinear image luminance factor (e.g. 4)

    The OpenCV merge_debevec function is relatively limited,
    but we'll take what we can get.
    """

    merge_debevec = cv.createMergeDebevec()
    hdr_debevec = merge_debevec.process(image_list, times=exposures)
    tonemap1 = cv.createTonemap(gamma=gamma)
    res_debevec = tonemap1.process(hdr_debevec.copy())
    res_debevec_8bit = np.clip(res_debevec * 255, 0, 255).astype('uint8')
    cv.imwrite(outfile, res_debevec_8bit)

if __name__ == "__main__":
    files = sys.argv[1:]
    merge_fits(files, '/tmp/fitsmerg.jpg')
