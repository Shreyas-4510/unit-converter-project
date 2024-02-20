import customtkinter
from tkinter import *
from tkinter import messagebox

app=customtkinter.CTk()
app.title('unit Converter')
app.geometry('500x450')
app.config(bg='#020a24')

font1=('Arial',30,'bold')
font2=('Arial',25,'bold')
font3=('Arial',20,'bold')

unit_options=['Length','Mass']
length_options=['meter','centimeter','foot','inches','squareft','squaremtr','acre']
mass_options=['kilogram','gram','pound']
variable1=StringVar()
variable2=StringVar()
variable3=StringVar()

def convert():
    length_factors={'meter':1,'centimeter':0.01,'feet':0.3048,'inches':2.54,'squareft':0.0929,'squaremtr':10.76391042,'acre':4}
    mass_factors={'kilogram':1,'gram':0.001,'pound':0.453592}
    try:
        if variable1.get()=='Length':
            meters=float(value_entry.get())*length_factors[variable2.get()]
            #convert from meter to the desried unit
            converted_value=meters/length_factors[variable3.get()]
        else:
            kilograms=float(value_entry.get())*mass_factors[variable2.get()]
            #convert from kilograms to the desried unit
            converted_value=kilograms/mass_factors[variable3.get()]
        result_label.configure(text=f'{value_entry.get()} {variable2.get()} ={converted_value:.2f} {variable3.get()}')
    except:
        messagebox.showerror('error','enter valid values!')

title_label=customtkinter.CTkLabel(app,font=font1,text='Unit Converter',text_color='#fff',bg_color='#020a24')
title_label.place(x=150,y=20)

unit_label=customtkinter.CTkLabel(app,font=font2,text='unit',text_color='#fff',bg_color='#020a24')
unit_label.place(x=180,y=100)

unit_option=customtkinter.CTkComboBox(app,font=font3,text_color='#000',fg_color='#fff',dropdown_hover_color='#06911f',values=unit_options,variable=variable1,width=120)
unit_option.place(x=180,y=130)

from_label=customtkinter.CTkLabel(app,font=font2,text='from',text_color='#fff',bg_color='#020a24')
from_label.place(x=20,y=180)

from_option=customtkinter.CTkComboBox(app,font=font3,text_color='#000',fg_color='#fff',dropdown_hover_color='#06911f',variable=variable2,width=120)
from_option.place(x=20,y=210)

to_label=customtkinter.CTkLabel(app,font=font2,text='TO',text_color='#fff',bg_color='#020a24')
to_label.place(x=180,y=180)

to_option=customtkinter.CTkComboBox(app,font=font3,text_color='#000',fg_color='#fff',dropdown_hover_color='#06911f',variable=variable3,width=120)
to_option.place(x=180,y=210)

value_label=customtkinter.CTkLabel(app,font=font1,text='Value',text_color='#fff',bg_color='#020a24')
value_label.place(x=340,y=180)

value_entry=customtkinter.CTkEntry(app,font=font3,text_color='#000',fg_color='#fff',border_color='#fff',width=120)
value_entry.place(x=340,y=210)

convert_button=customtkinter.CTkButton(app,command=convert,font=font2,text_color='#fff',text='convert',fg_color='#eb05ae',hover_color='#a8057d',bg_color='#020a24',cursor='hand2',corner_radius=10,width=200)
convert_button.place(x=150,y=280)

result_label=customtkinter.CTkLabel(app,font=font2,text='',text_color='#fff',bg_color='#020a24')
result_label.place(x=130,y=350)

def update_options(*args):
    if variable1.get()=='Length':
        from_option.configure(values=length_options)
        to_option.configure(values=length_options)
        from_option.set('meter')
        to_option.set('centimeter')
    else:
        from_option.configure(values=mass_options)
        to_option.configure(values=mass_options)
        from_option.set('kilogram')
        to_option.set('gram')
variable1.trace("w",update_options)



app.mainloop()