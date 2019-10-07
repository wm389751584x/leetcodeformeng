#! /usr/bin/env python  //what interpreter to use
# -*- coding: utf-8 -*-
"""
Simple dice roller example.

Converted to Python3...
"""

import random

min = 1
max = 6

roll_again = False

while roll_again == "yes" or roll_again == "y":
    print("Starting with", max, "sided dice.")
    roller = int(input("How many dice should I roll? "))
    print("Rolling the dice...")
    print("Let me roll those " + str(roller) + " dice for you!")
    print("The values are...")
    while roller > 0:
        value = (random.randint(min, max))
        print(str(value) + ", ", end="", flush=True)
        roller -= 1

    roll_again = str.lower(input("\nRoll the dice again? "))