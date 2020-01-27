#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import json
import re
from parsePopData import readPopularData
from parsePopData import scrapePopularData
from parsePopData import scrapeNewsData
from parsePopData import readNewsData

#User Menu
print("\n\t\t\t\t----------Welcome to Elijah's Movie Program----------\n")
print("\t\t\t\tDisclaimer: All movie data is obtained from www.IMDB.com\n")

print("1. Show me the most popular movies out right now\n\n")
print("2. Show me some movie news\n\n")

userSelection = input("Please select a number from the following options what information you are seeking: ")


#Get Most Popular Movies by rank on IMDB
if userSelection == "1":

    scrapePopularData()
    readPopularData()

#Get Movie News
elif userSelection == "2":
    
    scrapeNewsData()
    readNewsData()

elif userSelection != "1" or userSelection != "2":
    print("This is not a correct choice. Try again.\n")
