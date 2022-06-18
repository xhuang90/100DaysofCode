# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# @time: 2022-06-19 00:06
# @author: Hobey Wong
# @contact: hobey0712@gmail.com
# @file: main.py
# @desc:

# 1. Create a greeting for your program
print('Welcome to the Band Name Generator')

# 2. Ask the user for the city that they grew up in.
grew_up_city = input("What's name of the city you grew up in?\n")

# 3. Ask the user for the name of a pet.
pet_name = input("What's your pet's name?\n")

# 4. Combine the name of their city and pet and show them their band name.
band_name = grew_up_city + ' ' + pet_name
print('Your band name should be', band_name)
