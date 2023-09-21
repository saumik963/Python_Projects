from tkinter import *


def press():
    print(namev.get(), phonev.get(), genderv.get(),
          emrv.get(), paymentv.get(), service_value.get())

    try:
        with open("records.txt", "a") as f:  # Updated file path here
            data = f"{namev.get()}, {phonev.get()}, {genderv.get()}, {emrv.get()}, {paymentv.get()}, {service_value.get()}\n"
            f.write(data)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


root = Tk()

root.geometry("344x200")
root.maxsize(344, 200)

# Form labels
Label(root, text="Welcome to ABC Travels.",
      font="arial 13 bold").grid(row=0, column=3)
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emr = Label(root, text="Emergency Contact")
payment = Label(root, text="Payment Method")

# Pack all labels
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emr.grid(row=4, column=2)
payment.grid(row=5, column=2)

# Set entry form variables for Tkinter to store input
namev = StringVar()
phonev = StringVar()
genderv = StringVar()
emrv = StringVar()
paymentv = StringVar()
service_value = IntVar()

# Form entries
nameentry = Entry(root, textvariable=namev)
phoneentry = Entry(root, textvariable=phonev)
genderentry = Entry(root, textvariable=genderv)
emrentry = Entry(root, textvariable=emrv)
paymententry = Entry(root, textvariable=paymentv)

# packing entries
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emrentry.grid(row=4, column=3)
paymententry.grid(row=5, column=3)

# Checkbox
service = Checkbutton(text="Prebook Meals here.", variable=service_value)
service.grid(row=6, column=3)
Button(text="Submit", command=press).grid(row=7, column=3)

root.mainloop()
