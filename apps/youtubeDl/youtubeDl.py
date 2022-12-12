from pytube import YouTube
from rich import *
from rich.console import *
from rich.progress import *
import time

def youtubeDl(link):

    yt = YouTube(link)
    console = Console()
    progress = Progress()

    console.print(f"\n[bold][yellow]Title:[/] {yt.title}")
    console.print(f"[bold][yellow]Views:[/] {yt.views}")

    userInput = console.input("\n[bold][yellow]Is this the video you want to download?[/] (Y/N) -> ").title()

    if userInput == "Y" or userInput == "Yes":

        videoDownload = yt.streams.get_highest_resolution()
        #videoDownload.download()
        downloading = progress.add_task("[bold][yellow][/]", start=videoDownload.download(), total=None)
        while not progress.finished:
            progress.update(downloading, advance=0.5)
        

    if userInput == "N" or userInput == "No":
        pass

if __name__ == "__main__":
    youtubeDl()