#!/usr/bin/env python3
import ipdb

from classes.national_park import NationalPark
from classes.visitor import Visitor
from classes.trip import Trip

if __name__ == "__main__":
    print("HELLO! :) let's debug :vibing_potato:")

xtina = Visitor("xtina")
sean = Visitor("sean")
mary = Visitor("mary")

zion = NationalPark("zion")
yosemite = NationalPark("yosemite")

trip1 = Trip(xtina, yosemite, "11-5-22", "11-7-22")
trip2 = Trip(sean, yosemite, "11-5-22", "11-7-22")
trip3 = Trip(xtina, zion, "1-2-23", "2-2-23")
trip4 = Trip(sean, yosemite, "1-2-23", "2-2-23")
trip5 = Trip(mary, yosemite, "3-3-23", "3-4-23")

ipdb.set_trace()
