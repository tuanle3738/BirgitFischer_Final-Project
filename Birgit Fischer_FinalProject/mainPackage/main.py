# Name: Noah Kathman, Kevin Skiba, Alex Fisher, Tuan Le
# email: kathmans@mail.uc.edu, le2te@mail.uc.edu, fisheav@mail.uc.edu, skibakm@mail.uc.edu
# Assignment Title: Final Project
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: This project demonstrates that I can use Eclipse to create a PyDev project to decrypt a JSON file
# Citations:
# Anything else that's relevant:

# main.py

from functionsPackage.functions import *

extractData() # call the function to extract the json file

data_list = ['22147', '29029', '28011', '20392', '45608', '105654', '28894', '20392', '21723', '31471']

decrypted_location = decryptLocation(data_list) # call the function to decrypt the location data
print(decrypted_location)

display_image('group_picture.jpg') # show the taken image
