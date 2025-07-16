import tkinter
from tkinter import IntVar

# ====WINDOW====
window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=300,height=250)
window.config(pady=15)

# ====Labels and Entries====
label_w = tkinter.Label(text= "Enter Your Weight(kg)")
label_w.pack()


entry_w = tkinter.Entry(width=20)
entry_w.pack()

label_h = tkinter.Label(text= "Enter Your Height(cm)")
label_h.pack()

entry_h = tkinter.Entry(width=20)
entry_h.pack()

# ====BMI Calculator for Metric Units====
def bmi_calculator_MU():
    try:
        w = float(entry_w.get())
        h = float(entry_h.get()) / 100
        if h == 0 or w == 0:
            raise ValueError
        bmi = w / (h ** 2)

        if  bmi <18.5:
            label_bmi.config(text=f"Your BMI is {bmi} . You are underweight")

        elif 18.5 <= bmi < 25:
            label_bmi.config(text=f"Your BMI is {bmi} . You are normal weight")

        elif 25 <= bmi < 30:
            label_bmi.config(text=f"Your BMI is {bmi} . You are overweight")

        elif 30 <= bmi < 40:
            label_bmi.config(text=f"Your BMI is {bmi} . You are obese")

        elif 40 <= bmi:
            label_bmi.config(text=f"Your BMI is {bmi} . You are morbidly obese")

        label_error.config(text= "")
        label_bmi.pack()

    except:

        label_error.config(text="Please enter a valid number", font=("Arial",10,"italic") )
        label_error.pack()


# ====BMI Calculator for English Units====
def bmi_calculator_EU():
    try:

        w = float(entry_w.get())
        h = float(entry_h.get()) / 100
        if h == 0 or w == 0:
            raise ValueError
        bmi = 703 * w / (h ** 2)

        if bmi < 18.5:
            label_bmi.config(text=f"Your BMI is {bmi} . You are underweight")

        elif 18.5 <= bmi < 25:
            label_bmi.config(text=f"Your BMI is {bmi} . You are normal weight")

        elif 25 <= bmi < 30:
            label_bmi.config(text=f"Your BMI is {bmi} . You are overweight")

        elif 30 <= bmi < 40:
            label_bmi.config(text=f"Your BMI is {bmi} . You are obese")

        elif 40 <= bmi:
            label_bmi.config(text=f"Your BMI is {bmi} . You are morbidly obese")

        label_error.config(text="")
        label_bmi.pack()

    except:

        label_error.config(text="Please enter a valid number", font=("Arial", 10, "italic"))
        label_error.pack()

# ====Variables====
label_w_string = "Enter Your Weight(kg)"
label_h_string = "Enter Your Height(cm)"
current_fun = bmi_calculator_MU

# ====RadioButtons and Function Settings====
def radio_selected():
    global current_fun,label_w_string,label_h_string
    if radio_checked_state.get() == 10:
        current_fun = bmi_calculator_MU
        label_w_string = "Enter Your Weight(kg)"
        label_h_string = "Enter Your Height(cm)"
        label_w.config(text= label_w_string)
        label_h.config(text= label_h_string)

    elif radio_checked_state.get() == 20:
        current_fun = bmi_calculator_EU
        label_w_string = "Enter Your Weight(lbs)"
        label_h_string = "Enter Your Height(in)"
        label_w.config(text=label_w_string)
        label_h.config(text=label_h_string)


radio_checked_state = IntVar()
radiobutton = tkinter.Radiobutton(text="Metric Units", value=10, variable=radio_checked_state, command=radio_selected)
radiobutton_2 = tkinter.Radiobutton(text="English Units", value=20, variable=radio_checked_state, command=radio_selected)
radio_checked_state.set(10) # Radiobutton'da ilk seçili olanı ayarla (Metric Units)
radio_selected() # Seçim fonksiyonunu çağırır, label ve fonksiyonları günceller
radiobutton.pack()
radiobutton_2.pack()

label_bmi = tkinter.Label()
label_error = tkinter.Label(fg="red")

# ====Button====
button = tkinter.Button(text="Calculate",command= lambda: current_fun)
button.pack()

# ====Focus and Keyboard Settings====
entry_w.focus()
window.bind("<Up>",lambda event: entry_w.focus())
window.bind("<Down>",lambda  event: entry_h.focus())
window.bind("<Return>", lambda event:current_fun())

# ================
window.mainloop()