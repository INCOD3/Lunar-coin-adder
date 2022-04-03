import os
import xml.etree.ElementTree as ET


# Path selection for us WSL users
def main():
    adder = input("Enter the Lunar coins number you want to add: ")
    if len(adder) != 2:
        print("Please enter a number larger than 10, exiting the program")
        exit(-1)
    
    path = r"C:\Program Files (x86)\Steam\userdata\[ENTER YOUR STEAMID3 here (only the number)]\632360\remote\UserProfiles"
    # Get all the user profile xmls
    for filename in os.listdir(path):
        if not (filename.endswith('.xml')): continue 
        print("[debug] found " + filename + "profile")
        fullname = os.path.join(path, filename)
        tree = ET.parse(fullname)

        # Add the desired amount of coins to the existing coin total
        coinsNode = tree.getroot().find("coins")                                             
        coins = int(coinsNode.text)
        coins += int(adder)
        print("[debug] added " + adder + " lunar coins to every profile")
        coinsNode.text = str(coins)
        print("[debug] wrote to the xml files")
        # Write back to the xml
        tree.write(fullname)
        
if __name__ == "__main__":
    main()
