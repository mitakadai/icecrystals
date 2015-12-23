# -*- coding: utf-8 -*-

import time

from icecrystals import IceCrystals

def main():
    snowflake = IceCrystals(0)
    for i in range(100):
        print(snowflake.generate())

main()

