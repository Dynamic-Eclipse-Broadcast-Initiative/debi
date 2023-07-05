#!/usr/bin/env python3

import numpy as np
import numpy.testing
import unittest
import unpack12

class TestUnpackCases(unittest.TestCase):
    
    def test_unpack_12bimage_stride_commensurate(self):
        np.set_printoptions(formatter={'int':hex})
        t1 = np.array([0x10, 0x32, 0x54, 0x76, 0x98, 0xba], dtype=np.uint8)
        want1 = np.array([ [0x210, 0x543], [0x876, 0xba9]], dtype=np.uint16)
        got1 = unpack12.unpack_12bimage(t1, 3, 2, 2)
        self.assertEqual(got1.dtype, np.uint16)
        self.assertEqual(got1.shape, (2, 2))
        np.testing.assert_array_equal(got1, want1)

    def test_unpack_12bimage_stride_ex1(self):
        t1 = np.array([0x10, 0x2, 0x43, 0x5], dtype=np.uint8)
        want = np.array([[0x210], [0x543]], dtype=np.uint16)
        got = unpack12.unpack_12bimage(t1, 2, 1, 2)
        np.testing.assert_array_equal(got, want)

    def test_unpack_12bimage_stride_pad(self):
        t1 = np.array([0x10, 0x2, 0, 0x43, 0x5, 0], dtype=np.uint8)
        want = np.array([[0x210], [0x543]], dtype=np.uint16)
        got = unpack12.unpack_12bimage(t1, 3, 1, 2)
        np.testing.assert_array_equal(got, want)

    def test_unpack_12bimage_stride_pad2(self):
        t1 = np.array([0x10, 0x2, 0, 0, 0x43, 0x5, 0, 0], dtype=np.uint8)
        want = np.array([[0x210], [0x543]], dtype=np.uint16)
        got = unpack12.unpack_12bimage(t1, 4, 1, 2)
        np.testing.assert_array_equal(got, want)

if __name__ == "__main__":
    unittest.main()

