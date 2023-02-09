class UpdateWindow:
def _init_(self, id):
self.window = tkinter.Tk()
self.window.wm_title("Update data")
bg_color = "Blue"
fg_color = "white"

# Initializing all the variables
self.id = id

self.firstname = tkinter.StringVar()
self.lastname = tkinter.StringVar()
self.address = tkinter.StringVar()
self.contactNumber = tkinter.StringVar()
self.emailAddress = tkinter.StringVar()
self.history = tkinter.StringVar()
self.doctor = tkinter.StringVar()

self.genderType = ["Male", "Female", "Transgender", "Other"]
self.dateType = list(range(1, 32))
self.monthType = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
"October", "November", "December"]
self.yearType = list(range(1900, 2020))
self.bloodListType = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]

# Labels
tkinter.Label(self.window, fg=fg_color, bg=bg_color, text="Patient Id", font=("times new roman", 10, "bold"),
width=25).grid(pady=5, column=1, row=1)
tkinter.Label(self.window, fg=fg_color, bg=bg_color, text="Patient First Name",
font=("times new roman", 10, "bold"), width=25).grid(pady=5, column=1, row=2)
tkinter.Label(self.window, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"),
text="Patient Last Name", width=25).grid(pady=5, column=1, row=3)
tkinter.Label(self.window, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"), text="Date of Birth",
width=25).grid(pady=5, column=1, row=4)
tkinter.Label(self.window, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"),
text="Month of Birth", width=25).grid(pady=5, column=1, row=5)
tkinter.Label(self.window, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"), text="Year of Birth",
width=25).grid(pady=5, column=1, row=6)
tkinter.Label(self.window, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"),
text="Patient Gender", width=25).grid(pady=5, column=1, row=7)
tkinter.Label(self.window, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"),
text="Patient Address", width=25).grid(pady=5, column=1, row=8)
tkinter.Label(self.window, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"),
text="Patient Contact Number", width=25).grid(pady=5, column=1, row=9)
tkinter.Label(self.window, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"),
text="Patient Email Address", width=25).grid(pady=5, column=1, row=10)
tkinter.Label(self.window, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"),
text="Patient Blood Type", width=25).grid(pady=5, column=1, row=11)
tkinter.Label(self.window, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"),
text="History of Patient", width=25).grid(pady=5, column=1, row=12)
tkinter.Label(self.window, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"),
text="Name of Doctor", width=25).grid(pady=5, column=1, row=13)

# Set previous values
self.database = Database()
self.searchResults = self.database.Search(id)

tkinter.Label(self.window, text=self.searchResults[0][1], width=25).grid(pady=5, column=2, row=2)
tkinter.Label(self.window, text=self.searchResults[0][2], width=25).grid(pady=5, column=2, row=3)
tkinter.Label(self.window, text=self.searchResults[0][3], width=25).grid(pady=5, column=2, row=4)
tkinter.Label(self.window, text=self.searchResults[0][4], width=25).grid(pady=5, column=2, row=5)
tkinter.Label(self.window, text=self.searchResults[0][5], width=25).grid(pady=5, column=2, row=6)
tkinter.Label(self.window, text=self.searchResults[0][6], width=25).grid(pady=5, column=2, row=7)
tkinter.Label(self.window, text=self.searchResults[0][7], width=25).grid(pady=5, column=2, row=8)
tkinter.Label(self.window, text=self.searchResults[0][8], width=25).grid(pady=5, column=2, row=9)
tkinter.Label(self.window, text=self.searchResults[0][9], width=25).grid(pady=5, column=2, row=10)
tkinter.Label(self.window, text=self.searchResults[0][10], width=25).grid(pady=5, column=2, row=11)
tkinter.Label(self.window, text=self.searchResults[0][11], width=25).grid(pady=5, column=2, row=12)
tkinter.Label(self.window, text=self.searchResults[0][12], width=25).grid(pady=5, column=2, row=13)


self.idEntry = tkinter.Entry(self.window, width=25, textvariable=self.id)
self.firstnameEntry = tkinter.Entry(self.window, width=25, textvariable=self.firstname)
self.lastnameEntry = tkinter.Entry(self.window, width=25, textvariable=self.lastname)
self.addressEntry = tkinter.Entry(self.window, width=25, textvariable=self.address)
self.contactNumberEntry = tkinter.Entry(self.window, width=25, textvariable=self.contactNumber)
self.emailAddressEntry = tkinter.Entry(self.window, width=25, textvariable=self.emailAddress)
self.historyEntry = tkinter.Entry(self.window, width=25, textvariable=self.history)
self.doctorEntry = tkinter.Entry(self.window, width=25, textvariable=self.doctor)

self.idEntry.grid(pady=5, column=3, row=1)
self.firstnameEntry.grid(pady=5, column=3, row=2)
self.lastnameEntry.grid(pady=5, column=3, row=3)
self.addressEntry.grid(pady=5, column=3, row=8)
self.contactNumberEntry.grid(pady=5, column=3, row=9)
self.emailAddressEntry.grid(pady=5, column=3, row=10)
self.historyEntry.grid(pady=5, column=3, row=12)
self.doctorEntry.grid(pady=5, column=3, row=13)

# Combobox
self.dateOfBirthBox = tkinter.ttk.Combobox(self.window, values=self.dateType, width=20)
self.monthOfBirthBox = tkinter.ttk.Combobox(self.window, values=self.monthType, width=20)
self.yearOfBirthBox = tkinter.ttk.Combobox(self.window, values=self.yearType, width=20)
self.genderBox = tkinter.ttk.Combobox(self.window, values=self.genderType, width=20)
self.bloodListBox = tkinter.ttk.Combobox(self.window, values=self.bloodListType, width=20)

self.dateOfBirthBox.grid(pady=5, column=3, row=4)
self.monthOfBirthBox.grid(pady=5, column=3, row=5)
self.yearOfBirthBox.grid(pady=5, column=3, row=6)
self.genderBox.grid(pady=5, column=3, row=7)
self.bloodListBox.grid(pady=5, column=3, row=11)

# Button
tkinter.Button(self.window, width=10, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"),
text="Insert", command=self.Insert).grid(pady=15, padx=5, column=1,
row=14)
tkinter.Button(self.window, width=10, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"),
text="Reset", command=self.Reset).grid(pady=15, padx=5, column=2, row=14)
tkinter.Button(self.window, width=10, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"),
text="Close", command=self.window.destroy).grid(pady=15, padx=5, column=3,
row=14)

self.window.mainloop() 
def selectname(): 

  

    name = {1: "Nilesh", 2: "Shanu"} 

    b = {1: "Food", 2: "Exercise"} 

  

    for key, value in name.items(): 

  

        # taking input of name 

        print("Press", key, "for", value, "\n", end="") 

  

    n = int(input("type here..")) 

  

    if n > 2: 

        print("error select 1 or 2") 

        exit() 

    else: 

        return n
        