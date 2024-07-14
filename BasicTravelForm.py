from tkinter import *
root = Tk()
root.geometry("600x600")
heading=Label(text="Welcome to our Travel's Company",font="comicsansms 20 bold")
heading.grid(row=0,column=5)


name=Label(text="Name:")
name.grid(row=4,column=5)
nameentry=Entry(root,textvariable=StringVar())
nameentry.grid(row=4,column=6)

phone=Label(text="Phone No.")
phone.grid(row=5,column=5)
phoneentry=Entry(root,textvariable=IntVar())
phoneentry.grid(row=5,column=6)

gender=Label(text="Gender:")
gender.grid(row=6,column=5)
genderentry=Entry(root,textvariable=StringVar())
genderentry.grid(row=6,column=6)

EmergencyContact=Label(text="Emergency Contact:")
EmergencyContact.grid(row=7,column=5)
EmergencyContactEntry=Entry(root,textvariable=IntVar())
EmergencyContactEntry.grid(row=7,column=6)

Paymentmode=Label(text="Payment Mode:")
Paymentmode.grid(row=8,column=5)
PaymentmodeEntry=Entry(root,textvariable=StringVar())
PaymentmodeEntry.grid(row=8,column=6)

# Submit Button 

def getvals():
    print("Submitting Form")
    print(nameentry.get())
    print(phoneentry.get())
    print(genderentry.get())
    print(EmergencyContactEntry.get())
    print(PaymentmodeEntry.get())
    with open("Records.txt","w") as f:
        f.write(f"{nameentry.get(),phoneentry.get(),genderentry.get(),EmergencyContactEntry.get(),PaymentmodeEntry.get()}")
        
        
submit = Button(text="Submit",command=getvals)
submit.grid(row=12,column=6)

# Check Box
foodService=Checkbutton(text="Want to book your meals",variable=IntVar())
foodService.grid(row=10,column=6)

root.mainloop()