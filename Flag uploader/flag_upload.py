from nsdotpy.session import NSSession
import csv

UA = input("Please enter your nation's name")

session = NSSession("Flag_uploader", "1.0.0", "Written by 9003",UA)
reader = []

 with open("flag_list.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for each in reader:
        # logs in and checks if login was successful
        if session.login(each[0], each[1]):
            input(each[3])
            session.change_nation_flag(each[3])




