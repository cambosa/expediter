#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Install dependencies
# $ pip install -r requirements.txt

# Firefox webdriver
# https://github.com/mozilla/geckodriver/releases

"""
Purpose:    Organize evaluator notes IAW "Eval Worksheet Area Grade" categories,
            and stage notes for PEX data entry

Usage:      Verify this script is in the same current working directory of the target file, then run:

            python3 expeditor.py

            1. When prompted, enter the filename of your evaluator notes
            2. Take note of the URL generated (displayed in green)
            3. Login to PEX, navigate to the URL in another browser window, and copy/paste data
"""
import re
from string import digits
import time
import http.server
import socketserver
import threading
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'


# Prompts user to specify target filename.
# Note: Supplying a filepath will cause an error with the SimpleHTTPServer autonomous navigation later on.
filename = input(f"\n{bcolors.WARNING}[USER]" + f"\tEnter the target filename with extension (e.g. lastname_notes.txt):{bcolors.ENDC}" + f"\n\t=> ")
# Console notification of file format task starting
print(f"\n{bcolors.OKGREEN}[ OK ]{bcolors.ENDC}" + f"\tTARGET ACQUIRED: Processing " + filename + f" into PEX format...\n")
# Create timestamp
timestr = time.strftime("%Y%m%d-%H%M%S")
# Create outfile filename with timestamp data
outfile_filename = timestr + ".txt"
result_filename = str(outfile_filename)
print(result_filename)

def sort_area_101():
    with open(filename, 'rt') as f:
        lines = f.readlines()
        with open(outfile_filename, "a") as outfile:
            outfile.write(f"PRE-SORTIE ACTIONS\n")
        for line in sorted(lines):
            if re.search(r'101', line):
                sliced101 = line[3:]
                with open(outfile_filename, "a") as outfile:
                    outfile.write(f'\t' + sliced101)
                outfile.close()
    f.close()

def sort_area_102():
    with open(filename, 'rt') as f:
        lines = f.readlines()
        with open(outfile_filename, "a") as outfile:
            outfile.write(f"CREW COORDINATION\n")
        for line in sorted(lines):
            if re.search(r'102', line):
                sliced102 = line[3:]
                with open(outfile_filename, "a") as outfile:
                    outfile.write(f'\t' + sliced102)
                outfile.close()
    f.close()

def sort_area_103():
    with open(filename, 'rt') as f:
        lines = f.readlines()
        with open(outfile_filename, "a") as outfile:
            outfile.write(f"SAFETY/EMERGENCY PROCEDURES\n")
        for line in sorted(lines):
            if re.search(r'103', line):
                sliced103 = line[3:]
                with open(outfile_filename, "a") as outfile:
                    outfile.write(f'\t' + sliced103)
                outfile.close()
    f.close()

def sort_area_104():
    with open(filename, 'rt') as f:
        lines = f.readlines()
        with open(outfile_filename, "a") as outfile:
            outfile.write(f"CREW DISCIPLINE\n")
        for line in sorted(lines):
            if re.search(r'104', line):
                sliced104 = line[3:]
                with open(outfile_filename, "a") as outfile:
                    outfile.write(f'\t' + sliced104)
                outfile.close()
    f.close()

def sort_area_105():
    with open(filename, 'rt') as f:
        lines = f.readlines()
        with open(outfile_filename, "a") as outfile:
            outfile.write(f"SITUATIONAL AWARENESS\n")
        for line in sorted(lines):
            if re.search(r'105', line):
                sliced105 = line[3:]
                with open(outfile_filename, "a") as outfile:
                    outfile.write(f'\t' + sliced105)
                outfile.close()
    f.close()

def sort_area_106():
    with open(filename, 'rt') as f:
        lines = f.readlines()
        with open(outfile_filename, "a") as outfile:
            outfile.write(f"WEAPON SYSTEM OPERATIONS\n")
        for line in sorted(lines):
            if re.search(r'106', line):
                sliced106 = line[3:]
                with open(outfile_filename, "a") as outfile:
                    outfile.write(f'\t' + sliced106)
                outfile.close()
    f.close()

def sort_area_107():
    with open(filename, 'rt') as f:
        lines = f.readlines()
        with open(outfile_filename, "a") as outfile:
            outfile.write(f"BASIC HOST OPERATIONS\n")
        for line in sorted(lines):
            if re.search(r'107', line):
                sliced107 = line[3:]
                with open(outfile_filename, "a") as outfile:
                    outfile.write(f'\t' + sliced107)
                outfile.close()
    f.close()

def sort_area_108():
    with open(filename, 'rt') as f:
        lines = f.readlines()
        with open(outfile_filename, "a") as outfile:
            outfile.write(f"BASIC NETWORK OPERATIONS\n")
        for line in sorted(lines):
            if re.search(r'108', line):
                sliced108 = line[3:]
                with open(outfile_filename, "a") as outfile:
                    outfile.write(f'\t' + sliced108)
                outfile.close()
    f.close()

def sort_area_109():
    with open(filename, 'rt') as f:
        lines = f.readlines()
        with open(outfile_filename, "a") as outfile:
            outfile.write(f"BASIC CYBER SECURITY\n")
        for line in sorted(lines):
            if re.search(r'109', line):
                sliced109 = line[3:]
                with open(outfile_filename, "a") as outfile:
                    outfile.write(f'\t' + sliced109)
                outfile.close()
    f.close()

def sort_area_110():
    with open(filename, 'rt') as f:
        lines = f.readlines()
        with open(outfile_filename, "a") as outfile:
            outfile.write(f"POST-SORTIE/MISSION ACTIONS\n")
        for line in sorted(lines):
            if re.search(r'110', line):
                sliced110 = line[3:]
                with open(outfile_filename, "a") as outfile:
                    outfile.write(f'\t' + sliced110)
                outfile.close()
    f.close()

def sort_area_111():
    with open(filename, 'rt') as f:
        lines = f.readlines()
        with open(outfile_filename, "a") as outfile:
            outfile.write(f"DEBRIEF\n")
        for line in sorted(lines):
            if re.search(r'111', line):
                sliced111 = line[3:]
                with open(outfile_filename, "a") as outfile:
                    outfile.write(f'\t' + sliced111)
                outfile.close()
    f.close()

# Sort file IAW "Eval Worksheet Area Grade" categories for PEX entry
def pex_format():
    sort_area_101()
    sort_area_102()
    sort_area_103()
    sort_area_104()
    sort_area_105()
    sort_area_106()
    sort_area_107()
    sort_area_108()
    sort_area_109()
    sort_area_110()
    sort_area_111()
pex_format()
# Console notification of task completion
print(f"\n{bcolors.OKGREEN}[ OK ]{bcolors.ENDC}" + f"\tFormatting complete")

# Start the driver
driver = webdriver.Firefox()
# Navigate to pastebin
pastebin = 'https://psty.io/new'
print(f"{bcolors.OKGREEN}[ OK ]{bcolors.ENDC}" + "\tOpening browser")
driver.get(pastebin)
# Store the ID of the original window
original_window = driver.current_window_handle
# Check that we don't have other windows open already
assert len(driver.window_handles) == 1

# Start a HTTP server
PORT = 8000
def initiate_server():
    handler = http.server.SimpleHTTPRequestHandler

    class MyTCPServer(socketserver.TCPServer):
        def server_bind(self):
            import socket
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.bind(self.server_address)

    server_address = ('', PORT)
    httpd = MyTCPServer(server_address, handler)
    try:
        # Console notification of server activation
        print(f"{bcolors.OKGREEN}[ OK ]{bcolors.ENDC}" + "\tServer started at localhost:" + str(PORT))
        httpd.serve_forever()
    except KeyboardInterrupt:
        # Console notification of user-prompted SIGINT (e.g. Ctrl + C)
        print(f"{bcolors.WARNING}[WARN] {bcolors.BOLD}Signal Interrupt{bcolors.ENDC}")
        pass
    finally:
        httpd.server_close()
        # Console notification of server kill command succeeding
        print(f"{bcolors.FAIL}[WARN] {bcolors.BOLD}HTTP server was killed in action{bcolors.ENDC}")

threading.Thread(target=initiate_server).start()

# Start the driver
driver2 = webdriver.Firefox()
# Navigate to HTTP server
driver2.get('localhost:' + str(PORT) + "/" + result_filename)
# Select/copy text from "notes.txt"
element = driver2.find_element_by_tag_name("body")
element.send_keys(Keys.CONTROL, "a")
element.send_keys(Keys.CONTROL, "c")

for window_handle in driver.window_handles:
    if window_handle != original_window:
        # Switch to original window 
        driver2.switch_to_window(original_window)
        break

# Paste text
element2 = driver.find_element_by_name("code")
element2.send_keys(Keys.CONTROL, "v")
# Submit text
submit = driver.find_element_by_css_selector('#submit').click()
# Close browser of HTTP server
driver2.close()
# Get current URL
url = str(driver.current_url)
# Console notification with pastebin hyperlink
print(f"{bcolors.OKGREEN}[ OK ]{bcolors.BOLD}" + f"\tYour notes were saved to:{bcolors.OKGREEN}\t" + url + f"{bcolors.ENDC}")
