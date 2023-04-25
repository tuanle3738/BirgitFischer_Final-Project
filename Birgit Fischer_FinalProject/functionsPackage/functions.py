# Name: Noah Kathman, Kevin Skiba, Alex Fisher, Tuan Le
# email: kathmans@mail.uc.edu, le2te@mail.uc.edu, fisheav@mail.uc.edu, skibakm@mail.uc.edu
# Assignment Title: Final Project
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: This project demonstrates that I can use Eclipse to create a PyDev project to decrypt a JSON file
# Citations:
# Anything else that's relevant:

# functions.py

import json
import numpy as np
from PIL import Image

def extractData(): # extract data from JSON file
    with open('Encrypted_Group_Hints_Spring_2023_Section_001.json') as jsonFile:
        data = json.load(jsonFile)
        dataArray = np.array([])
        for num in data['Birgit Fischer']:
            dataArray = np.append(dataArray, num)
        print(dataArray)
        
def decryptLocation(data_list): # decrypt location data and return it
    decrypted = ''
    with open('english.txt', 'r') as file:
        lines = file.readlines()
        for index in data_list:
            line_number = int(index) - 1  # Adjusting index to 0-based
            if line_number < len(lines):
                decrypted += lines[line_number].strip() + ' '
    decrypted = decrypted.strip()
    return decrypted

def display_image(image):
    # Open the image file
    img = Image.open(image)
    # Show the image
    img.show()





