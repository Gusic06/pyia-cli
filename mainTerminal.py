import os
import subprocess
import sys
import time
from threading import *
import cv2

from rich import *
from rich.panel import *
from rich.traceback import *

from apps.pyflix.pyflix import pyflix
from apps.youtubeDl.youtubeDl import youtubeDl
from dependencies.commands import commands


def checkTimeSettings(Input: str):

    console = Console()
    global timeSetting

    if Input == "-":
        try:
            if "US" in timeSetting:
                timeSetting = "US"
                return timeSetting

            if "EU" in timeSetting:
                timeSetting = "EU"
                return timeSetting

        except NameError:
            timeSetting = "EU"
            return timeSetting

    if Input == "-v" or Input == "--view":

            if "US" in timeSetting:
                timeSetting = "US"
                console.print(f"[bold]Current time layout: [yellow]{timeSetting}[/]")
                return timeSetting

            if "EU" in timeSetting:
                timeSetting = "EU"
                console.print(f"[bold]Current time layout: [yellow]{timeSetting}[/]")
                return timeSetting

    if Input == "-e" or Input == "--edit":

        userInput = console.input("[bold][yellow]Select time layout\n1) Day/Month/Year\nor\n2) Month/Day/Year[/]\n\n> ")

        if userInput == "1":
            timeSetting = "EU"
            return timeSetting

        if userInput == "2":
            timeSetting = "US"
            return timeSetting

        else:
            console.print("[bold][red]Err[/]")


def pyia():

    install()
    console = Console()

    OSNAME = os.getlogin()

    os.system("cls")

    console.print(Panel("[bold][yellow]Welcome![/]\n\nUse [yellow]help[/] to learn what commands are available.[/]", title_align="center", title="[bold][blue]Py[/][yellow]thonia[/]", border_style=""))

    currentDirectory = os.curdir
    loopBackDirectory = os.getcwd()

    while True:

        checkTimeSettings("-") # Giving the function a none value to get an output

        if timeSetting == "US":
            currentDate = time.strftime("%m/%d/%y")
        if timeSetting == "EU":
            currentDate = time.strftime("%d/%m/%y")

        if currentDirectory == '.': 
            currentDirectory = '~'
        
        console.print(f"\n[bold][green]pythonia@{OSNAME} | [yellow]{currentDirectory}[/] | [{currentDate}][/]")
        userInput = console.input("[bold]> [/]",)
        userInput = userInput.split(" ", 4)
        

        if userInput[0] == "help":
            console.print(commands)

        
        if userInput[0] == "clear" or userInput[0] == "cls":
           os.system("cls")


        if userInput[0] == "pip":
            if userInput[1] == "install":
                try:
                    subprocess.call(["py", "-m", "pip", "install", f"{userInput[2]}"])
                except ModuleNotFoundError:
                    console.log(f"[red]ModuleNotFoundError: {userInput[2]} couldn't be found..[/]")
            if userInput[1] == "uninstall":
                try:
                    subprocess.call(["py", "-m", "pip", "uninstall", f"{userInput[2]}"])
                except ModuleNotFoundError:
                    console.log(f"[red]ModuleNotFoundError: {userInput[2]} couldn't be found..[/]")


        if userInput[0] == "pylint":
            if os.path.exists(userInput[1]) and ".py" in userInput[1]:
                try:
                    os.system(f"pylint {userInput[1]}")
                except PermissionError:
                    try:
                        subprocess.call(["pylint", f"{userInput[1]}"])
                    except Exception:
                        console.log(f"[bold][red]Error: unable to run pylint on {userInput[1]}.[/]")  


        if userInput[0] == "code":
            if userInput[1] == ".":
                try:
                    os.system("code .") 
                except Exception:
                    try:
                        subprocess.call(["code", "."])
                    except Exception:
                        console.log("[bold][red]Error: unable to open VSCode.[/]")  
            if userInput[1] != ".":
                if os.path.exists(userInput[1]) and ".py" in userInput[1]:
                    try:
                        os.system(f"code {userInput[1]}")
                    except Exception:
                        try:
                            subprocess.call(["code", f"{userInput[1]}"])
                        except Exception:
                            console.log(f"[bold][red]Error: unable to open {userInput[1]} in VSCode.[/]")  
                if os.path.exists(userInput[1]) is False and ".py" in userInput[1]:
                    console.log(f"[bold][red]Error: Unable to open {userInput[1]} in VSCode as {userInput[1]} either isn't in the current working directory or it doesn't exist.[/]")

        
        if userInput[0] == "ls":

            if userInput[1] == "?curdir":
                for items in os.listdir(os.getcwd()):
                    print(f"[bold][yellow]{items :10}[/]")
            else:
                for items in os.listdir(userInput[1]):
                    print(f"[bold][yellow]{items :10}[/]")


        if userInput[0] == "mkdir":
            os.mkdir(userInput[1])
            console.print(f"Created {userInput[1]}")


        if userInput[0] == "cd":

            try:

                if userInput[2] == "-ls":
                    dir_ = userInput[1]

                    for items in os.listdir(dir_):
                        print(f"[bold][yellow]{items}[/]")

                    if os.path.exists(fr".\\{dir_}"):
                        os.chdir(dir_)
                        currentDirectory = fr"{currentDirectory}/{dir_}"

            except IndexError:

                if userInput[1] != "?origin":
                    dir_ = userInput[1]
                    if os.path.exists(fr".\\{dir_}"):
                        os.chdir(dir_)
                        currentDirectory = fr"{currentDirectory}/{dir_}"
                                 
                if userInput[1] == "?origin":
                    os.chdir(loopBackDirectory)
                    currentDirectory = os.curdir


        if userInput[0] == "newthr":

            if userInput[1] == "pyflix":
                appThread = Thread(target=pyflix, daemon=True)
                subprocess.run(["cmd.exe", "/c", "start", f"{appThread}"], timeout=15)
                #appThread.start()

            if userInput[1] == "youtube-dl":
                appThread = Thread(target=youtubeDl(console.input("[bold][yellow]Link: [/]")), daemon=True)
                subprocess.run(["cmd.exe", "/c", "start", f"{appThread}"], timeout=15)
                #appThread.start()
                

        if userInput[0] == "systime":

            if userInput[1] == "-e" or userInput[1] == "--edit":
                checkTimeSettings(userInput[1])

            if userInput[1] == "-v" or userInput[1] == "--view":
                checkTimeSettings("-v")


        if userInput[0] == "open":


            if userInput[1] == "-va" or userInput[1] == "--viewapps":
                console.print("[bold][blue]Py[/][yellow]flix[/] -> Movie Viewer (use '[yellow]-o pyflix[/]' or '[yellow]--open pyflix[/]' to open pyflix) \n[red]Youtube-DL[/] -> Downloads Youtube Videos (use '[yellow]-o youtube-dl[/]' or '[yellow]--open youtube-dl[/]' to open Youtube-DL)\n")
                continue


            if userInput[1] == "-a" or userInput[1] == "--all":
                if "~" in currentDirectory:
                    dir_ = currentDirectory.replace("~", ".")
                for items in dir_:
                    print(items)
                    os.startfile(items)
                    if ".mp4" in items:
                        video = cv2.VideoCapture(items)
                        duration = video.get(cv2.CAP_PROP_POS_MSEC)
                        os.startfile(items)
                        time.sleep(duration)
                    else:
                        try:
                            with open(items, "r")as file:
                                contents = file.read()
                            console.print(f"[bold][yellow]{contents}[/]")
                        except PermissionError:
                            pass


            if userInput[1] == "pyflix" or userInput[1] == "Pyflix":
                pyflix()
                os.system("cls")
                continue


            if userInput[1] == "youtube-dl" or userInput[1] == "Youtube-DL":
                youtubeDl(console.input("\n[bold][yellow]Link: [/]"))
                os.system("cls")
                continue


            elif os.path.exists(userInput[1]):

                if os.path.exists(userInput[1]):
                    with open(userInput[1], "r")as file:
                        contents = file.read()
                    console.print(f"[bold][yellow]{contents}[/]")

                if os.path.exists(userInput[1]) is False:
                    console.log(f"[bold][red]Error: {userInput[1]} either isn't in the current working directory or it doesn't exist.[/]")
            
            if ".mp4" in userInput[1]:
                os.startfile(userInput[1])
                console.log(f"[bold][yellow]Playing {userInput[1]} now..[/]")

            if os.path.exists(userInput[1]) is False:
                    console.log(f"[bold][red]Error: {userInput[1]} either isn't in the current working directory or it doesn't exist.[/]")


        if userInput[0] == "delete":
            os.remove(userInput[1])
            console.print(f"[bold][yellow]Deleted {userInput[1]}[/]")
            

        if userInput[0] == "exit":
            os.system("cls")
            sys.exit()


if __name__ == "__main__":
    pyia()