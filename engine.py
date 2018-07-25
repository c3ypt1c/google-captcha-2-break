#!/usr/bin/python3.6
import time #For timing
startLoad = time.time()

print ( "Creating imports...")
from selenium import webdriver #For the driver
from random import random #For the "human factor"
from selenium.webdriver.common.keys import Keys #For the return key (enter)
import os #For paths and files
import threading #For command stacks


print ( "Reading word file..." )
class Words:
    fileOp = open ( "words.txt" )
    words = fileOp.read().split("\n")
    fileOp.close()
    del fileOp

print ( "Creating methods..." )
class Methods:
    global avoidBotBehaviour
    avoidBotBehaviour = 1 #Set to 1 or 0 
    
    def HumanTyping(element, text, scale=0.33): #mimics human typing
        global avoidBotBehaviour
        for x in text:
            element.send_keys(x);
            time.sleep(random()*scale*avoidBotBehaviour)
            
    def SendMessage(element, message): #Types a message and presses enter
        print ( "Sending message:", message )
        Methods.HumanTyping(element, message+Keys.RETURN, scale=0.1)

    def nothing(a=None): #empty method
        pass

    def randomWord(wordList):
        return wordList[int(random()*len(wordList))]
    
class URL:
    class google:
        captchaTest = "https://www.google.com/recaptcha/api2/demo"

    targetFirst = []
    targetFirst.append(["https://www.google.com/",
                        "DO SEARCH",
                        {"elementID":"lst-ib",
                         "afterelementID":None}
                        ])
    googleTrackedWebsites = []

class Config:
    searchIterations = 1#0
    wordDeepness = 2

endLoad = time.time()
#quit()
print ( "Took ", endLoad - startLoad, "s to load methods", sep="" )

print ( "Loading driver..." )
driver = webdriver.Firefox(os.getcwd());
print ( "Trying to generate convincing cookies..." )
for link in URL.targetFirst:
    print ( "Loading", link[0], "..." )
    driver.get(link[0])
    if link[1] == "DO SEARCH":
        print ( "Starting first search" )
        
        driver.find_element_by_id(link[2]["elementID"]).click()
        Methods.SendMessage(driver.find_element_by_id(link[2]["elementID"]),
                "".join( [ Methods.randomWord(Words.words) + " " for _ in range(Config.wordDeepness) ] ) )
        
        for iteration in range(Config.searchIterations):
            print ( "Iteration of random search: ", iteration + 1, "/",Config.searchIterations,"...", sep="" )
            
            ##driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #Scrolling if necesary
            
    else:
        print ( "ERROR" )

print ( "Clicking robot box" )

