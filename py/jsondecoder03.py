#!/usr/bin/env python3

# json is part of the standard library
import json

def main():
    ## open the file
    with open("datacenter.json", "r") as datacenter:
        datacenterstring = datacenter.read()
    
    ## display our decoded string
    print(datacenterstring)
    print(type(datacenterstring))
    
    ## pause the program to allow for inspection
    print("\nThe code above is string data. Python cannot easily work with this data.")
    input("Press Enter to continue")            
    
    ## Create the json string
    datacenterdecoded = json.loads(datacenterstring)
    
    ## This is now a dictionary
    print(type(datacenterdecoded))
    
    ## display the servers in row1
    print(datacenterdecoded["row1"])
    
    ## display the servers in row3
    print(datacenterdecoded["row3"])
    
    ## display the 2nd server in row2
    print(datacenterdecoded["row2"][1])
                
main()
