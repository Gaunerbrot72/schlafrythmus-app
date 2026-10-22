import tkinter as tk
from tkinter import ttk

rules_1 = {
    'Getrennt':0,
    'Zusammen':1
}

rules_2 = {
    'Arbeitstage': {'Schlafstunden': 7, 'Einschlafzeit': 1},
    'Wochenende': {'Schlafstunden': 9, 'Einschlafzeit': 1}
}

root = tk.Tk()

root.title('Schlafrythmus')

root.geometry('300x200')

optionen_1 = ['Getrennt', 'Zusammen']
optionen_2 = ['Arbeitstage', 'Wochenende']

dropbox_1 = ttk.Combobox(root, values=optionen_1, state='readonly')
dropbox_1.set('Auswählen...')
dropbox_1.pack(pady=5)

dropbox_2 = ttk.Combobox(root, values=optionen_2, state='readonly')
dropbox_2.set('Auswählen...')
dropbox_2.pack(pady=5)

label = ttk.Label(root, text='Wann aufstehen?')
label.pack(pady=5)

frame_zeit = ttk.Frame(root)
frame_zeit.pack(pady=5)

spin_hh = ttk.Spinbox(
    frame_zeit,
    from_=0,
    to=23,
    wrap=True,
    width=3,
    format="%02.0f"  
)
spin_hh.set("12")
spin_hh.pack(side="left")

ttk.Label(frame_zeit, text=" : ", font=("Arial", 12, "bold")).pack(side="left")

spin_mm = ttk.Spinbox(
    frame_zeit,
    from_=0,
    to=59,
    wrap=True,
    width=3,
    format="%02.0f"
)
spin_mm.set("00")
spin_mm.pack(side="left")

def calculate(einschlafzeit:int, schlafzeit:int)->str:
    hour = int(spin_hh.get())
    bedtime = hour - (einschlafzeit + schlafzeit)
    if bedtime < 0:
        bedtime = 24 + bedtime
    return f'{bedtime}:{spin_mm.get()}'

def calculate_bedtime():
    if dropbox_1.get() != 'Auswählen...' and dropbox_2.get() != 'Auswählen...':
        add_presleep = rules_1[dropbox_1.get()]
        sleep_data = rules_2[dropbox_2.get()]
        einschlafzeit = sleep_data['Einschlafzeit'] + add_presleep
        schlafzeit = sleep_data['Schlafstunden']
        bedtime = calculate(einschlafzeit, schlafzeit)
        bedtime_label.config(text=bedtime)
    else:
        bedtime_label.config(text='Bitte überall etwas auswählen!')

calc_button = ttk.Button(root, text='Berechnen', command=calculate_bedtime)
calc_button.pack(pady=5)

bedtime_label = ttk.Label(root, text='')
bedtime_label.pack(pady=5)

root.mainloop()