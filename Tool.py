import requests as r
import os
import time

logo = """

\033[38;2;0;128;225m ███████████             ███████████                   ████  ███
\033[38;2;0;128;225m░░███░░░░░███           ░█░░░███░░░█                  ░░███ ░███
\033[38;2;0;128;225m ░███    ░███ █████ ████░   ░███  ░   ██████   ██████  ░███ ░███
\033[38;2;0;225;225m ░██████████ ░░███ ░███     ░███     ███░░███ ███░░███ ░███ ░███
\033[38;2;0;225;225m ░███░░░░░░   ░███ ░███     ░███    ░███ ░███░███ ░███ ░███ ░███
\033[38;2;0;225;225m ░███         ░███ ░███     ░███    ░███ ░███░███ ░███ ░███ ░░░ 
\033[38;2;128;0;225m █████        ░░███████     █████   ░░██████ ░░██████  █████ ███
\033[38;2;128;0;225m░░░░░          ░░░░░███    ░░░░░     ░░░░░░   ░░░░░░  ░░░░░ ░░░ 
\033[38;2;128;0;225m               ███ ░███                                         
\033[38;2;128;0;225m              ░░██████                                          
\033[38;2;128;0;225m               ░░░░░░                                           

\033[38;2;0;128;225m[+] \033[38;2;0;225;225mTool by: \033[38;2;128;0;225m@Corey-Yule\033[0m
\n
"""

taskManagerPath = "Storage/TaskManager.py"
requestTestingPath = "Storage/requestPuller.py"

while True:
    print(logo)
    print("\033[38;2;0;128;225m[1] Task Manager \033[0m")
    print("\033[38;2;0;225;225m[2] HTML / JSON Puller \033[0m")
    print("\033[38;2;128;0;225m[3] exit \033[0m")
    print("")
    x = input("option: ")

    if x == "3":
        time.sleep(0.3)
        print("Exiting.")
        time.sleep(0.3)
        print("Exiting..")
        time.sleep(0.3)
        print("Exiting...")
        break
    elif x == "1":
        if os.path.isfile(taskManagerPath):
            os.system(f"python3 {taskManagerPath}")
        else:
            print("Error: TaskManager.py not found")
    elif x == "2":
        if os.path.isfile(requestTestingPath):
            os.system(f"python3 {requestTestingPath}")
        else:
            print("Error: requestPuller.py not found")
