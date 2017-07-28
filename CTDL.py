#!/usr/local/bin/python3

import sys
import os
import requests
import json

def main():
    sampleData = init()
    totalSampleCount = len(sampleData)

    print("Total number of samples found: {0}".format(totalSampleCount))
    print("Enter numers on left to select options.")

    while (True):
        try:
            f = input("0: Quit\n1: Download ALL\n2: See filter options\n")
            int(f)
        except ValueError:
            print("Invalid input! Please try again. (1/2)")
            continue

        if (f == 0):
            break
        elif (f == 1):
            print("Downloading ALL {0} samples: ".format(len))
            downloadSamples(sampleData, 0)
            break
        elif (f == 2):
            print("Filter options: ")
            showFilters(sampleData)
            break
        else:
            print("Selection {0} not available (1/2)".format(f))


def init():
    # Creating our sample folder where our downloads will be stored
    print("Creating sample directory if one doesn't exist: ", end='')

    if not os.path.exists('./samples'):
        os.makedirs('./samples')

    print("DONE")

    # Pulling most current json sample data from below URL
    print("Updating sample data to most current: ", end='')
    r = requests.get('https://motian.indabamusic.com/samples')
    if (not r.status_code is 200):
        print("FAILED, Server Returned {0}".format(r.status_code))
        exit()
    print("DONE")
    return r.json()

def showFilters(sampleData):
    print("Showing Filters: ")

def downloadSamples(sampleData, f):
    if (f is 0):
        print("Downloading ALL {0} samples".format(len(sampleData)))

if __name__ == '__main__':
    main()
