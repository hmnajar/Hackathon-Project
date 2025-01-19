import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
from tkinter import font
from PIL import Image
from PIL import ImageTk

def update_team_image1(*args):#this is the function used to update the left team logos
    team_selected = T1_selected_option.get()
    if team_selected in team_images:
        try:
            image_path = team_images[team_selected]
            pil_image = Image.open(image_path)
            pil_image = pil_image.resize((200,200))
            team_image = ImageTk.PhotoImage(pil_image)
            team_image_label1.config(image=team_image)
            team_image_label1.image = team_image
        except Exception as e:
            print(f"Failed to Load Image")

def update_team_image2(*args):#this is the function used to update the right team logos
    team_selected = T2_selected_option.get()
    if team_selected in team_images:
        try:
            image_path = team_images[team_selected]
            pil_image = Image.open(image_path)
            pil_image = pil_image.resize((200,200))
            team_image = ImageTk.PhotoImage(pil_image)
            team_image_label2.config(image=team_image)
            team_image_label2.image = team_image
        except Exception as e:
            print(f"Failed to Load Image")

mainWindow = tk.Tk()
mainWindow.title("Val Match Predictor", )

mainWindow.configure(bg="#F5F5F5") #background color

mainWindow.columnconfigure(0, weight=1, uniform="all")
mainWindow.columnconfigure(1, weight=1, uniform="all")
mainWindow.columnconfigure(2, weight=1, uniform="all")

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=1)
mainWindow.rowconfigure(2, weight=1, uniform="all")
mainWindow.rowconfigure(3, weight=1, uniform="all")
mainWindow.rowconfigure(4, weight=1, uniform="all")
mainWindow.rowconfigure(5, weight=1)
mainWindow.rowconfigure(6, weight=1)

title_label = tk.Label(mainWindow, text="Valorant Match Predictor", font=("Arial", 24), bg="#F5F5F5")                           #title 
title_label.grid(row=0, column=0, pady=(20,10), columnspan = 3)

times_new_roman_font = font.Font(family="Times New Roman", size=14)                                                             #font

description = "Valorant Match Prediction Tool powered by Machine Learning and Artificial Intelligence to predict VCT matches"
directions = tk.Label(mainWindow, text=description, font=times_new_roman_font, bg="#F5F5F5")                                    #description
directions.grid(row=2, column=0, pady=(10, 10), columnspan=3, sticky="ew")

button_image = Image.open(r"C:/Users/PC/Desktop/Hackathon 2025/StartButton.PNG")                                  #Start Button #change possible dependent on image
resized_image = button_image.resize((250, 70))
button_photo = ImageTk.PhotoImage(resized_image)

image_path1 = r"C:\Users\PC\Desktop\Hackathon 2025\logoValorant.PNG" #logo image #change possible dependent on image
logo_image1 = Image.open(image_path1).resize((300, 300))
photo1 = ImageTk.PhotoImage(logo_image1)
image_label1 = tk.Label(mainWindow, image=photo1, bg="#F5F5F5")
image_label1.grid(row=1, column=0, columnspan=3)

image_path2 = r"C:\Users\PC\Desktop\Hackathon 2025\logoValorant.PNG" #leftsided team #change possible dependent on image
logo_image2 = Image.open(image_path2).resize((300, 300))
photo2 = ImageTk.PhotoImage(logo_image2)
image_label2 = tk.Label(mainWindow, image=photo2, bg="#F5F5F5")
image_label2.grid(row=1, column=0, columnspan=1)

image_path3 = r"C:\Users\PC\Desktop\Hackathon 2025\logoValorant.PNG" #right sided team #change possible dependent on image
logo_image3 = Image.open(image_path3).resize((300, 300))
photo3 = ImageTk.PhotoImage(logo_image3)
image_label3 = tk.Label(mainWindow, image=photo3, bg="#F5F5F5")
image_label3.grid(row=1, column=2, columnspan=5) # weird convention

selected_option = StringVar()
T1_selected_option = StringVar() #used stringvar so we can keep track of it using the drop down menu
T2_selected_option = StringVar()

selected_option.set("Pick a Map")
T1_selected_option.set("Pick Team 1")
T2_selected_option.set("Pick Team 2")


options = ["Haven", "Ascent", "Split", "Fracture", "Pearl", "Breeze", "Icebox", "Sunset", "Lotus", "Bind"]
teams = ["100T", "C9", "EG", "FUR", "KRU", "LEV", "LOUD", "MIBR", "NRG", "SEN", "G2", "2G"]

#list of team images
team_images = {"100T": r"C:/Users/PC/Desktop/Hackathon 2025/100TLogo.PNG", #change possible dependent on image
                "C9" : r"C:/Users/PC/Desktop/Hackathon 2025/C9Logo.PNG",
                "EG" : r"C:/Users/PC/Desktop/Hackathon 2025/EGLogo.PNG",
                "FUR" : r"C:/Users/PC/Desktop/Hackathon 2025/FURLogo.PNG",
                "KRU" : r"C:/Users/PC/Desktop/Hackathon 2025/KRULogo.PNG",
                "LEV" : r"C:/Users/PC/Desktop/Hackathon 2025/LEVLogo.PNG",
                "LOUD" : r"C:/Users/PC/Desktop/Hackathon 2025/LOUDLogo.PNG",
                "MIBR" : r"C:/Users/PC/Desktop/Hackathon 2025/MIBRLogo.PNG",
                "NRG" : r"C:/Users/PC/Desktop/Hackathon 2025/NRGLogo.PNG",
                "SEN" : r"C:/Users/PC/Desktop/Hackathon 2025/SENLogo.PNG",
                "G2" : r"C:/Users/PC/Desktop/Hackathon 2025/G2Logo.PNG",
                "2G" : r"C:/Users/PC/Desktop/Hackathon 2025/TwoGLogo.PNG"
               }

dropdown = tk.OptionMenu(mainWindow, selected_option, *options)                                                                 #map dropdown
dropdown.grid(row=3, column=1, padx=10, pady=(1, 0))

def display_selection():
    print(f"Selected option: {selected_option.get()}")

T1_dropdown = tk.OptionMenu(mainWindow, T1_selected_option, *teams)                                                             #team1 dropdown
T1_dropdown.grid(row=5, column=0, pady=(10,5))

button = tk.Button(mainWindow, image=button_photo, command=display_selection)                                                #match results button
button.grid(row=5, column=1, pady=(10,20))


T2_dropdown = tk.OptionMenu(mainWindow, T2_selected_option, *teams)                                                            #team2 dropdown
T2_dropdown.grid(row=5, column=2, pady=(10,5))

statistics = tk.Listbox(mainWindow)                                                                                            #list box
statistics.grid(row=6, column=0, columnspan=1, pady=(10,20))

statistics.config(height=15, width=50)

T1_statistics = tk.Listbox(mainWindow)                                                                                         #Team 1 list box
T1_statistics.grid(row=6, column=2, columnspan=1, pady=(10,20))

T1_statistics.config(height=15, width=50)

T2_statistics = tk.Listbox(mainWindow)                                                                                         #Team 2 list box
T2_statistics.grid(row=6, column=1, columnspan=1, pady=(10,20))

T2_statistics.config(height=15, width=50)

team_image_label1 = tk.Label(mainWindow, bg="#F5F5F5") #This u pdates the team logo
team_image_label1.grid(row=1, column=0, pady=(10, 20), columnspan=1)
team_image_label2 = tk.Label(mainWindow, bg="#F5F5F5") #This u pdates the team logo
team_image_label2.grid(row=1, column=2, pady=(10, 20), columnspan=5)

T1_selected_option.trace_add("write", update_team_image1) #independently updates left sided team # trace_add tracjs variables in our case its stringVar
T2_selected_option.trace_add("write", update_team_image2) #independently updates right sided team

mainWindow.mainloop()