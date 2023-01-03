import tkinter

from customtkinter import CTk, CTkFrame, CTkLabel, CTkFont as Font, CTkButton
import os
from PIL import Image


class App(CTk):
    def __init__(self):
        super().__init__()

        self.title("Management Panel")
        self.minsize(900, 500)
        self.geometry("900x500")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # create navigation frame
        self.navigation_frame = CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(20, weight=1)

        self.navigation_frame_label = CTkLabel(self.navigation_frame, text="Management Panel", compound="left", font=Font(size=20, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home", fg_color="transparent", text_color=("gray10", "gray90"), font=("Arial", 20), hover_color=("gray70", "gray30"), anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.apps_button = CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Apps", fg_color="transparent", text_color=("gray10", "gray90"), font=("Arial", 20),hover_color=("gray70", "gray30"), anchor="w", command=self.apps_button_event)
        self.apps_button.grid(row=2, column=0, sticky="ew")

        self.games_button = CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Games", fg_color="transparent", text_color=("gray10", "gray90"), font=("Arial", 20), hover_color=("gray70", "gray30"), anchor="w", command=self.games_button_event)
        self.games_button.grid(row=3, column=0, sticky="ew")

        self.about_button = CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="About", fg_color="transparent", text_color=("gray10", "gray90"), font=("Arial", 20), hover_color=("gray70", "gray30"), anchor="w", command=self.about_button_event)
        self.about_button.grid(row=4, column=0, sticky="ew")

        # create frames
        self.home_frame = CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.apps_frame = CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.apps_frame.grid_columnconfigure(0, weight=1)
    
        self.games_frame = CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.games_frame.grid_columnconfigure(0, weight=1)

        self.about_frame = CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.about_frame.grid_columnconfigure(0, weight=1)


        # Create elements for frames
        self.home_frame_button_1 = CTkButton(self.home_frame, text="CTkButton", compound="top")
        self.home_frame_button_1.grid(row=3, column=0, padx=20, pady=10)

        self.apps_frame_button_1 = CTkButton(self.apps_frame, text="CTkButto", compound="top")
        self.apps_frame_button_1.grid(row=3, column=0, padx=20, pady=10)

        self.games_frame_button_1 = CTkButton(self.games_frame, text="CTkButt", compound="top")
        self.games_frame_button_1.grid(row=3, column=0, padx=20, pady=10)

        self.about_frame_button_1 = CTkButton(self.about_frame, text="CTkBut", compound="top")
        self.about_frame_button_1.grid(row=3, column=0, padx=20, pady=10)

        # select default frame
        self.select_frame_by_name("Home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "Home" else "transparent")
        self.apps_button.configure(fg_color=("gray75", "gray25") if name == "Apps" else "transparent")
        self.games_button.configure(fg_color=("gray75", "gray25") if name == "Games" else "transparent")
        self.about_button.configure(fg_color=("gray75", "gray25") if name == "About" else "transparent")

        # show selected frame
        if name == "Home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()

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

    def home_button_event(self):
        self.select_frame_by_name("Home")
    def apps_button_event(self):
        self.select_frame_by_name("Apps")
    def games_button_event(self):
        self.select_frame_by_name("Games")
    def about_button_event(self):
        self.select_frame_by_name("About")

if __name__ == "__main__":
    app = App()
    app.mainloop()