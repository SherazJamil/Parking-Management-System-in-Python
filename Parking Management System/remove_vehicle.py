from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import json
from types import LambdaType


# #! Making the second_root/main Window
# second_root = Tk()
# second_root.geometry("700x500")
# second_root.title("Parking Management System")
# #!-------------------------------------


def remove_page(second_root):

    #! Reading variable values from fields
    vno_entry = StringVar()
    vfee_entry = StringVar()
    fee = 0
    #!-----------------------------------

    a_file = open("data.json", "r")
    output = json.load(a_file)
    dictionary_data = output
    a_file.close()

    # name = dictionary_data[vno_entry.get().strip().upper()]
    # print(name[0])

    def write_data_to_file(dictionary_data_in, filename):
        print("inside write-data with dictionary_data_in is: {} and filename is: {}".format(
            dictionary_data_in, filename))
        a_file = open(filename, "w")
        json.dump(dictionary_data_in, a_file)
        a_file.close()


    def choice(option):
        global pop
        global fee
        if option == "yes":
            a_file = open("data.json", "r")
            output = json.load(a_file)
            dictionary_data = output
            a_file.close()
            # name = dictionary_data[vno_entry.get().strip().upper()]
            dict_entry = vno_entry.get().strip().upper()
            if dict_entry in dictionary_data:
                print("inside if yes and if data exists!")
                #!---------Read remove file-----------
                a_file = open("remove_data.json", "r")
                remove_data_output = json.load(a_file)
                remove_data_record = remove_data_output
                a_file.close()
                print("just read and closed the remove data file")

                #!------------------------------------
                localtime = time.asctime(time.localtime(time.time()))
                time_list = localtime.split(' ')
                print(time_list)
                previous_data = dictionary_data[vno_entry.get(
                ).strip().upper()]
                print("previous data is: {}".format(previous_data))

                # DataList = [remove_data_record[vno_entry.get().strip().upper()],
                #     vtype_combo.get(), time_list[3]]
                previous_data[2]["out_time"] = time_list[3]
                remove_data_record[vno_entry.get(
                ).strip().upper()] = previous_data
                print("remove data record is: {}".format(remove_data_record))

                # print(DataList)
                # dictionary_data[name] = DataList
                dictionary_data.pop(vno_entry.get().strip().upper())
                print("You pressed Yes and fee in if: {} ".format(fee))
                vno_entry.delete(0, 'end')
                #!------------------------
                vfee_entry.config(state="normal")
                vfee_entry.delete(0, 'end')
                vfee_entry.config(state="disable")
                #!------------------------
                # vfee_entry.delete(0, 'end')
                write_data_to_file(remove_data_record, "remove_data.json")
            else:
                messagebox.showinfo("Wait!", "Vehicle does not exist")
                print("Vehicle does not exist!!!!!")
                print("You pressed Yes and fee in else: {} ".format(fee))
            write_data_to_file(dictionary_data, "data.json")
            pop.destroy()
        elif option == "no":
            vfee_entry.config(state="normal")
            vfee_entry.delete(0, 'end')
            vfee_entry.insert(0, fee)
            vfee_entry.config(state="disable")
            print("You pressed No and fee: {} ".format(fee))
            pop.destroy()

    def popup(v_no, v_type, o_name):
        global pop
        global fee
        pop = Toplevel(second_root)
        pop.title("Are you sure?")
        pop.geometry("300x250")
        pop.config(bg="blue", pady=10)

        vno_h_lbl = Label(pop, text="Vehicle No:   ", bg="blue",
                          fg="white", font=("helvetica", 12, "bold"))
        vno_h_lbl.grid(row=1, column=1, pady=2, padx=5)

        vno_lbl = Label(pop, text=v_no, bg="blue",
                        fg="white", font=("helvetica", 12, "bold"))
        vno_lbl.grid(row=1, column=2, pady=2, padx=5)

        vtype_h_lbl = Label(pop, text="Vehicle Type: ", bg="blue",
                            fg="white", font=("helvetica", 12, "bold"))
        vtype_h_lbl.grid(row=2, column=1, pady=2, padx=5)

        vtype_lbl = Label(pop, text=v_type, bg="blue",
                          fg="white", font=("helvetica", 12, "bold"))
        vtype_lbl.grid(row=2, column=2, pady=2, padx=5)

        oname_h_lbl = Label(pop, text="Owner Name: ", bg="blue",
                            fg="white", font=("helvetica", 12, "bold"))
        oname_h_lbl.grid(row=3, column=1, pady=2, padx=5)

        oname_lbl = Label(pop, text=o_name, bg="blue",
                          fg="white", font=("helvetica", 12, "bold"))
        oname_lbl.grid(row=3, column=2, padx=5, pady=2)

        fee_h_lbl = Label(pop, text="Vehicle Fee:  ", bg="blue",
                          fg="white", font=("helvetica", 12, "bold"))
        fee_h_lbl.grid(row=4, column=1, pady=2, padx=5)

        if v_type == "Motorbike":
            fee = 20
        elif v_type == "Car":
            fee = 40

        fee_lbl = Label(pop, text="Rs. {}".format(fee), bg="blue",
                        fg="white", font=("helvetica", 12, "bold"))
        fee_lbl.grid(row=4, column=2, padx=5, pady=2)

        pop_lbl = Label(pop, text="Is this fee paid?", bg="blue",
                        fg="white", font=("helvetica", 12, "bold"))
        pop_lbl.grid(row=5, column=1, padx=20, pady=5)

        yes = Button(pop, text="YES",
                     command=lambda: choice("yes"), bg="orange")
        yes.grid(row=6, column=1, padx=10)

        no = Button(pop, text="NO",
                    command=lambda: choice("no"), bg="yellow")
        no.grid(row=6, column=2, padx=10)

        myFrame = Frame(pop, bg="blue")
        myFrame.pack(pady=5)

    def submitRemoveForm():
        #! Printing field data
        print("vno_entry: {} ".format(vno_entry.get()))
        print("vfee_entry: {} ".format(vfee_entry.get()))
        #!---------------------------------------------------

        if vno_entry.get().strip() != "":
            #! Opening Record File to read JSON data
            a_file = open("data.json", "r")
            output = json.load(a_file)
            dictionary_data = output
            a_file.close()
            #!---------------------------------------

            #! Removing a Vehice data from map

            field_data = vno_entry.get().strip().upper()
            if field_data in dictionary_data:
                name = dictionary_data[vno_entry.get().strip().upper()]
                print(name[0])
                popup(vno_entry.get().strip().upper(), name[1], name[0])
            elif field_data == "":
                print("Field data is: {}".format(field_data))
                messagebox.showinfo("Wait!", "Please enter some data")
                print("Please enter some data")
            else:
                messagebox.showinfo("Wait!", "Vehicle does not exist")
                print("Vehicle does not exist neechy")
                print("Field data is: {}".format(field_data))
            #!---------------------------------------------

            #! Clearing the fields after data entry
            vno_entry.delete(0, 'end')
            vfee_entry.delete(0, 'end')
            #!-------------------------------------
        else:
            messagebox.showerror(
                "Mising Vehicle Number!", "Please enter Vehicle Number!")
    #!---------------------------------------------

    #! Getting local time for display
    localtime = time.asctime(time.localtime(time.time()))
    #!-------------------------------

    #! Title Frame
    title_frame = Frame(second_root, width=500, relief=FLAT)
    title_frame.pack(side=TOP)
    #!-----------------------------------------------

    #! Field Frame fror label + field
    field_frame = Frame(second_root, width=500, relief=FLAT)
    field_frame.pack(side=TOP)
    #!--------------------------------------------

    #! Button Frame
    button_frame = Frame(second_root, width=500, pady=10, relief=FLAT)
    button_frame.pack(side=TOP)
    #!--------------------------------------------

    #! Title label
    title_lbl = Label(title_frame, font=(
        'Verdana', 32), text="Remove Vehicle", bd=6)
    title_lbl.grid(row=0, column=0)
    #!--------------------------------------------

    #! set current time
    date_lbl = Label(title_frame, font=('arial', 14, 'bold'),
                     text="Date:"+localtime, fg="blue",
                     bd=10, anchor="w")
    date_lbl.grid(row=1, column=0)
    #!--------------------------------------------

    #! Vehicle No. label and field
    vno_entry_lbl = Label(field_frame, font=('arial', 14, 'bold'),
                          justify="left",
                          text="Vehicle Number:", fg="black",
                          bd=10, anchor="w")
    vno_entry_lbl.grid(row=0, column=0)

    vno_entry = Entry(field_frame, font=('arial', 14), width=22,
                      textvariable="vno_entry", justify="left")
    vno_entry.grid(row=0, column=1)
    #!------------------------------------------------------------

    #! Vehicle parking fee label and field
    vfee_entry_lbl = Label(field_frame, font=('arial', 14, 'bold'), justify="left",
                           text="Vehicle Fee:", fg="black",
                           bd=10, anchor="w")
    vfee_entry_lbl.grid(row=1, column=0)

    vfee_entry = Entry(field_frame, font=('arial', 14), width=22,
                       textvariable="vfee_entry", justify="left", state="disable")
    vfee_entry.grid(row=1, column=1)
    #!---------------------------------------------------------------

    #! Submittion Button
    rem_btn = Button(button_frame, font=('Verdana', 14),
                     text="Remove Vehicle", command=submitRemoveForm)
    rem_btn.grid(row=0, column=0)
    #!---------------------------------------------------------
