# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 10:11:38 2021

@author: Waqad, Sheraz Jameel & Ayyaz

"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from remove_vehicle import remove_page
import time
import json


def add_vehicle_page(root):
    global localtime
    localtime = time.asctime(time.localtime(time.time()))
    #! Reading variable values from fields
    vno_entry_r = StringVar()
    vowner_entry_r = StringVar()
    vtype_combo_val = StringVar()
    fee = 0
    #!-----------------------------------

    #! SubmitForm Buttion Click method

    def submitAddForm():
        global localtime
        localtime = time.asctime(time.localtime(time.time()))
        global fee
        #! Printing field data
        print("vno_entry_r: {} ".format(vno_entry_r.get()))
        print("vowner_entry_r: {} ".format(vowner_entry_r.get()))
        #!---------------------------------------------------

        #! Opening Record File to read JSON data
        a_file = open("data.json", "r")
        output = json.load(a_file)
        dictionary_data_r = output
        print(dictionary_data_r)
        a_file.close()
        #!---------------------------------------

        #! Entering new Vehice data to map

        if vno_entry_r.get().strip() != "":
            if vowner_entry_r.get().strip() != "":
                if vtype_combo.get() != "Vehicle Type":
                    name = vno_entry_r.get().strip().upper()
                    time_list = localtime.split(' ')
                    print(time_list)
                    if vtype_combo.get() == "Car":
                        fee = 40
                    elif vtype_combo.get() == "Motorbike":
                        fee = 20
                    DataList = [vowner_entry_r.get().strip().title(),
                                vtype_combo.get(), {"in_time": time_list[3],
                                                    "out_time": "",
                                                    "fee": fee,
                                                    }
                                ]
                    print(DataList)
                    dictionary_data_r[name] = DataList

                    #! Opening file for writing data
                    a_file = open("data.json", "w")
                    json.dump(dictionary_data_r, a_file)
                    a_file.close()
                    #!--------------------------------

                    #! Clearing the fields after data entry
                    vno_entry_r.delete(0, 'end')
                    vowner_entry_r.delete(0, 'end')
                    vtype_combo.delete(0, 'end')
                    vtype_combo.set("Vehicle Type")
                    root.update()
                    #!-------------------------------------
                else:
                    messagebox.showerror(
                        "Mising Vehicle Type", "Please select Vehicle Type!")
            else:
                messagebox.showerror("Mising Owner Name",
                                     "Please enter Owner Name!")
        else:
            messagebox.showerror("Mising Vehicle Number",
                                 "Please enter Vehicle Number!")

        #!---------------------------------------------
    #!---------------------------------------------

    #! Combobox value change listener function

    def onComboChanged(event):
        print("ÿou selected: {}".format(vtype_combo.get()))
    #!-----------------------------------------------------

    # a_file = open("data.json", "r")
    # output = a_file.read()
    # print(output)
    # a_file.close()

    #! Title Frame
    title_frame_r = Frame(root, width=700, relief=FLAT)
    title_frame_r.pack(side=TOP)
    #!-----------------------------------------------

    #! Field Frame fror label + field
    field_frame_r = Frame(root, width=700, relief=FLAT)
    field_frame_r.pack(side=TOP)
    #!--------------------------------------------

    #! Button Frame
    button_frame_r = Frame(root, width=700, pady=10, relief=FLAT)
    button_frame_r.pack(side=TOP)
    #!--------------------------------------------

    #! Title label
    title_lbl = Label(title_frame_r, font=(
        'Verdana', 32), text="Add Vehicle", bd=6)
    title_lbl.grid(row=0, column=0)
    #!--------------------------------------------

    #! set current time
    #! Getting local time for display
    localtime = time.asctime(time.localtime(time.time()))
    #!-------------------------------
    date_lbl = Label(title_frame_r, font=('arial', 14, 'bold'),
                     text="Date: "+localtime, fg="blue",
                     bd=10, anchor="w")
    date_lbl.grid(row=1, column=0)
    #!--------------------------------------------

    #! Vehicle No. label and field
    vno_entry_lbl = Label(field_frame_r, font=('arial', 14, 'bold'),
                          justify="left",
                          text="Vehicle Number:", fg="black",
                          bd=10, anchor="w")
    vno_entry_lbl.grid(row=0, column=0)

    vno_entry_r = Entry(field_frame_r, font=('arial', 14), width=22,
                        textvariable="vno_entry_r", justify="left")
    vno_entry_r.grid(row=0, column=1)
    #!------------------------------------------------------------

    #! Vehicle Owner label and field
    vowner_entry_lbl = Label(field_frame_r, font=('arial', 14, 'bold'), justify="left",
                             text="Vehicle Owner:", fg="black",
                             bd=10, anchor="w")
    vowner_entry_lbl.grid(row=1, column=0)

    vowner_entry_r = Entry(field_frame_r, font=('arial', 14), width=22,
                           textvariable="vowner_entry_r", justify="left")
    vowner_entry_r.grid(row=1, column=1)
    #!---------------------------------------------------------------

    #! Combo box label and field
    vtype_combo_lbl = Label(field_frame_r, font=('arial', 14, 'bold'), justify="left",
                            text="Vehicle Type:  ", fg="black",
                            bd=10, anchor="w")
    vtype_combo_lbl.grid(row=2, column=0)

    items = ('Motorbike', 'Car')
    vtype_combo = ttk.Combobox(field_frame_r, font=('arial', 14),
                               textvariable="vtype_combo_val",
                               state="readonly")
    vtype_combo['values'] = items
    vtype_combo.set('Vehicle Type')
    vtype_combo.grid(row=2, column=1)
    vtype_combo.bind('<<ComboboxSelected>>', onComboChanged)
    #!---------------------------------------------------------

    #! Submittion Button
    add_btn = Button(button_frame_r, font=('Verdana', 14),
                     text="Add Vehicle", command=submitAddForm)
    add_btn.grid(row=0, column=0)
    #!---------------------------------------------------------
