#!/usr/bin/env python3

#Import statements: Noteable packages are BeautifulSoup which is chiefly used as an HTML Parser,
#The requests package which handles HTTP requests to get web page file code, json which handles data saving/formatting,
#And the re package, which is used for the use of Regular Expressions

from bs4 import BeautifulSoup
import requests
import json
import re
from parsePopData import readPopularData
from parsePopData import scrapePopularData
from parsePopData import scrapeNewsData
from parsePopData import readNewsData

#User Menu showing two choices for now: Most popular movies in list format or current movie news
print("\n\t\t\t\t----------Welcome to Elijah's Movie Program----------\n")
print("\t\t\t\tDisclaimer: All movie data is obtained from www.IMDB.com\n")

print("1. Show me the most popular movies out right now\n\n")
print("2. Show me some movie news\n\n")

#Get user selection
userSelection = input("Please select a number from the following options what information you are seeking: ")


#Get Most Popular Movies by rank on IMDB
if userSelection == "1":

    scrapePopularData()
    readPopularData()

#Get Movie News
elif userSelection == "2":
    
    scrapeNewsData()
    readNewsData()

#Lightweight validation for correct user input
elif userSelection != "1" or userSelection != "2":
    print("This is not a correct choice. Try again.\n")
