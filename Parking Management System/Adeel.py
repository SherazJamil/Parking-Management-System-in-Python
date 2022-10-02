
# # this is title page Div
# title_div = Frame(root, width=1600, relief=SUNKEN)
# title_div.pack(side=TOP)

# #this is text field div
# field_div = Frame(root, width=1600, relief=SUNKEN)
# field_div.pack(side=TOP)

# # set lable for Main Title
# lblInfo = Label(title_div, font=('helvetica', 30, 'bold'),
#                 text="Parking Management System",
#                 fg="Black", bd=10, anchor='w')
# lblInfo.grid(row=0, column=0)

# # set current time
# lblInfo = Label(title_div, font=('arial', 20, 'bold'),
#                 text="Date:"+localtime, fg="Steel Blue",
#                 bd=10, anchor='w')
# lblInfo.grid(row=1, column=0)

# # set field for vehical number
# lblReference = Label(field_div, font=('arial', 16, 'bold'),
#                      text="Name:", bd=16, anchor="w")
# lblReference.grid(row=0, column=0)
# txtReference = Entry(field_div, font=('arial', 16, 'bold'),
#                      textvariable="", bd=2, insertwidth=4,
#                      bg="white", justify='left')
# txtReference.grid(row=0, column=1)

# # set field for vehical type

# lblReference = Label(field_div, font=('arial', 16, 'bold'),
#                      text="V. Type:", bd=16, anchor="w")
# lblReference.grid(row=1, column=0)
# txtReference = Entry(field_div, font=('arial', 16, 'bold'),
#                      textvariable="", bd=4, insertwidth=4,
#                      bg="white", justify='left')
# txtReference.grid(row=1, column=1)

# # set fields for text price

# lblReference = Label(field_div, font=('arial', 16, 'bold'),
#                      text="Owner Name:", bd=16, anchor="w")
# lblReference.grid(row=2, column=0)
# txtReference = Entry(field_div, font=('arial', 16, 'bold'),
#                      textvariable="", bd=2, insertwidth=4,
#                      bg="white", justify='left')
# txtReference.grid(row=2, column=1)
# rand = StringVar()
# Msg = StringVar()
# key = StringVar()
# mode = StringVar()
# Result = StringVar()
