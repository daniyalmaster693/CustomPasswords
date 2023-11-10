from tkinter import *
import customtkinter
import secrets
import string
import os


app = customtkinter.CTk ()
app.geometry ("1000x700")
app.title ("Custom Passwords")


icon_path = app, ("Custom Passwords Icon.ico")


customtkinter.set_appearance_mode ("System")
customtkinter.set_default_color_theme ("dark-blue")


def raise_frame (frame):
    frame.tkraise ()


def close_program ():
    app.quit()


def change_appearance_mode (new_appearance_mode: str):
    customtkinter.set_appearance_mode (new_appearance_mode)


def change_scaling_mode (new_scaling_mode: str):
    new_scaling_float = int (new_scaling_mode.replace ("%", "")) /100
    customtkinter.set_widget_scaling (new_scaling_float)


def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)


def copy_password_to_clipboard ():
    password = textbox_1.get ("1.0", "end - 1c")
    app.clipboard_clear ()
    app.clipboard_append (password)
    app.update ()





password_label = []


def add_password ():
    password = entry_1.get ()
    entry_1.delete (0, customtkinter.END)
    Label = customtkinter.CTkLabel (scrollable_frame_1, text = password)
    Label.pack ()
    password_label.append (Label)


def delete_password (Label):
    if password_label:
        Label = password_label [-1]
        Label.destroy ()
        password_label.pop ()


def generate_password (length, use_letters = True, use_numbers = True, use_symbols = False):
    characters = ""


    use_letters = password_generator_switch_1.get () == "Yes"
    use_numbers = password_generator_switch_2.get () == "Yes"
    use_symbols = password_generator_switch_3.get () == "Yes"


    if use_letters:
        characters += string.ascii_letters


    if use_numbers:
        characters += string.digits


    if use_symbols:
        characters += string.punctuation


    if not characters:
        raise ValueError ("You must select a character, number or symbol to create your password")
    
    
    password = ''.join(secrets.choice (characters) for _ in range (length))
    return password





def generate_password_button_clicked ():
    

    use_letters = password_generator_switch_1.get () == "Yes"
    use_numbers = password_generator_switch_2.get () == "Yes"
    use_symbols = password_generator_switch_3.get () == "Yes"

    
    error_message = ""


    if not (use_letters or use_numbers or use_symbols):
        error_message = "You must select at least one switch in order to generate a password"


        textbox_3.configure (state = "normal")
        textbox_3.delete (1.0, END)
        textbox_3.insert (END, error_message)
        textbox_3.configure (state = "disabled")

        
        textbox_2.configure (state = "normal")
        textbox_2.delete (1.0, END)
        textbox_2.configure (state = "disabled")


        return

    
    try:
        password_length = int (entry_2.get())
        if 1 <= password_length <= 12:
            password = generate_password (password_length)
            entry_2.delete (0, END)

           
            textbox_1.configure (state = "normal")
            textbox_1.delete (1.0, END)
            textbox_1.insert (END, password)
            textbox_1.configure (state = "disabled")


            Label = customtkinter.CTkLabel (scrollable_frame_2, text = password)
            Label.pack ()
            password_label.append (Label)

            
            textbox_2.configure (state = "normal")
            textbox_2.delete (1.0, END)
            textbox_2.configure (state = "disabled")


            textbox_3.configure(state = "normal")
            textbox_3.delete(1.0, END)
            textbox_3.configure(state = "disabled")

            password_generator_switch_1.deselect ()
            password_generator_switch_2.deselect ()
            password_generator_switch_3.deselect ()


            raise_frame (f6)
        

        else:
            error_message = "Please enter a valid number between 1 and 12"
            
            
            textbox_2.configure (state = "normal")
            textbox_2.delete (1.0, END)
            textbox_2.insert (END, error_message)
            textbox_2.configure (state = "disabled")
           
               
    except ValueError:
        error_message = "Please enter a number between 1 and 12"
       
       
        textbox_2.configure(state = "normal")
        textbox_2.delete(1.0, END)
        textbox_2.insert(END, error_message)
        textbox_2.configure(state = "disabled")





f1 = customtkinter.CTkFrame (app, bg_color = "black", height = 1000, width = 1000)
f2 = customtkinter.CTkFrame (app, bg_color = "black", height = 1000, width = 1000)
f3 = customtkinter.CTkFrame (app, bg_color = "black", height = 1000, width = 1000)
f4 = customtkinter.CTkFrame (app, bg_color = "black", height = 1000, width = 1000)
f5 = customtkinter.CTkFrame (app, bg_color = "black", height = 1000, width = 1000)
f6 = customtkinter.CTkFrame (app, bg_color = "black", height = 1000, width = 1000)


for frame in (f1, f2, f3, f4, f5, f6):
    frame.grid (row = 10, column = 0, pady = 2, padx = 10, sticky = "news")





title_label_1 = customtkinter.CTkLabel (f1, text = "Custom Passwords", bg_color = "transparent",font = ("Roboto", 24), height = 40, width = 1000, 
                        padx = 12, pady = 10, anchor = customtkinter.CENTER)
title_label_1.place (x = 15,  y = 30, anchor = "nw")


title_label_2 = customtkinter.CTkLabel (f2, text = "Generate a Password", bg_color = "transparent",font = ("Roboto", 24), height = 40, width = 1000, 
                        padx = 12, pady = 10, anchor = customtkinter.CENTER)
title_label_2.place (x = 15,  y = 30, anchor = "nw")


title_label_3 = customtkinter.CTkLabel (f3,  text = "Viewing Created Passwords", bg_color = "transparent",font = ("Roboto", 24), height = 40, width = 1000, 
                        padx = 12, pady = 10, anchor = customtkinter.CENTER)
title_label_3.place (x = 15,  y = 30, anchor = "nw")


title_label_4 = customtkinter.CTkLabel (f4, text = "Viewing Saved Passwords", bg_color = "transparent",font = ("Roboto", 24), height = 40, width = 1000, 
                        padx = 12, pady = 10, anchor = customtkinter.CENTER)
title_label_4.place (x = 15,  y = 30, anchor = "nw")


title_label_5 = customtkinter.CTkLabel (f5, text = "Settings", bg_color = "transparent", font = ("Roboto", 24), height = 40, width = 1000, 
                        padx = 12, pady = 10, anchor = customtkinter.CENTER)
title_label_5.place (x = 15,  y = 30, anchor = "nw")


title_label_6 = customtkinter.CTkLabel (f6, text = "Here is your password", bg_color = "transparent", font = ("Roboto", 24), height = 40, width = 1000, 
                        padx = 12, pady = 10, anchor = customtkinter.CENTER)
title_label_6.place (x = 15,  y = 30, anchor = "nw")





verision_label_1 = customtkinter.CTkLabel (f5,text = "Verision: Developement", bg_color = "transparent", font = ("Roboto", 16), height = 40, width = 1000, 
                        padx = 12, pady = 10, anchor = customtkinter.CENTER)
verision_label_1.place (x = 8,  y = 640, anchor = "nw")


password_entry_example_1 = customtkinter.CTkLabel (f4,text = "Enter your password like this:  Google - 12345", bg_color = "transparent", font = ("Roboto", 16), height = 40, width = 1000, 
                        padx = 12, pady = 10, anchor = customtkinter.CENTER)
password_entry_example_1.place (x = 6,  y = 572, anchor = "nw")


password_entry_notice_1 = customtkinter.CTkLabel (f3,text = "Created passwords must be saved manually", bg_color = "transparent", font = ("Roboto", 16), height = 40, width = 1000, 
                        padx = 12, pady = 10, anchor = customtkinter.CENTER)
password_entry_notice_1.place (x = 8,  y = 470, anchor = "nw")


password_length_notice_1 = customtkinter.CTkLabel (f2,text = "Enter a number between 1 and 12 as the length of your password", 
                                                   bg_color = "transparent", font = ("Roboto", 16), height = 40, width = 1000, 
                                                   padx = 12, pady = 10, anchor = customtkinter.CENTER)
password_length_notice_1.place (x = 12,  y = 200, anchor = "nw")





button_1 = customtkinter.CTkButton (f1, text = "Generate a Password", font = ("Roboto", 18), fg_color = "blue", 
                                    hover_color = "gray", text_color = "white", height = 40, width = 210, anchor = customtkinter.CENTER, 
                                    command = lambda: raise_frame (f2))
button_1.place (x = 415, y = 200, anchor = "nw")


button_2 = customtkinter.CTkButton (f1, text = "View Created Passwords", font = ("Roboto", 18), fg_color = "blue", 
                                    hover_color = "gray", text_color = "white", height = 40, width = 210, anchor = customtkinter.CENTER, corner_radius = 6,
                                    command = lambda: raise_frame (f3))
button_2.place (x = 415,  y = 250, anchor = "nw")


button_3 = customtkinter.CTkButton (f1, text = "View Saved Passwords", font = ("Roboto", 18), fg_color = "blue", 
                                    hover_color = "gray", text_color = "white", height = 40, width = 210, anchor = customtkinter.CENTER, corner_radius = 6,
                                    command = lambda: raise_frame (f4))
button_3.place (x = 415,  y = 300, anchor = "nw")


button_4 = customtkinter.CTkButton (f1, text = "Settings", font = ("Roboto", 18), fg_color = "blue", 
                                    hover_color = "gray", text_color = "white", height = 40, width = 210, anchor = customtkinter.CENTER, corner_radius = 6,
                                    command = lambda: raise_frame (f5))
button_4.place (x = 415,  y = 350, anchor = "nw")


button_5 = customtkinter.CTkButton (f1, text = "Exit", font = ("Roboto", 18), fg_color = "blue", 
                                    hover_color = "gray", text_color = "white", height = 40, width = 210, anchor = customtkinter.CENTER, corner_radius = 6,
                                    command = close_program)
button_5.place (x = 415,  y = 400, anchor = "nw")





back_button_1 = customtkinter.CTkButton (f2, text = "Back", font = ("Roboto", 16), fg_color = "blue", 
                                    hover_color = "gray", text_color = "white", height = 40, width = 65, anchor = customtkinter.CENTER, corner_radius = 6,
                                    command = lambda: raise_frame (f1))
back_button_1.place (x = 15,  y = 650, anchor = "nw")


back_button_2 = customtkinter.CTkButton (f3, text = "Back", font = ("Roboto", 16), fg_color = "blue", 
                                    hover_color = "gray", text_color = "white", height = 40, width = 65, anchor = customtkinter.CENTER, corner_radius = 6,
                                    command = lambda: raise_frame (f1))
back_button_2.place (x = 15,  y = 650, anchor = "nw")


back_button_3 = customtkinter.CTkButton (f4, text = "Back", font = ("Roboto", 16), fg_color = "blue", 
                                    hover_color = "gray", text_color = "white", height = 40, width = 65, anchor = customtkinter.CENTER, corner_radius = 6,
                                    command = lambda: raise_frame (f1))
back_button_3.place (x = 15,  y = 650, anchor = "nw")


back_button_4 = customtkinter.CTkButton (f5, text = "Back", font = ("Roboto", 16), fg_color = "blue", 
                                    hover_color = "gray", text_color = "white", height = 40, width = 65, anchor = customtkinter.CENTER, corner_radius = 6,
                                    command = lambda: raise_frame (f1))
back_button_4.place (x = 15,  y = 650, anchor = "nw")


back_button_4 = customtkinter.CTkButton (f6, text = "Back", font = ("Roboto", 16), fg_color = "blue", 
                                    hover_color = "gray", text_color = "white", height = 40, width = 65, anchor = customtkinter.CENTER, corner_radius = 6,
                                    command = lambda: raise_frame (f2))
back_button_4.place (x = 15,  y = 650, anchor = "nw")





save_button_1 = customtkinter.CTkButton (f5, text = "Save Settings", font = ("Roboto", 16), fg_color = "#aed2b0", 
                                    hover_color = "gray", text_color = "white", height = 40, width = 65, anchor = customtkinter.CENTER, corner_radius = 6)
save_button_1.place (x = 90,  y = 650, anchor = "nw")


copy_button_1 = customtkinter.CTkButton (f6, text = "Copy Password", font = ("Roboto", 16), fg_color = "#aed2b0", 
                                    hover_color = "gray", text_color = "white", height = 40, width = 65, anchor = customtkinter.CENTER, corner_radius = 6, 
                                    command = copy_password_to_clipboard)
copy_button_1.place (x = 170,  y = 650, anchor = "nw")


home_button_1 = customtkinter.CTkButton (f6, text = "Home", font = ("Roboto", 16), fg_color = "blue", 
                                    hover_color = "gray", text_color = "white", height = 40, width = 65, anchor = customtkinter.CENTER, corner_radius = 6,  
                                    command = lambda: raise_frame (f1))
home_button_1.place (x = 92,  y = 650, anchor = "nw")


generate_password_button_1 = customtkinter.CTkButton (f2, text = "Generate Password", font = ("Roboto", 16), fg_color = "#aed2b0", 
                                    hover_color = "gray", text_color = "white", height = 40, width = 160, anchor = customtkinter.CENTER, corner_radius = 6,
                                    command = generate_password_button_clicked)
generate_password_button_1.place (x = 440,  y = 505, anchor = "nw")


add_password_button_1 = customtkinter.CTkButton (f4, text = "Add Password", font = ("Roboto", 16), fg_color = "#6ea4e0", 
                                    hover_color = "gray", text_color = "white", height = 35, width = 65, anchor = customtkinter.CENTER,
                                    corner_radius = 6, command = add_password)
add_password_button_1.place (x = 460, y = 200 )


delete_password_button_1 = customtkinter.CTkButton (f4, text = "Delete Password", font = ("Roboto", 16), fg_color = "#aed2b0",
                                    hover_color = "gray", text_color = "white", height = 35, width = 65, anchor = customtkinter.CENTER,
                                    corner_radius = 6,  command = lambda: delete_password (Label))
delete_password_button_1.place (x = 697,  y = 575)





password_generator_switch_1 = customtkinter.CTkSwitch (f2, text = "Include letters in your password", fg_color = "#6ea4e0", 
                                                       progress_color = "#fed600", corner_radius = 20, onvalue= "Yes", offvalue = "No")
password_generator_switch_1.place (x = 400, y = 305, anchor = "nw")


password_generator_switch_2 = customtkinter.CTkSwitch (f2, text = "Include numbers in your password", fg_color = "#6ea4e0", 
                                                       progress_color = "#fed600", corner_radius = 20, onvalue= "Yes", offvalue = "No")
password_generator_switch_2.place (x = 400, y = 355, anchor = "nw")


password_generator_switch_3 = customtkinter.CTkSwitch (f2, text = "Include punctuation in your password", fg_color = "#6ea4e0", 
                                                       progress_color = "#fed600", corner_radius = 20, onvalue= "Yes", offvalue = "No")
password_generator_switch_3.place (x = 400, y = 405, anchor = "nw")





settings_optionmenu_1 = customtkinter.CTkOptionMenu (f5, values = ["Dark", "Light", "System"], 
                                            height = 30, width = 75, fg_color = "#6ea4e0", corner_radius = 6, command = change_appearance_mode)
settings_optionmenu_1.set ("Select an appearance mode")
settings_optionmenu_1.place (x = 400, y = 150, anchor = "nw")


settings_optionmenu_2 = customtkinter.CTkOptionMenu (f5, values = ["80%", "85%", "90%", "95%", "100%", "110%"], 
                                            height = 30, width = 75, fg_color = "#6ea4e0", corner_radius = 6, command = change_scaling_mode)
settings_optionmenu_2.set ("Scale the UI")
settings_optionmenu_2.place (x = 400, y = 200, anchor = "nw")





scrollable_frame_1 = customtkinter.CTkScrollableFrame (f4, width = 600, height = 275, corner_radius = 6)
scrollable_frame_1.place (x = 210, y = 280, anchor = "nw")


scrollable_frame_2 = customtkinter.CTkScrollableFrame (f3, width = 700, height = 300, corner_radius = 6)
scrollable_frame_2.place (x = 137, y = 150, anchor = "nw")





entry_1 = customtkinter.CTkEntry (f4, font = ("Roboto", 16), height = 30, width = 163, text_color = "white", corner_radius = 6, 
                                  placeholder_text = "Enter your password")
entry_1.place (x = 435, y = 160, anchor = "nw")


entry_2 = customtkinter.CTkEntry (f2, font = ("Roboto", 16), height = 30, width = 130, text_color = "white", corner_radius = 6)
entry_2.place (x = 450, y = 150, anchor = "nw")


textbox_1 = customtkinter.CTkTextbox (f6, font = ("Roboto", 16), height = -15, width = 400, text_color = "white", corner_radius = 6)
textbox_1.configure (state = "disabled")
textbox_1.place (x = 317, y = 160, anchor = "nw")


textbox_2 = customtkinter.CTkTextbox (f2, font = ("Roboto", 16), height = -15, width = 350, text_color = "white", corner_radius = 6)
textbox_2.configure (state = "disabled")
textbox_2.place (x = 340, y = 250, anchor = "nw")


textbox_3 = customtkinter.CTkTextbox (f2, font = ("Roboto", 16), height = -15, width = 505, text_color = "white", corner_radius = 6)
textbox_3.configure (state = "disabled")
textbox_3.place (x = 265, y = 448, anchor = "nw")





raise_frame (f1)
app.mainloop ()