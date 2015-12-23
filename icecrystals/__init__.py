# -*- coding: utf-8 -*-

# The MIT License (MIT)
#
# Copyright (c) 2015 mitakadai
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

VERSION = '0.1'

import time

class IceCrystals:

    def __init__(self, machine_id, epoch=0, init_serial_no=0):
        self._machine_id = machine_id
        self._epoch = epoch
        self._serial_no = init_serial_no

    def generate(self):
        unique_id = (
            ((int(time.time() * 1000) - self._epoch) & 0x1ffffffffff) << 22 |
            (self._machine_id & 0x3ff) << 12 |
            (self._serial_no & 0xfff)
            )
        self._serial_no += 1
        return unique_id

