#!/usr/bin/env python3


#  Author  : kozyol
#  Github  : https://github.com/kozyol/SigNull


# This is test version!!
# Not completed and not optimized!!


# All imported Modules
# Plyer modules: for android functionality
from plyer import vibrator
from plyer import notification
from plyer.utils import platform

# Kivy modules: for the app
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.screenmanager import Screen, ScreenManager


# KV config files
# All KV files used in this app
for files in [
    "mainmenu.kv",
    "console.kv",
    "notification.kv",
    "profile.kv",
    "edit.kv",
]:
    with open("Scripts/%s" % files, "r") as kv:
        Builder.load_string(kv.read())


# ImageButton
# This is for clickable image buttons
class ImageButton(ButtonBehavior, Image):
    def on_press(self):
        pass


# MainMenu class
# This will handle MainMenu stuff
class MainMenu(Screen):
    # Path to Assets
    background = "Assets/background.jpg"
    font = "Assets/font.ttf"

    # Get data function
    # This will get username and first-name and set it to user info
    def get_data(self):
        with open("Data/account", "r") as data:
            lines = data.readlines()
            try:
                uname = lines[0].split(":")[1]
            except IndexError:
                uname = "Guest"

            try:
                fname = lines[1].split(":")[1]
            except IndexError:
                fname = "Guest"

        self.manager.get_screen(
            "Profile"
        ).ids.userinfo.text = f"{fname}\n[size=17][font=RobotoMono-Regular]@[color=#aaaaaa]{uname}[/color][/font]"


# Console menu class
# This will handle Console menu stuff
class Console(Screen):
    # Path to Assets
    background = "Assets/background.jpg"
    font = "Assets/font.ttf"

    # Get data function
    # This will get username and first-name and set it to user info
    def get_data(self):
        with open("Data/account", "r") as data:
            lines = data.readlines()
            try:
                uname = lines[0].split(":")[1]
            except IndexError:
                uname = "Guest"

            try:
                fname = lines[1].split(":")[1]
            except IndexError:
                fname = "Guest"

        self.manager.get_screen(
            "Profile"
        ).ids.userinfo.text = f"{fname}\n[size=17][font=RobotoMono-Regular]@[color=#aaaaaa]{uname}[/color][/font]"


# Notification menu class
# This will handle Notification menu stuff
class Notification(Screen):
    # Path to Assets
    background = "Assets/background.jpg"
    font = "Assets/font.ttf"

    # Get data function
    # This will get username and first-name and set it to user info
    def get_data(self):
        with open("Data/account", "r") as data:
            lines = data.readlines()
            try:
                uname = lines[0].split(":")[1]
            except IndexError:
                uname = "Guest"

            try:
                fname = lines[1].split(":")[1]
            except IndexError:
                fname = "Guest"

        self.manager.get_screen(
            "Profile"
        ).ids.userinfo.text = f"{fname}\n[size=17][font=RobotoMono-Regular]@[color=#aaaaaa]{uname}[/color][/font]"


# Profile menu class
# This will handle Profile menu stuff
class Profile(Screen):
    # Path to Assets
    background = "Assets/background.jpg"
    font = "Assets/font.ttf"

    # Load profile function
    # This will load text inputs - in edit menu - to current info
    def load_profile(self):
        with open("Data/account", "r") as data:
            lines = data.readlines()
            try:
                uname = lines[0].split(":")[1]
            except IndexError:
                uname = "Guest"

            try:
                fname = lines[1].split(":")[1]
            except IndexError:
                fname = "Guest"

        self.manager.get_screen("Edit").ids.Username.text = "".join(uname)
        self.manager.get_screen("Edit").ids.Firstname.text = "".join(fname)


# Edit menu class
# This will handle Edit menu stuff
class Edit(Screen):
    # Path to Assets
    background = "Assets/background.jpg"
    font = "Assets/font.ttf"

    # Get data function
    # This will get username and first-name and set it to user info
    def get_data(self):
        with open("Data/account", "r") as data:
            lines = data.readlines()
            try:
                uname = lines[0].split(":")[1]
            except IndexError:
                uname = "Guest"

            try:
                fname = lines[1].split(":")[1]
            except IndexError:
                fname = "Guest"

        self.manager.get_screen(
            "Profile"
        ).ids.userinfo.text = f"{fname}\n[size=17][font=RobotoMono-Regular]@[color=#aaaaaa]{uname}[/color][/font]"

    # Save data function
    # This will save the changes to username and first-name
    def save_profile(self, Username, Firstname):
        with open("Data/account", "w") as data:
            data.write(f"uname:{Username.text.strip()}\nfname:{Firstname.text.strip()}")

        self.manager.get_screen(
            "Profile"
        ).ids.userinfo.text = f"{Firstname.text.strip()}\n[size=17][font=RobotoMono-Regular]@[color=#aaaaaa]{Username.text.strip()}[/color][/font]"

        try:
            title = "Success"
            message = "Profile Updated..."
            ticker = "New message"
            kwargs = {
                "title": title,
                "message": message,
                "ticker": ticker,
                "toast": True,
                "app_icon": "Data/notification.png",
            }
            notification.notify(**kwargs)
        except:
            pass


# Main class of the app
class SigNullApp(App):
    # Build method
    def build(self):
        # Root screen
        root = ScreenManager()

        # Main menu screen
        self.MainMenu = MainMenu(name="MainMenu")
        root.add_widget(self.MainMenu)

        # Console menu screen
        self.Console = Console(name="Console")
        root.add_widget(self.Console)

        # Notification menu screen
        self.Notification = Notification(name="Notification")
        root.add_widget(self.Notification)

        # Profile menu screen
        self.Profile = Profile(name="Profile")
        root.add_widget(self.Profile)

        # Edit menu screen
        self.Edit = Edit(name="Edit")
        root.add_widget(self.Edit)

        # Set current screen to main menu and return root
        root.current = "MainMenu"
        return root


# Run App
if __name__ == "__main__":
    signull = SigNullApp()
    signull.run()

# EOF
