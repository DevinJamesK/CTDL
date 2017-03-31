#!/usr/bin/python3

import sys
import os
import requests
import json

def main():
    init()

def init():
    if not os.path.exists('./samples'):
        print ("Creating sample directory: ", end='')
        os.makedirs('./samples')
        print ("DONE")

    print ("Updating sample data: ", end='')
    r = requests.get('https://motian.indabamusic.com/samples')
    if (not r.status_code is 200):
        print("FAILED, Server Returned {0}".format(r.status_code))
        exit()
    print("DONE")

if __name__ == '__main__':
    main()
