# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 10:11:38 2021

@author: Waqad, Sheraz Jameel & Ayyaz

"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from remove_vehicle import remove_page
from add_vehicle import add_vehicle_page
from record import record_page
import time
import json


# #! Getting local time for display
# localtime = time.asctime(time.localtime(time.time()))
# #!-------------------------------

#! Making the root/main Window
main_root = Tk()
main_root.geometry("700x500")
main_root.resizable(width=FALSE, height=FALSE)
main_root.title("Parking Management System")
#!------------------------------------------

#! Making the Tabs Window
tab_parent = ttk.Notebook(main_root, width=700, height=500)
tab_parent.grid(row=0, column=0)
#!------------------------------------------

#! Making the roots of different Tab Windows
root = Frame(tab_parent, width=700, height=500, padx=40, pady=40)
second_root = Frame(tab_parent, width=700, height=500, padx=40, pady=40)
third_root = Frame(tab_parent, width=700, height=500, padx=40, pady=40)

root.pack(fill="both", expand=1)
second_root.pack(fill="both", expand=1)
third_root.pack(fill="both", expand=1)
#!------------------------------------------

#! Adding the pages to Tabs
tab_parent.add(root, text="Add Vehicle")
tab_parent.add(second_root, text="Remove Vehicle")
tab_parent.add(third_root, text="Parking Record")
#!------------------------------------------

#!+++++---First_Page---+++++

add_vehicle_page(root)

#!+++++---Second_Page---+++++

remove_page(second_root)

#!+++++---Third_Page----+++++

record_page(third_root)

main_root.mainloop()
