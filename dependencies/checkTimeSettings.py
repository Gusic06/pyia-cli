import time
import os
from rich.console import *
from rich import *
from rich.traceback import *
from mainTerminal import currentDate
def checkTimeSettings(Input: str):
    console = Console()
    install()
    if Input == "-v" or Input == "--view":
        if os.path.exists(".\\settings.txt"):
            with open(".\\settings.txt", "r")as file:
                contents = file.read()
            if "US" in contents:
                timeSetting: str = "US"
                console.print(f"Current time layout: {timeSetting}")
                return timeSetting
            if "EU" in contents:
                timeSetting: str = "EU"
                console.print(f"Current time layout: {timeSetting}")
                return timeSetting
    if Input == "-e" or Input == "--edit":
        userInput = console.input("[bold][yellow]Select time layout\n1) Day/Month/Year\nor\n2) Month/Day/Year[/]\n\n> ")
        if userInput == "1":
            timeSetting: str = "EU"
            return timeSetting
        if userInput == "2":
            timeSetting: str = "US"
            return timeSetting
        else:
            console.print("[bold][red]Err[/]")
if __name__ == "__main__":
    checkTimeSettings(input("stfu lol"))