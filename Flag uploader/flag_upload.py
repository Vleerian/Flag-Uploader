from nsdotpy.session import NSSession
import requests
import os
import uuid
import random
import csv

# Create the folder if it doesn't already exist
folder_name = "Flags"
if not os.path.exists(folder_name):
	os.makedirs(folder_name)

UA=input("User Agent: ")
mode=input("What mode would you like to use? I can do random or from a file or type litterly anything else for 9003 mode: ")

session = NSSession("Flag updator", "1.0.0", "Written by 9003", UA)


if mode.lower() == "random":
	print("You are in random mdoe meaning all flags will be randomly picked.")
	folder_path = "Flags/Random"  # Replace with the path to your folder
	file_list = os.listdir(folder_path)  # Get a list of all files in the folder
	random_file = random.choice(file_list)  # Pick a random file from the list
	random_file_path = os.path.join(folder_path, random_file)  # Get the full path to the random file

	with open('puppet.csv') as csv_file:
		csv_reader = csv.reader(csv_file)
		for row in csv_reader:
			if session.login(row[0], row[1]):  # logs in and checks if login was successful
				session.change_nation_flag(random_file_path)
elif mode.lower() == "file":
	print("You are in file mode meaning that 3rd value in the csv will be picked.")
	with open('puppet.csv') as csv_file:
		csv_reader = csv.reader(csv_file)
		for row in csv_reader:
			if session.login(row[0], row[1]):
				try:
					session.change_nation_flag(os.path.join("Flags",row[2]))
				except IndexError:
					ans = input("No file found type random for a random flag or anything else and I'll skip it")
					if ans.lower().strip() == "random":
						print("You are in random mdoe meaning all flags will be randomly picked.")
						folder_path = "Flags/Random"  # Replace with the path to your folder
						file_list = os.listdir(folder_path)  # Get a list of all files in the folder
						random_file = random.choice(file_list)  # Pick a random file from the list
						random_file_path = os.path.join(folder_path, random_file)
						if session.login(row[0], row[1]):  # logs in and checks if login was successful
							session.change_nation_flag(random_file_path)


else:
	print("You are in the best mode I'll handle the flags! 9003 Style!")
	with open('puppet.csv') as csv_file:
		csv_reader = csv.reader(csv_file)
		for row in csv_reader:
			if session.login(row[0], row[1]):  # logs in and checks if login was successful
				session.change_nation_flag(os.path.join("Flags","9003.png"))	
