from nsdotpy.session import NSSession
import rtoml
import os
import random

# Setup nsdotpy session
UA = input("Please enter your nation's name")
session = NSSession("Flag_uploader", "1.0.0", "Vleerian", UA)

# Load the config file
with open("config.toml", "r") as f:
    config = rtoml.load(f)

# Create a list populated with the files present in the flags directory
Flags = [f for f in os.listdir("flags") if os.path.isfile(os.path.join("flags", f))]

# Begin populating nations with flags
for nation, password in config["nations"].items():
    # logs in and checks if login was successful
    Flag = f"./flags/{random.choice(Flags)}"
    if session.login(nation, password):
        session.change_nation_flag(Flag)
