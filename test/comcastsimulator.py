#!/usr/bin/env python3
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

FUN_BIKE_URL = 'https://ucsdfunbike.github.io/funBike/'


def main():
   driver = webdriver.Firefox()
   driver.get( FUN_BIKE_URL )
   time.sleep(20)
   driver.close()
    # my code here

if __name__ == "__main__":
   main()


