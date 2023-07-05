#!/usr/bin/env python3
""" Unpack raw images as produced by the libcamera-raw."""

import sys
import numpy as np
import numpy.testing
import unittest

def unpack_12bimage(raw: np.ndarray, stride: int, width: int,
    height: int = 0) -> np.ndarray:
    """ Unpack an raw image of 12bit pixels arranged in rows stride bytes wide
    into an image of 16bit pixels.

    Parameters:
        raw: ndarray
        stride: number of bytes in a row (i.e. math.ceil(width * 1.5))
        width: Number of columns in the image
        height: Number of rows in the image. Default of 0 means use as many rows as
          the data supports.

    Returns:
        ndarray
    """
    # image = np.frombuffer(byte_string, np.uint8)
    raw_rows = raw.reshape(-1, stride)
    if height == 0:
        height = raw_rows.shape[0]
    padding = (3 - (stride % 3)) % 3
    cols = ((stride + 2) // 3) * 2
    image = np.pad(raw.reshape(-1, stride), ((0,0), (0, padding)))

    image = image.reshape(-1,3)
    # b0 b1 b2 0
    # b3 b4 b5 0
    # b6 b7 b8 0
    image = np.hstack( (image, np.zeros((image.shape[0],1), dtype=np.uint8)) )
    image.dtype='<u4' # 'u' for unsigned int
    image = np.hstack( (image, np.zeros((image.shape[0],1), dtype=np.uint8)) )
    image[:,1] = (image[:,0] >> 12) & 0xfff
    image[:,0] = image[:,0] & 0xfff
    image = image.astype(np.uint16)
    image = image.reshape(-1, cols)

    return image[0:height, 0:width]

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '-t':
        sys.exit(unittest.main())
    print('arg0', sys.argv[0])
    # Get the first image from a rpi hq image 
    stride = 4056 * 3 / 2
    rows = 3040
    image = np.fromfile('/Users/castor/astro/raw-stuff/books.split.aa', np.uint8)





