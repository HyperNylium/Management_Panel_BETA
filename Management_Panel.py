
import platform
from os import system, startfile
from time import sleep
from webbrowser import open as WBopen
from sys import exit

try:
    from tkinter import *
    from tkinter.ttk import *
except:
    print("\033[31m" + "\nIt looks like you don't have a critical the python library: tkinter\nPlease open the"  +  "\033[36m" + " 'Updater.exe' " + "\033[31m" + "to install all the libraries correctly or open your terminal in administrator mode and type" +  "\033[36m" + ' python -m pip install tk ' + "\033[31m" + "to install correctly")
    sleep(8)
    exit()

try:
    from pyautogui import confirm, alert
except:
    print("\033[31m" + "\nIt looks like you don't have a critical the python library: pyautogui\nPlease open the"  +  "\033[36m" + " 'Updater.exe' " + "\033[31m" + "to install all the libraries correctly or open your terminal in administrator mode and type" +  "\033[36m" + ' python -m pip install pyautogui ' + "\033[31m" + "to install correctly")
    sleep(8)
    exit()

try:
	from customtkinter import CTk, CTkFrame, CTkLabel, CTkFont as Font, CTkButton, set_appearance_mode
except:
    print("\033[31m" + "\nIt looks like you don't have a critical the python library: customtkinter\nPlease open the"  +  "\033[36m" + " 'Updater.exe' " + "\033[31m" + "to install all the libraries correctly or open your terminal in administrator mode and type" +  "\033[36m" + ' python -m pip install customtkinter ' + "\033[31m" + "to install correctly")
    sleep(8)
    exit()


try:
    from plyer import notification
except:
    print("\033[31m" + "\nIt looks like you don't have a critical the python library: plyer\nPlease open the"  +  "\033[36m" + " 'Updater.exe' " + "\033[31m" + "to install all the libraries correctly or open your terminal in administrator mode and type" +  "\033[36m" + ' python -m pip install plyer ' + "\033[31m" + "to install correctly")
    sleep(8)
    exit()


try:
    from requests import get
except:
    print("\033[31m" + "\nIt looks like you don't have a critical the python library: requests\nPlease open the"  +  "\033[36m" + " 'Updater.exe' " + "\033[31m" + "to install all the libraries correctly or open your terminal in administrator mode and type" +  "\033[36m" + ' python -m pip install requests ' + "\033[31m" + "to install correctly")
    sleep(8)
    exit()


try:
    from winshell import desktop
except:
    print("\033[31m" + "\nIt looks like you don't have a critical the python library: winshell\nPlease open the"  +  "\033[36m" + " 'Updater.exe' " + "\033[31m" + "to install all the libraries correctly or open your terminal in administrator mode and type" +  "\033[36m" + ' python -m pip install winshell ' + "\033[31m" + "to install correctly")
    sleep(8)
    exit()

try:
    from colorama import Fore
except:
    print("\033[31m" + "\nIt looks like you don't have a critical the python library: colorama\nPlease open the"  +  "\033[36m" + " 'Updater.exe' " + "\033[31m" + "to install all the libraries correctly or open your terminal in administrator mode and type" +  "\033[36m" + ' python -m pip install colorama ' + "\033[31m" + "to install correctly")
    sleep(8)
    exit()


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
###
### Author/Creator: HyperNylium
###
### Command: pyinstaller --onefile Management_Panel.py
###
### Website: http://www.hypernylium.com
###
### GitHub: https://github.com/HyperNylium/
###
### License: Mozilla Public License Version 2.0
###
### IMPORTANT:  I OFFER NO WARRANTY OR GUARANTEE FOR THIS SCRIPT. USE AT YOUR OWN RISK.
###             I tested it on my own and implemented some failsafes as best as I could,
###             but there could always be some kind of bug.
###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

set_appearance_mode("dark")

# Text Colors
CLR_RED = Fore.RED
CLR_GREEN = Fore.GREEN
CLR_YELLOW = Fore.YELLOW
CLR_BLUE = Fore.BLUE
CLR_CYAN = Fore.CYAN
CLR_WHITE = Fore.WHITE
CLR_BLACK = Fore.BLACK
CLR_MAGENTA = Fore.MAGENTA
RESET_ALL = Fore.RESET

CurrentAppVersion = "3.7.0"
UpdateLink = "https://github.com/HyperNylium/Management_Panel"
DataTXTFileUrl = "http://www.hypernylium.com/Python-Projects/Management_Panel/Data.txt"
clear_command = "cls" if platform.system() == "Windows" else "clear"

Website = "http://hypernylium.com/"
GithubURL = "https://github.com/HyperNylium"
DiscordURL = "https://discord.gg/4FHTjAgw95"
instagramURL = "https://www.instagram.com/hypernylium/"
YoutubeURL = "https://www.youtube.com/channel/UCpJ4F4dMn_DIhtrCJwDUK2A"
TikTokURL = "https://www.tiktok.com/foryou?lang=en"
FacebookURL = "https://www.facebook.com/HyperNylium/"
TwitterURL = "https://twitter.com/HyperNylium"
GetUserDesktopLocation = desktop()

"""
Game_1 = Rocket League
Game_2 = ARK
Game_3 = Destiny 2
Game_4 = Fall Guys
Game_5 = Warships
Game_6 = Control
Game_7 = GTA5
Game_8 = War Thunder
"""

Game_1 = "com.epicgames.launcher://apps/9773aa1aa54f4f7b80e44bef04986cea%3A530145df28a24424923f5828cc9031a1%3ASugar?action=launch&silent=true"
Game_2 = "steam://rungameid/346110"
Game_3 = "com.epicgames.launcher://apps/428115def4ca4deea9d69c99c5a5a99e%3A06bd477f9fbe4259a1421fb3f559aa46%3A592c359fb0e0413fb46dee2d24448eb4?action=launch&silent=true"
Game_4 = "com.epicgames.launcher://apps/50118b7f954e450f8823df1614b24e80%3A38ec4849ea4f4de6aa7b6fb0f2d278e1%3A0a2d9f6403244d12969e11da6713137b?action=launch&silent=true"
Game_5 = "com.epicgames.launcher://apps/84c76746bce94effb8e1047fabfd7eb7%3Ab9e23e5fa8e84064b356677022beb37a%3Aa79746038c6948558274065d24f3faa3?action=launch&silent=true"
Game_6 = "com.epicgames.launcher://apps/calluna%3A9afb582e90b74bdd9e2146fb79c78589%3ACalluna?action=launch&silent=true"
Game_7 = "steam://rungameid/271590"
Game_8 = "steam://rungameid/236390"


print(CLR_YELLOW + "\n  Checking for updates" + RESET_ALL)
response = get(DataTXTFileUrl)

lines = response.text.split('\n')

delimeter = "="

def findValue(fullString):
    fullString = fullString.rstrip("\n")
    value = fullString[fullString.index(delimeter)+1:]
    value = value.replace(" ","")
    return value

for line in lines:
    if line.startswith("Version"):
        App_Version = findValue(line).strip()
    if line.startswith("DevName"):
        Developer = findValue(line).strip()
    if line.startswith("Developer_Lowercase"):
        Developer_Lowercase = findValue(line)
    if line.startswith("LastEditDate"):
        LastEditDate = findValue(line).strip()
    if line.startswith("LatestVersionPythonLink"):
        LatestVersionPythonLink = findValue(line).strip()
    if line.startswith("LatestVersionPythonFileName"):
        LatestVersionPythonFileName = findValue(line).strip()
    if line.startswith("LatestVersionProjectLink"):
        LatestVersionProjectLink = findValue(line).strip()

if App_Version < CurrentAppVersion:
        print(CLR_RED + f"\n  You have an invalid copy/version of this software. Use at your own risk!\n\n  Live/Public version: {App_Version}\n  Current version: {CurrentAppVersion}\n\n  Please go to http://search.hypernylium.com/results/ServerFileManager/ to get the latest/authentic version of this software")
        sleep(7)
        exit()
elif App_Version != CurrentAppVersion or App_Version > CurrentAppVersion:
        print(CLR_RED + f"\n  New version found!" + RESET_ALL)
        output = confirm(title='New Version!', text=f'New Version is v{App_Version}\nYour Version is v{CurrentAppVersion}\n\nNew Version of the app is now available to download/install\nClick "OK" to update and "Cancel" to cancel')
        if (output == "OK"):
            WBopen(UpdateLink)
            exit()
        else:
            exit()
else:
    print(CLR_GREEN + f"\n  {App_Version} is the latest version. Continuing on with launch protocol" + RESET_ALL)
    pass


class App(CTk):
    def __init__(self):
        super().__init__()

        self.title("Management Panel")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.geometry("900x500+400+150")
        self.resizable(0, 0)

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # create navigation frame
        self.navigation_frame = CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(20, weight=1)

        self.navigation_frame_label = CTkLabel(self.navigation_frame, text="Management Panel", compound="left", font=Font(size=20, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.welcome_button = CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Welcome", fg_color="transparent", text_color=("gray10", "gray90"), font=("Arial", 22), hover_color=("gray70", "gray30"), anchor="w", command=self.welcome_button_event)
        self.welcome_button.grid(row=1, column=0, sticky="ew")

        self.apps_button = CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Apps", fg_color="transparent", text_color=("gray10", "gray90"), font=("Arial", 22),hover_color=("gray70", "gray30"), anchor="w", command=self.apps_button_event)
        self.apps_button.grid(row=2, column=0, sticky="ew")

        self.games_button = CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Games", fg_color="transparent", text_color=("gray10", "gray90"), font=("Arial", 22), hover_color=("gray70", "gray30"), anchor="w", command=self.games_button_event)
        self.games_button.grid(row=3, column=0, sticky="ew")

        self.about_button = CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="About", fg_color="transparent", text_color=("gray10", "gray90"), font=("Arial", 22), hover_color=("gray70", "gray30"), anchor="w", command=self.about_button_event)
        self.about_button.grid(row=4, column=0, sticky="ew")

        # create frames
        self.welcome_frame = CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.welcome_frame.grid_columnconfigure(0, weight=1)

        self.apps_frame = CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.apps_frame.grid_columnconfigure(0, weight=1)
    
        self.games_frame = CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.games_frame.grid_columnconfigure(0, weight=1)

        self.about_frame = CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.about_frame.grid_columnconfigure(0, weight=1)


        # Create elements for frames
        self.welcome_frame_button_1 = CTkLabel(self.welcome_frame, text="Welcome", font=Font(size=50, weight="bold"))
        self.welcome_frame_button_1.grid(row=1, column=1, padx=220, pady=50)

        self.welcome_frame_button_1 = CTkLabel(self.welcome_frame, text="Click one of the buttons on the side to get started", font=Font(size=20, weight="bold"))
        self.welcome_frame_button_1.grid(row=2, column=1, padx=0, pady=0)

        self.spacer = CTkLabel(self.apps_frame, text="")
        self.spacer.grid(row=1, column=0, padx=70, pady=50)

        self.apps_frame_button_1 = CTkButton(self.apps_frame, text="YT Downloader", compound="top", font=Font(size=20))
        self.apps_frame_button_1.grid(row=1, column=1, padx=20, pady=10)

        self.apps_frame_button_2 = CTkButton(self.apps_frame, text="J.A.R.V.I.S", compound="top")
        self.apps_frame_button_2.grid(row=1, column=2, padx=20, pady=10)

        self.games_frame_button_1 = CTkButton(self.games_frame, text="CTkButt", compound="top")
        self.games_frame_button_1.grid(row=3, column=0, padx=20, pady=10)

        self.about_frame_button_1 = CTkButton(self.about_frame, text="CTkBut", compound="top")
        self.about_frame_button_1.grid(row=3, column=0, padx=20, pady=10)

        # select default frame
        self.select_frame_by_name("Welcome")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.welcome_button.configure(fg_color=("gray75", "gray25") if name == "Welcome" else "transparent")
        self.apps_button.configure(fg_color=("gray75", "gray25") if name == "Apps" else "transparent")
        self.games_button.configure(fg_color=("gray75", "gray25") if name == "Games" else "transparent")
        self.about_button.configure(fg_color=("gray75", "gray25") if name == "About" else "transparent")

        # show selected frame
        if name == "Welcome":
            self.welcome_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.welcome_frame.grid_forget()

        if name == "Apps":
            self.apps_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.apps_frame.grid_forget()

        if name == "Games":
            self.games_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.games_frame.grid_forget()

        if name == "About":
            self.about_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.about_frame.grid_forget()

    def welcome_button_event(self):
        self.select_frame_by_name("Welcome")
    def apps_button_event(self):
        self.select_frame_by_name("Apps")
    def games_button_event(self):
        self.select_frame_by_name("Games")
    def about_button_event(self):
        self.select_frame_by_name("About")
    def PowerSettings(self):
        system("cmd /c control powercfg.cpl")
    def DisplaySettings(self):
        system("cmd /c control desk.cpl")
    def NetworkSettings(self):
        system("cmd /c %systemroot%\system32\control.exe /name Microsoft.NetworkAndSharingCenter")
    def SoundSettings(self):
        system("cmd /c control mmsys.cpl sounds")
    def AppSettings(self):
        system("cmd /c start ms-settings:appsfeatures")#Put "appwiz.cpl" after /c for control center version
    def StorageSettings(self):
        system("cmd /c start ms-settings:storagesense")
    def WindowsUpdate(self):
        system("cmd /c %systemroot%\system32\control.exe /name Microsoft.WindowsUpdate")
    def TaskManager(self):
        system("cmd /c taskmgr")
    def VPNSettings(self):
        system("cmd /c start ms-settings:network-vpn")
    def ResetNetworkDrive(self):
            try:
                startfile("NetworkDriveReset.bat")
            except:
                alert(self, text=f"The file 'NetworkDriveReset.bat' was not found. This file resets all network drives that are on the users system. The Creator/Developer {Developer} uses this file but doesn't include it with version control.", title='FILE NOT FOUND!', button='OK')

    def github(self):
        open(GithubURL)
    def youtube(self):
        open(YoutubeURL)
    def discord(self):
        open(DiscordURL)
    def instagram(self):
        open(instagramURL)
    def TikTok(self):
        open(TikTokURL)
    def OpenSite(self):
        open(Website)
    def OpenUpdater(self):
        startfile("Updater.exe")
        sleep(0.3)
        self.destroy()
    def Jarvis(self):
        startfile("Jarvis.py")
        sleep(0.3)
        self.destroy()
    def YTDownloader(self):
        startfile("YT_Downloader.py")
        sleep(0.3)
        self.destroy()
    def LaunchGame_1(self):
        open(Game_1)
        notification.notify("Management Panel", "Your game is launching.\nPlease wait while your game launches", timeout=6)
    def LaunchGame_2(self):
        open(Game_2)
        notification.notify("Management Panel", "Your game is launching.\nPlease wait while your game launches", timeout=6)
    def LaunchGame_3(self):
        open(Game_3)
        notification.notify("Management Panel", "Your game is launching.\nPlease wait while your game launches", timeout=6)
    def LaunchGame_4(self):
        open(Game_4)
        notification.notify("Management Panel", "Your game is launching.\nPlease wait while your game launches", timeout=6)
    def LaunchGame_5(self):
        open(Game_5)
        notification.notify("Management Panel", "Your game is launching.\nPlease wait while your game launches", timeout=6)
    def LaunchGame_6(self):
        open(Game_6)
        notification.notify("Management Panel", "Your game is launching.\nPlease wait while your game launches", timeout=6)
    def LaunchGame_7(self):
        open(Game_7)
        notification.notify("Management Panel", "Your game is launching.\nPlease wait while your game launches", timeout=6)
    def LaunchGame_8(self):
        open(Game_8)
        notification.notify("Management Panel", "Your game is launching.\nPlease wait while your game launches", timeout=6)
    def on_closing(self, event=0):
        print(CLR_RED + "\n  GUI is being terminated" + RESET_ALL)
        self.destroy()
        exit()

if __name__ == "__main__":
    app = App()
    app.mainloop()