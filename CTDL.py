#!/usr/bin/python3

import sys
import os
import requests
import json

def main():
    sampleData = init()

def init():
    # Creating our sample folder where our downloads will be stored
    if not os.path.exists('./samples'):
        print ("Creating sample directory if one doesn't exist: ", end='')
        os.makedirs('./samples')
        print ("DONE")

    # Pulling most current json sample data from below URL
    print ("Updating sample data to most current: ", end='')
    r = requests.get('https://motian.indabamusic.com/samples')
    if (not r.status_code is 200):
        print("FAILED, Server Returned {0}".format(r.status_code))
        exit()
    print("DONE")
    return r.json();

if __name__ == '__main__':
    main()
