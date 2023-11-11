from tkinter import * # import the required libraries for the application
import customtkinter
import secrets
import string


app = customtkinter.CTk () # this tells the comptuter what the app variable will mean, and to use custom tkinter for the app as well as define CTk
app.geometry ("1000x700") # this code is used to create the size of the window for the app
app.title ("Custom Passwords") # this code is used to select what the title bar text should say


customtkinter.set_appearance_mode ("System") 
customtkinter.set_default_color_theme ("dark-blue") # sets the appearance of the app


def raise_frame (frame): # this function allows frames to be raised (allowing frame switching)
    frame.tkraise ()


def close_program (): # this function allows the exit button to close the application
    app.quit()


def change_appearance_mode (new_appearance_mode: str): # this fucntion allows the settings option menu for appearance modes to chnage the mode from dark to light
    customtkinter.set_appearance_mode (new_appearance_mode)


def change_scaling_mode (new_scaling_mode: str): # this function allows the settings scaling option menu to change the scale of text and buttons
    new_scaling_float = int (new_scaling_mode.replace ("%", "")) /100 #
    customtkinter.set_widget_scaling (new_scaling_float)


def copy_password_to_clipboard (): # this function allows the copy button to take the text from a textbox and copy it to your clipboard
    password = textbox_1.get ("1.0", "end - 1c")
    app.clipboard_clear ()
    app.clipboard_append (password)
    app.update ()





password_label = []


def add_password (): # this function allows you to add a password to the scrollable frame in order to save passwords
    password = entry_1.get ()
    entry_1.delete (0, customtkinter.END)
    Label = customtkinter.CTkLabel (scrollable_frame_1, text = password)
    Label.pack ()
    password_label.append (Label)


def delete_password (Label): # this function allows you to delete a password from the scrollable frame
    if password_label:
        Label = password_label [-1]
        Label.destroy ()
        password_label.pop ()


def generate_password (length, use_letters = True, use_numbers = True, use_symbols = False): # this loop is used to generate the password
    characters = ""


    use_letters = password_generator_switch_1.get () == "Yes" # this code is used to allow the user to determine what is included in the password
    use_numbers = password_generator_switch_2.get () == "Yes"
    use_symbols = password_generator_switch_3.get () == "Yes"


    if use_letters: # this code tells the computer what to do if a user selects the use letters parameter
        characters += string.ascii_letters


    if use_numbers: # this code tells the computer what to do if a user selects the use numbers parameter
        characters += string.digits


    if use_symbols: # this code tells the computer what to do if a user selects the use punctuation parameter
        characters += string.punctuation


    if not characters: # this if statement provides an error message in a textbox telling the user what is required in order to create a password
        raise ValueError ("You must select a character, number or symbol to create your password")
    
    
    password = ''.join(secrets.choice (characters) for _ in range (length)) # this code tells the computer what to use and how to make the password
    return password





def generate_password_button_clicked (): # this function controls everything that happens when you click generate password
    

    use_letters = password_generator_switch_1.get () == "Yes" # this code gets the computer to take the user's set parameters to generate the password
    use_numbers = password_generator_switch_2.get () == "Yes"
    use_symbols = password_generator_switch_3.get () == "Yes"

    
    error_message = ""


    if not (use_letters or use_numbers or use_symbols): # this code gives the user an error message when a parameter is not selected
        error_message = "You must select at least one switch in order to generate a password"


        textbox_3.configure (state = "normal") # this code allows the texbox for the password to clear once the password has been generated
        textbox_3.delete (1.0, END)
        textbox_3.insert (END, error_message)
        textbox_3.configure (state = "disabled")

        
        textbox_2.configure (state = "normal") # this code allows the texbox for the password to clear once the password has been generated
        textbox_2.delete (1.0, END)
        textbox_2.configure (state = "disabled")


        return

    
    try:
        password_length = int (entry_2.get()) # this code is used to grab the input from the user for the length of the password
        if 1 <= password_length <= 12:
            password = generate_password (password_length)
            entry_2.delete (0, END)

           
            textbox_1.configure (state = "normal") # this textbox is used to show the password to the user and clear the textbox once the frame has been exited
            textbox_1.delete (1.0, END)
            textbox_1.insert (END, password)
            textbox_1.configure (state = "disabled")


            Label = customtkinter.CTkLabel (scrollable_frame_2, text = password) # this code allows generated passwords to show up in the view created passwords frame
            Label.pack ()
            password_label.append (Label)

            
            textbox_2.configure (state = "normal")
            textbox_2.delete (1.0, END)
            textbox_2.configure (state = "disabled")


            textbox_3.configure(state = "normal")
            textbox_3.delete(1.0, END)
            textbox_3.configure(state = "disabled")


            password_generator_switch_1.deselect () # this code is used to deslect the switches once the frame has been exited and the password has been generated to its default state
            password_generator_switch_2.deselect ()
            password_generator_switch_3.deselect ()


            raise_frame (f6) # this code tells the computer what frame to show when the password has been generated
        

        else:
            error_message = "Please enter a valid number between 1 and 12" # this code gives the user an error message if the input for the length of the password is not valid
            
            
            textbox_2.configure (state = "normal") # this code is used to clear and update the textbox depending on what has happend (password has been generated or if the input is valid)
            textbox_2.delete (1.0, END)
            textbox_2.insert (END, error_message)
            textbox_2.configure (state = "disabled")
           
               
    except ValueError:
        error_message = "Please enter a number between 1 and 12" 
       
       
        textbox_2.configure(state = "normal")
        textbox_2.delete(1.0, END)
        textbox_2.insert(END, error_message)
        textbox_2.configure(state = "disabled")





f1 = customtkinter.CTkFrame (app, bg_color = "black", height = 1000, width = 1000) # this code sets the size and appearance of each frame
f2 = customtkinter.CTkFrame (app, bg_color = "black", height = 1000, width = 1000)
f3 = customtkinter.CTkFrame (app, bg_color = "black", height = 1000, width = 1000)
f4 = customtkinter.CTkFrame (app, bg_color = "black", height = 1000, width = 1000)
f5 = customtkinter.CTkFrame (app, bg_color = "black", height = 1000, width = 1000)
f6 = customtkinter.CTkFrame (app, bg_color = "black", height = 1000, width = 1000)


for frame in (f1, f2, f3, f4, f5, f6): # this code adds further customization to each frame
    frame.grid (row = 10, column = 0, pady = 2, padx = 10, sticky = "news")





title_label_1 = customtkinter.CTkLabel (f1, text = "Custom Passwords", bg_color = "transparent",font = ("Roboto", 24), height = 40, width = 1000, 
                        padx = 12, pady = 10, anchor = customtkinter.CENTER)
title_label_1.place (x = 15,  y = 30, anchor = "nw") # this code is used to create labels as well as customize them


title_label_2 = customtkinter.CTkLabel (f2, text = "Generate a Password", bg_color = "transparent",font = ("Roboto", 24), height = 40, width = 1000, 
                        padx = 12, pady = 10, anchor = customtkinter.CENTER)
title_label_2.place (x = 15,  y = 30, anchor = "nw") # this code is used to create labels as well as customize them


title_label_3 = customtkinter.CTkLabel (f3,  text = "Viewing Created Passwords", bg_color = "transparent",font = ("Roboto", 24), height = 40, width = 1000, 
                        padx = 12, pady = 10, anchor = customtkinter.CENTER)
title_label_3.place (x = 15,  y = 30, anchor = "nw") # this code is used to create labels as well as customize them


title_label_4 = customtkinter.CTkLabel (f4, text = "Viewing Saved Passwords", bg_color = "transparent",font = ("Roboto", 24), height = 40, width = 1000, 
                        padx = 12, pady = 10, anchor = customtkinter.CENTER)
title_label_4.place (x = 15,  y = 30, anchor = "nw") # this code is used to create labels as well as customize them


title_label_5 = customtkinter.CTkLabel (f5, text = "Settings", bg_color = "transparent", font = ("Roboto", 24), height = 40, width = 1000, 
                        padx = 12, pady = 10, anchor = customtkinter.CENTER)
title_label_5.place (x = 15,  y = 30, anchor = "nw") # this code is used to create labels as well as customize them


title_label_6 = customtkinter.CTkLabel (f6, text = "Here is your password", bg_color = "transparent", font = ("Roboto", 24), height = 40, width = 1000, 
                        padx = 12, pady = 10, anchor = customtkinter.CENTER)
title_label_6.place (x = 15,  y = 30, anchor = "nw") # this code is used to create labels as well as customize them





verision_label_1 = customtkinter.CTkLabel (f5,text = "Verision: Developement", bg_color = "transparent", font = ("Roboto", 16), height = 40, width = 1000, 
                        padx = 12, pady = 10, anchor = customtkinter.CENTER)
verision_label_1.place (x = 8,  y = 640, anchor = "nw") # this code is used to create the label that shows the version of the app

password_entry_example_1 = customtkinter.CTkLabel (f4,text = "Enter your password like this:  Google - 12345", bg_color = "transparent", font = ("Roboto", 16), height = 40, width = 1000, 
                        padx = 12, pady = 10, anchor = customtkinter.CENTER)
password_entry_example_1.place (x = 6,  y = 572, anchor = "nw") # this code is used to give the user an example of how to save a password


password_entry_notice_1 = customtkinter.CTkLabel (f3,text = "Created passwords must be saved manually", bg_color = "transparent", font = ("Roboto", 16), height = 40, width = 1000, 
                        padx = 12, pady = 10, anchor = customtkinter.CENTER)
password_entry_notice_1.place (x = 8,  y = 470, anchor = "nw") # this code is used to tell the user that passwords must be saved manually


password_length_notice_1 = customtkinter.CTkLabel (f2,text = "Enter a number between 1 and 12 as the length of your password", 
                                                   bg_color = "transparent", font = ("Roboto", 16), height = 40, width = 1000, 
                                                   padx = 12, pady = 10, anchor = customtkinter.CENTER)
password_length_notice_1.place (x = 12,  y = 200, anchor = "nw") # this code is used to tell the user what integer should be entered for the length of the password





button_1 = customtkinter.CTkButton (f1, text = "Generate a Password", font = ("Roboto", 18), fg_color = "blue", 
                                    hover_color = "gray", text_color = "white", height = 40, width = 210, anchor = customtkinter.CENTER, 
                                    command = lambda: raise_frame (f2)) # this code is used to create a button as well as customize it
button_1.place (x = 415, y = 200, anchor = "nw") 


button_2 = customtkinter.CTkButton (f1, text = "View Created Passwords", font = ("Roboto", 18), fg_color = "blue", 
                                    hover_color = "gray", text_color = "white", height = 40, width = 210, anchor = customtkinter.CENTER, corner_radius = 6,
                                    command = lambda: raise_frame (f3)) # this code is used to create a button as well as customize it
button_2.place (x = 415,  y = 250, anchor = "nw")


button_3 = customtkinter.CTkButton (f1, text = "View Saved Passwords", font = ("Roboto", 18), fg_color = "blue", 
                                    hover_color = "gray", text_color = "white", height = 40, width = 210, anchor = customtkinter.CENTER, corner_radius = 6,
                                    command = lambda: raise_frame (f4)) # this code is used to create a button as well as customize it
button_3.place (x = 415,  y = 300, anchor = "nw")


button_4 = customtkinter.CTkButton (f1, text = "Settings", font = ("Roboto", 18), fg_color = "blue", 
                                    hover_color = "gray", text_color = "white", height = 40, width = 210, anchor = customtkinter.CENTER, corner_radius = 6,
                                    command = lambda: raise_frame (f5)) # this code is used to create a button as well as customize it
button_4.place (x = 415,  y = 350, anchor = "nw")


button_5 = customtkinter.CTkButton (f1, text = "Exit", font = ("Roboto", 18), fg_color = "blue", 
                                    hover_color = "gray", text_color = "white", height = 40, width = 210, anchor = customtkinter.CENTER, corner_radius = 6,
                                    command = close_program) # this code is used to create a button as well as customize it
button_5.place (x = 415,  y = 400, anchor = "nw")





back_button_1 = customtkinter.CTkButton (f2, text = "Back", font = ("Roboto", 16), fg_color = "blue", 
                                    hover_color = "gray", text_color = "white", height = 40, width = 65, anchor = customtkinter.CENTER, corner_radius = 6,
                                    command = lambda: raise_frame (f1)) # this code is used to take the user to the previous frame
back_button_1.place (x = 15,  y = 650, anchor = "nw")


back_button_2 = customtkinter.CTkButton (f3, text = "Back", font = ("Roboto", 16), fg_color = "blue", 
                                    hover_color = "gray", text_color = "white", height = 40, width = 65, anchor = customtkinter.CENTER, corner_radius = 6,
                                    command = lambda: raise_frame (f1)) # this code is used to take the user to the previous frame
back_button_2.place (x = 15,  y = 650, anchor = "nw")


back_button_3 = customtkinter.CTkButton (f4, text = "Back", font = ("Roboto", 16), fg_color = "blue", 
                                    hover_color = "gray", text_color = "white", height = 40, width = 65, anchor = customtkinter.CENTER, corner_radius = 6,
                                    command = lambda: raise_frame (f1)) # this code is used to take the user to the previous frame
back_button_3.place (x = 15,  y = 650, anchor = "nw")


back_button_4 = customtkinter.CTkButton (f5, text = "Back", font = ("Roboto", 16), fg_color = "blue", 
                                    hover_color = "gray", text_color = "white", height = 40, width = 65, anchor = customtkinter.CENTER, corner_radius = 6,
                                    command = lambda: raise_frame (f1)) # this code is used to take the user to the previous frame
back_button_4.place (x = 15,  y = 650, anchor = "nw")


back_button_4 = customtkinter.CTkButton (f6, text = "Back", font = ("Roboto", 16), fg_color = "blue", 
                                    hover_color = "gray", text_color = "white", height = 40, width = 65, anchor = customtkinter.CENTER, corner_radius = 6,
                                    command = lambda: raise_frame (f2)) # this code is used to take the user to the previous frame
back_button_4.place (x = 15,  y = 650, anchor = "nw")





save_button_1 = customtkinter.CTkButton (f5, text = "Save Settings", font = ("Roboto", 16), fg_color = "#aed2b0", 
                                    hover_color = "gray", text_color = "white", height = 40, width = 65, anchor = customtkinter.CENTER, corner_radius = 6)
save_button_1.place (x = 90,  y = 650, anchor = "nw") # this code is used to create a button as well as customize it


copy_button_1 = customtkinter.CTkButton (f6, text = "Copy Password", font = ("Roboto", 16), fg_color = "#aed2b0", 
                                    hover_color = "gray", text_color = "white", height = 40, width = 65, anchor = customtkinter.CENTER, corner_radius = 6, 
                                    command = copy_password_to_clipboard) # this code is used to create a button as well as customize it
copy_button_1.place (x = 170,  y = 650, anchor = "nw")


home_button_1 = customtkinter.CTkButton (f6, text = "Home", font = ("Roboto", 16), fg_color = "blue", 
                                    hover_color = "gray", text_color = "white", height = 40, width = 65, anchor = customtkinter.CENTER, corner_radius = 6,  
                                    command = lambda: raise_frame (f1)) # this code is used to create a button as well as customize it
home_button_1.place (x = 92,  y = 650, anchor = "nw")





generate_password_button_1 = customtkinter.CTkButton (f2, text = "Generate Password", font = ("Roboto", 16), fg_color = "#aed2b0", 
                                    hover_color = "gray", text_color = "white", height = 40, width = 160, anchor = customtkinter.CENTER, corner_radius = 6,
                                    command = generate_password_button_clicked) # this code is used to call the generated password button clicked function and use it to determine whether it can generate a password
generate_password_button_1.place (x = 440,  y = 505, anchor = "nw")


add_password_button_1 = customtkinter.CTkButton (f4, text = "Add Password", font = ("Roboto", 16), fg_color = "#6ea4e0", 
                                    hover_color = "gray", text_color = "white", height = 35, width = 65, anchor = customtkinter.CENTER,
                                    corner_radius = 6, command = add_password) # this code is used to add a password to the view created passwords frame
add_password_button_1.place (x = 460, y = 200 )


delete_password_button_1 = customtkinter.CTkButton (f4, text = "Delete Password", font = ("Roboto", 16), fg_color = "#aed2b0",
                                    hover_color = "gray", text_color = "white", height = 35, width = 65, anchor = customtkinter.CENTER,
                                    corner_radius = 6,  command = lambda: delete_password (Label)) # this code is used to delete a password in the view saved passwords frame
delete_password_button_1.place (x = 697,  y = 575)





password_generator_switch_1 = customtkinter.CTkSwitch (f2, text = "Include letters in your password", fg_color = "#6ea4e0", 
                                                       progress_color = "#fed600", corner_radius = 20, onvalue= "Yes", offvalue = "No")
password_generator_switch_1.place (x = 400, y = 305, anchor = "nw") # this code is used as a way for the user to select a parameter for the creation of a password


password_generator_switch_2 = customtkinter.CTkSwitch (f2, text = "Include numbers in your password", fg_color = "#6ea4e0", 
                                                       progress_color = "#fed600", corner_radius = 20, onvalue= "Yes", offvalue = "No")
password_generator_switch_2.place (x = 400, y = 355, anchor = "nw") # this code is used as a way for the user to select a parameter for the creation of a password


password_generator_switch_3 = customtkinter.CTkSwitch (f2, text = "Include punctuation in your password", fg_color = "#6ea4e0", 
                                                       progress_color = "#fed600", corner_radius = 20, onvalue= "Yes", offvalue = "No")
password_generator_switch_3.place (x = 400, y = 405, anchor = "nw") # this code is used as a way for the user to select a parameter for the creation of a password





settings_optionmenu_1 = customtkinter.CTkOptionMenu (f5, values = ["Dark", "Light", "System"], 
                                            height = 30, width = 75, fg_color = "#6ea4e0", corner_radius = 6, command = change_appearance_mode)
settings_optionmenu_1.set ("Select an appearance mode") # This code is used to allow the user to set the appearance of the app
settings_optionmenu_1.place (x = 400, y = 150, anchor = "nw") 


settings_optionmenu_2 = customtkinter.CTkOptionMenu (f5, values = ["80%", "85%", "90%", "95%", "100%", "110%"], 
                                            height = 30, width = 75, fg_color = "#6ea4e0", corner_radius = 6, command = change_scaling_mode)
settings_optionmenu_2.set ("Scale the UI") # this code is used to change the size of text and buttons in the app
settings_optionmenu_2.place (x = 400, y = 200, anchor = "nw")





scrollable_frame_1 = customtkinter.CTkScrollableFrame (f4, width = 600, height = 275, corner_radius = 6)
scrollable_frame_1.place (x = 210, y = 280, anchor = "nw") # this code is used to create a scrollable frame for viewing saved passwords


scrollable_frame_2 = customtkinter.CTkScrollableFrame (f3, width = 700, height = 300, corner_radius = 6)
scrollable_frame_2.place (x = 137, y = 150, anchor = "nw") # this code is used to create a scrollable frame for viewing created passwords





entry_1 = customtkinter.CTkEntry (f4, font = ("Roboto", 16), height = 30, width = 163, text_color = "white", corner_radius = 6, 
                                  placeholder_text = "Enter your password")
entry_1.place (x = 435, y = 160, anchor = "nw") # this code is used to allow the user to add a password to the view saved passwords frame


entry_2 = customtkinter.CTkEntry (f2, font = ("Roboto", 16), height = 30, width = 130, text_color = "white", corner_radius = 6)
entry_2.place (x = 450, y = 150, anchor = "nw") # this code is used to allow the user to input the length of the password they want to create





textbox_1 = customtkinter.CTkTextbox (f6, font = ("Roboto", 16), height = -15, width = 400, text_color = "white", corner_radius = 6)
textbox_1.configure (state = "disabled") # this code is used to create a textbox and customize it
textbox_1.place (x = 317, y = 160, anchor = "nw")


textbox_2 = customtkinter.CTkTextbox (f2, font = ("Roboto", 16), height = -15, width = 350, text_color = "white", corner_radius = 6)
textbox_2.configure (state = "disabled") # this code is used to create a textbox and customize it
textbox_2.place (x = 340, y = 250, anchor = "nw")


textbox_3 = customtkinter.CTkTextbox (f2, font = ("Roboto", 16), height = -15, width = 505, text_color = "white", corner_radius = 6)
textbox_3.configure (state = "disabled") # this code is used to create a textbox and customize it
textbox_3.place (x = 265, y = 448, anchor = "nw")





raise_frame (f1) # this code tells the computer what frame to show first when the app is launched
app.mainloop () 
