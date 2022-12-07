import tkinter

import pygame
import pymysql
import customtkinter as c
from pygame import mixer

c.set_default_color_theme("dark-blue")
conn = pymysql.connect(host="localhost", user="root", passwd="", database="SavingApp")
cursor = conn.cursor()


class Home(c.CTk):

    def __init__(self):
        super().__init__()
        pygame.init()
        self.title("Saving App")
        self.geometry("880x430")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=2)

        self.left_frame = c.CTkFrame(self, width=180, corner_radius=0)
        self.left_frame.grid(row=0, column=0, sticky="nswe")
        self.right_frame = c.CTkFrame(self, width=580, corner_radius=5)
        self.right_frame.grid(row=0, column=1, padx=20, pady=15, sticky="nswe")

        #-----------leftframe----------

        self.left_frame.grid_rowconfigure(1, weight=4)
        self.left_frame.grid_rowconfigure(11, minsize=10)

        self.Header = c.CTkLabel(self.left_frame,
                                 text="Saving App",
                                 text_font=("Arial", 16),
                                 ).grid(row=0, column=0, pady=40, padx=10,sticky="n")
        self.user = c.CTkLabel(self.left_frame, text="Hello,Lamees")
        self.user.grid(row=1, column=0, padx=20, sticky="n")
        self.label_mode = c.CTkLabel(self.left_frame, text="Appearance Mode:")
        self.label_mode.grid(row=9, column=0, padx=20)
        self.optionmenu_1 = c.CTkOptionMenu(self.left_frame, values=["Light", "Dark"], command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20)

        #----------rightframe------------

        self.goal_var1 = tkinter.IntVar()
        self.goal_var2 = tkinter.IntVar()
        self.percent_var = tkinter.DoubleVar()

        self.container = c.CTkFrame(self.right_frame, corner_radius=5, fg_color=("white", "gray38"))
        self.container.grid(row=0, column=0, padx=20, pady=15, sticky="nswe")

        self.container.grid_rowconfigure(1, weight=4)
        self.container.grid_rowconfigure(11, minsize=10)
        self.info_header = c.CTkLabel(self.container, text="Select your goal:", text_font=("Arial", 14))
        self.info_header.grid(row=0, column=0, padx=5, pady=20, sticky="w")
        self.goal_menue = c.CTkOptionMenu(self.container, values=["Phone", "Bag", "Travel", "Laptop"])
        self.goal_menue.grid(row=0, column=1, padx=5,columnspan=2)

        self.info_header1 = c.CTkLabel(self.container, text="Set your total income:", text_font=("Arial", 14))
        self.info_header1.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.income_slider = c.CTkSlider(self.container, from_=500, to=30000, orient="horizontal", width=365,
                                         number_of_steps=50, variable=self.goal_var1)
        self.income_slider.grid(row=3,column=1,columnspan=4,padx=10)
        self.income_lable = c.CTkLabel(self.container, textvariable=self.goal_var1)
        self.income_lable.grid(row=3, column=0, padx=10)

        self.info_header2 = c.CTkLabel(self.container, text="Set your saving total:", text_font=("Arial", 14))
        self.info_header2.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.goal_slider = c.CTkSlider(self.container, from_=1200, to=10000,orient="horizontal", width=365, number_of_steps=20,
                                       variable=self.goal_var2)
        self.goal_slider.grid(row=5, column=1, columnspan=4, padx=10, pady=10)
        self.goal_lable = c.CTkLabel(self.container, textvariable=self.goal_var2)
        self.goal_lable.grid(row=5, column=0, padx=10, pady=10)

        self.info_header4 = c.CTkLabel(self.container, text="Select your saving percent:", text_font=("Arial", 14))
        self.info_header4.grid(row=8, column=0, padx=5, pady=10, sticky="w")
        self.percent_radio = c.CTkRadioButton(self.container, text="5%", variable=self.percent_var, value=0.05, text_font=("Arial", 12))
        self.percent_radio.grid(row=9, column=1, padx=5)
        self.percent_radio1 = c.CTkRadioButton(self.container, text="10%", variable=self.percent_var, value=0.1, text_font=("Arial", 12))
        self.percent_radio1.grid(row=9, column=2, padx=5)
        self.percent_radio2 = c.CTkRadioButton(self.container, text="15%", variable=self.percent_var, value=0.15, text_font=("Arial", 12))
        self.percent_radio2.grid(row=9, column=3, padx=5)
        self.percent_radio3 = c.CTkRadioButton(self.container, text="20%", variable=self.percent_var, value=0.2, text_font=("Arial", 12))
        self.percent_radio3.grid(row=9, column=4, padx=5)

        self.submit_btn = c.CTkButton(self.container, text="Set goal", width=150, command=self.next_frame)
        self.submit_btn.grid(row=10, column=3, columnspan=2, pady=10)

        #-----defaultValues-------

        self.goal_var1.set(500)
        self.goal_var2.set(1200)
        self.percent_var.set(0.05)
        self.goal_menue.set("Bag")

    def change_appearance_mode(self, new_appearance_mode):
        c.set_appearance_mode(new_appearance_mode)

    def goal_frame(self):
        self.l = self.math()
        self.achivment = tkinter.IntVar()
        self.Content = f"your goal has been settled!\nyou can achieve your goal only in\n{self.l}  months\nyou have to save\n{self.amount_per_month}SR per month!"
        self.remaining = self.goal_var2.get()
        self.remain = f"Remaining amount is {self.remaining}"
        self.text_remaining = tkinter.StringVar()
        self.text_remaining.set(self.remain)

        self.box_frame = c.CTkFrame(self.right_frame, corner_radius=5, fg_color=("white", "gray38"))
        self.box_frame.columnconfigure(2, weight=0)
        self.box_frame.grid(row=0, column=0, padx=15, pady=20, sticky="nswe")
        self.box = c.CTkLabel(self.box_frame, text=self.Content, text_font=("Arial", 22))
        self.box.grid(row=0, column=0, columnspan=4, rowspan=4, padx=10, pady=20)
        self.conter_lable = c.CTkLabel(self.box_frame, textvariable=self.text_remaining,text_font=("Arial", 18))
        self.conter_lable.grid(row=7, column=0, columnspan=4, rowspan=4, padx=10, pady=15, sticky="s")

        self.saving_frame = c.CTkFrame(self.right_frame, corner_radius=5, fg_color=("white", "gray38"))
        self.saving_frame.grid(row=0, column=3, pady=20, sticky="nswe")
        self.saving_progress = c.CTkSlider(self.saving_frame, orient="vertical", height=270, from_=0, to=self.goal_var2.get(),
                                           state="disable", variable=self.achivment)
        self.saving_progress.grid(row=1, column=0, padx=40, pady=5)
        self.lable = c.CTkLabel(self.saving_frame, textvariable=self.goal_var2)
        self.lable.grid(row=0, column=0, padx=5)
        self.add_btn = c.CTkButton(self.saving_frame, text="add", width=100, command=self.add_val)
        self.add_btn.grid(row=4, column=0, pady=10)

    def add_val(self):
        if self.l > 0:
            if self.remaining > self.amount_per_month:
                self.saving_progress.set(self.achivment.get()+int(self.amount_per_month))
                self.remaining = self.remaining-int(self.amount_per_month)
                self.text_remaining.set(f"Only {self.remaining} is left!")
                self.into()
                mixer.music.load('add.mp3')
                mixer.music.play(0)
            elif self.remaining <= self.amount_per_month:
                self.saving_progress.set(self.achivment.get() + int(self.amount_per_month))
                self.remaining = self.remaining - self.remaining
                self.text_remaining.set(f"congrats you have achieved your goal:)")
                mixer.music.load('achived.mp3')
                mixer.music.play(0)
            self.l = self.l - 1


    def math(self):
        self.amount_per_month = self.percent_var.get()*float(self.goal_var1.get())
        for x in range(1, 120):
            num_month = x*self.amount_per_month
            if num_month < self.goal_var2.get():
                continue
            else:
                return x

    def next_frame(self):
        self.container.destroy()
        self.insert_into()
        self.math()
        self.goal_frame()

    def insert_into(self):
        objective = str(self.goal_menue.get())
        income = int(self.goal_var1.get())
        saving_total = int(self.goal_var2.get())
        percent = int(self.percent_var.get()*100)
        recored = (objective, income, saving_total, percent)
        insertion = """INSERT INTO goal (objective,income,saving_total,percent)
                    VALUES(%s, %s, %s, %s) """
        cursor.execute(insertion, recored)
        conn.commit()

    def into(self):
        remaining = int(self.remaining)
        saving_total = int(self.goal_var2.get())
        recored = (saving_total, remaining)
        inserting = """INSERT INTO achivement (saving_total,remaining)VALUES(%s,%s)"""
        cursor.execute(inserting, recored)
        conn.commit()


h = Home()
h.mainloop()
