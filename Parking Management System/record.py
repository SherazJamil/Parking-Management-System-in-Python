from tkinter import *
from tkinter import ttk
import json

# #! Making the root/main Window
# root = Tk()
# root.geometry("700x500")
# root.title("Parking Management System")
# #!----------------------------

feeval = 0


def record_page(root):
    feeval = 0
    #! Opening Record File to read JSON data

    def readData():
        a_file = open("data.json", "r")
        output = json.load(a_file)
        dictionary_data = output
        a_file.close()
        return dictionary_data
    #!---------------------------------------

    def refresh_tree():
        global feeval
        for i in tv.get_children():
            tv.delete(i)
        #!--------------------------
        dictionary_data = readData()
        for k in dictionary_data.keys():
            temp_list = [k, dictionary_data[k][0], dictionary_data[k][1]]
            print(k, dictionary_data[k][0], dictionary_data[k][1])
            tv.insert('', 'end', values=temp_list)

        rem_file = open("remove_data.json", "r")
        output = json.load(rem_file)
        rem_data = output
        rem_file.close()

        feeval = 0
        for k in rem_data.keys():
            feeval += rem_data[k][2]['fee']
            print("feeval is: {}".format(feeval))

        vfeeval_entry.config(state="normal")
        vfeeval_entry.delete(0, 'end')
        vfeeval_entry.insert(0, feeval)
        vfeeval_entry.config(state="disable")

    #! Field Frame fror label + field
    tree_frame = Frame(root, width=500, relief=FLAT, padx=20, pady=20)
    tree_frame.pack(side=TOP)
    #!--------------------------------------------

    field_frame_r = Frame(root, width=500, relief=FLAT)
    field_frame_r.pack(side=TOP)

    #! Button Frame
    button_frame_r = Frame(root, width=700, pady=10, relief=FLAT)
    button_frame_r.pack(side=TOP)
    #!---------------------------------------------

    #! Submittion Button
    ref_btn = Button(button_frame_r, font=('Verdana', 14),
                     text="Refresh Record", command=refresh_tree)
    ref_btn.grid(row=0, column=0)
    #!---------------------------------------------------------

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    tv = ttk.Treeview(tree_frame, columns=(1, 2, 3), show="headings",
                      height=10, yscrollcommand=tree_scroll.set)
    tv.pack(side=TOP)

    tree_scroll.config(command=tv.yview)

    tv.heading(1, text="Vehicle No.")
    tv.heading(2, text="Vehicle Owner")
    tv.heading(3, text="Vehicle Type")

    tv.column(1, anchor=CENTER)
    tv.column(2, anchor=CENTER)
    tv.column(3, anchor=CENTER)

    # tple = (1, 2, "waqad")
    # tv.insert('', 'end', values=tple)

    dictionary_data = readData()
    for k in dictionary_data.keys():
        temp_list = [k, dictionary_data[k][0], dictionary_data[k][1]]
        print(k, dictionary_data[k][0], dictionary_data[k][1])
        tv.insert('', 'end', values=temp_list)

    vfeeval_entry_lbl = Label(field_frame_r, font=('arial', 14, 'bold'), justify="left",
                              text="Total Vehicle Fee Earned from Removed Vehicles:", fg="black",
                              bd=10, anchor="w")
    vfeeval_entry_lbl.grid(row=1, column=0)

    vfeeval_entry = Entry(field_frame_r, font=('arial', 14), width=16,
                          textvariable="feeval", justify="left", state="disable")
    vfeeval_entry.grid(row=1, column=1)

    rem_file = open("remove_data.json", "r")
    output = json.load(rem_file)
    rem_data = output
    rem_file.close()

    for k in rem_data.keys():
        feeval += rem_data[k][2]['fee']
        print("feeval is: {}".format(feeval))

    vfeeval_entry.config(state="normal")
    vfeeval_entry.delete(0, 'end')
    vfeeval_entry.insert(0, feeval)
    vfeeval_entry.config(state="disable")
