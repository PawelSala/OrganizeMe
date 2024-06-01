import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk #dodawanie zdjec
import tools
import time
import random

root = tk.Tk()
root.resizable(False, False) #brak mozliwosci zmiany okienka

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#OKNO LOGOWANIA
def login_window(window, on_login_click, on_go_register_click):
    for content in window.winfo_children():
        content.destroy()
    
    #okienko wyskakuje na srodku ekranu
    window_width = int(screen_width * 0.237) #szerokosc okna i wysokosc dopasowana do ekranu uzytkownika
    window_height = int(screen_height * 0.29)
    x_window_place = (screen_width / 2) - (window_width /2)
    y_window_place = (screen_height / 2) - (window_height /2)
    root.geometry('%dx%d+%d+%d' % (window_width, window_height, x_window_place, y_window_place))
    
    window.title("Log in")
    window.configure(bg="#F5F5F5")
    window.iconbitmap("graphic_elements/logo_icon.ico")

    label_login = tk.Label(
        window, 
        text = "E-mail", 
        bg="#F5F5F5",
        fg="#023047",
        font = ("Arial Rounded MT Bold", 15)
        )
    label_login.place(x=128, y=160)

    label_password = tk.Label(
        window, 
        text = "Password", 
        bg="#F5F5F5",
        fg="#023047",
        font=("Arial Rounded MT Bold", 15)
        )
    label_password.place(x=128, y=232)

    label_register = tk.Label(
        window, 
        text = "First time? Register here", 
        bg="#F5F5F5",
        font=("Arial Rounded MT Bold", 8),
        fg = "#767676"
        )
    label_register.place(x=193, y=349)

    error_label = tk.Label(
        window,
        text="",
        bg="#F5F5F5",
        fg="#FF0000",
        font=("Arial Rounded MT Bold", 8),
        )
    error_label.place(x=136, y=218)

    #login i haslo, boxy do wpisywania
    entry_font = ("Helvetica", 14)
    entry_login = tk.Entry(window, bg="#E4E4E4", width =30,  font = entry_font, border=0)
    entry_login.place(x=136, y=190)

    entry_password = tk.Entry(window, bg="#E4E4E4", width =30,  font = entry_font, border=0, show="*")
    entry_password.place(x=136, y=262)

    #login i haslo, tlo boxow
    image = Image.open("graphic_elements/login_window/entry_bg.png")
    photo = ImageTk.PhotoImage(image)
    login_label = tk.Label(root,image =photo, bd = 0, bg = "#F5F5F5")
    login_label.image = photo
    login_label.place(x = 129, y=189)
    login_label.lower()

    image = Image.open("graphic_elements/login_window/entry_bg.png")
    photo = ImageTk.PhotoImage(image)
    login_label = tk.Label(root,image =photo, bd = 0, bg = "#F5F5F5")
    login_label.image = photo
    login_label.place(x = 129, y=261)
    login_label.lower()

    #przycisk logowania, tlo
    image = Image.open("graphic_elements/login_window/login_btn.png")
    photo = ImageTk.PhotoImage(image)
    login_label = tk.Label(root,image =photo, bd = 0, bg = "#F5F5F5")
    login_label.image = photo
    login_label.pack()
    login_label.place(x = 268, y=305)
    login_label.lower()
    
    
    #przycisk logowania
    label_login_btn = tk.Button(
        window, 
        text = "Log in",
        bg="#E4E4E4",
        font=("Arial Rounded MT Bold", 8),
        bd = 0,
        highlightthickness=0,
        activebackground="#E4E4E4",
        command=lambda:on_login_click(entry_login.get(), entry_password.get())
        )
    label_login_btn.place(x=280, y=306)

    #ikonka strzalka
    image = Image.open("graphic_elements/login_window/arrow.png")
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(root, image =photo, bd = 0)
    label.image = photo
    label.pack()
    label.place(x = 339, y=343)

    #ikonka rejestracji - button
    image = Image.open("graphic_elements/login_window/register_icon.png")
    photo = ImageTk.PhotoImage(image)
    register_button = tk.Button(window, image =photo, command=on_go_register_click, bd = 0, highlightthickness=0)
    register_button.image = photo
    register_button.pack()
    register_button.place(x = 366, y=338)
    
    #logo
    image = Image.open("graphic_elements/login_window/logo_complete.png")
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=photo, bd=0)
    label.image = photo
    label.pack()
    label.place(x = 237, y=13)




# OKNO REJSETRACJI
def register_window(window, back_to_login_click, on_register_click):
    for content in window.winfo_children():
        content.destroy()

    window.title("Register window")
    window.geometry("599x389")
    window.configure(bg="#F5F5F5")
    window.iconbitmap("graphic_elements/logo_icon.ico")

    # napisy
    label_name = tk.Label(
        window,
        text="Name:",
        bg="#F5F5F5",
        fg="#023047",
        font=("Arial Rounded MT Bold", 15)
    )
    label_name.place(x=128, y=50)

    label_mail = tk.Label(
        window,
        text="Mail:",
        bg="#F5F5F5",
        fg="#023047",
        font=("Arial Rounded MT Bold", 15)
    )
    label_mail.place(x=128, y=120)

    label_password2 = tk.Label(
        window,
        text="Password:",
        bg="#F5F5F5",
        fg="#023047",
        font=("Arial Rounded MT Bold", 15)
    )
    label_password2.place(x=128, y=190)

    label_password3 = tk.Label(
        window,
        text="Confirm Password:",
        bg="#F5F5F5",
        fg="#023047",
        font=("Arial Rounded MT Bold", 15)
    )
    label_password3.place(x=128, y=260)

    error_label = tk.Label(
        window,
        text="",
        fg="#FF0000",
        bg="#F5F5F5",
        font=("Arial Rounded MT Bold", 6)
    )
    error_label.place(x=136, y=178)


    # imie, mail i haslo, boxy do wpisywania
    register_font = ("Helvetica", 14)
    register_name = tk.Entry(window, bg="#E4E4E4", width =30,  font = register_font, border=0)
    register_name.place(x=136, y=80)

    register_mail = tk.Entry(window, bg="#E4E4E4", width =30,  font = register_font, border=0)
    register_mail.place(x=136, y=150)

    register_password = tk.Entry(window, bg="#E4E4E4", width =30,  font = register_font, border=0)
    register_password.place(x=136, y=220)

    register_password2 = tk.Entry(window, bg="#E4E4E4", width =30,  font = register_font, border=0)
    register_password2.place(x=136, y=290)


    # imie, mail i haslo, tlo do boxow
    def create_bg(x, y):
        image = Image.open("graphic_elements/login_window/entry_bg.png")
        photo = ImageTk.PhotoImage(image)
        entry_label = tk.Label(root, image=photo, bd=0, bg="#F5F5F5")
        entry_label.image = photo
        entry_label.place(x=x, y=y)
        entry_label.lower()

    create_bg(129, 79)
    create_bg(129, 149)
    create_bg(129, 219)
    create_bg(129, 289)

    # przycisk rejestracji i BACK, tlo
    def create_button_bg(image_path, x, y):
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        button_label = tk.Label(root, image=photo, bd=0, bg="#F5F5F5")
        button_label.image = photo
        button_label.place(x=x, y=y)
        button_label.lower()
    
    create_button_bg("graphic_elements/login_window/login_btn.png", 293, 337)
    create_button_bg("graphic_elements/login_window/login_btn.png", 228, 337)

    # przycisk rejestracji
    label_register_btn = tk.Button(
        window,
        text = "Register",
        bg="#E4E4E4",
        font=("Arial Rounded MT Bold", 8),
        bd = 0,
        highlightthickness=0,
        activebackground="#E4E4E4",
        command = lambda:on_register_click(register_mail.get(),register_password.get(),register_name.get(),register_password2.get())
        )
    label_register_btn.place(x=303, y=337)

     # przycisk BACK
    label_back_btn = tk.Button(
        window,
        text = "Back",
        bg="#E4E4E4",
        font=("Arial Rounded MT Bold", 8),
        bd = 0,
        highlightthickness=0,
        activebackground="#E4E4E4",
        command=back_to_login_click
        )
    label_back_btn.place(x=246, y=337)



#OKNO GLOWNE
def home_window(window, add_note_click, remove_note_click, name, logout):
# def home_window(window):
    for content in window.winfo_children():
        content.destroy()

    #okienko wyskakuje na srodku ekranu
    window_width = int(screen_width * 0.65) #szerokosc okna i wysokosc dopasowana do ekranu uzytkownika
    window_height = int(screen_height * 0.7)
    x_window_place = (screen_width / 2) - (window_width /2)
    y_window_place = (screen_height / 2) - (window_height /2)
    root.geometry('%dx%d+%d+%d' % (window_width, window_height, x_window_place, y_window_place))
    
    window.title("Homepage")
    window.configure(bg="#F0F0F0")
    window.iconbitmap("graphic_elements/logo_icon.ico")


    #Ramka dla menu bocznego
    frame_menu = tk.Frame(window)
    frame_menu.grid(row=0, column=0, sticky="nw")

    #Ramka dla kalendarza
    frame_calendar = tk.Frame(window)
    frame_calendar.grid(row=0, column=0, sticky="nsew")

    #ramka dla miesiąca
    frame_month = tk.Frame(window)
    frame_month.grid(row=0, column=0, sticky="nsew")

    global view_number #widok kalendarza:  0 - rok,  1,2,3.. - dany miesiac
    view_number = 0

    new_size = (1229,929) 
    
    def menu_open_clicked():
        print("Menu clicked!")
        frame_menu.lift()

    def menu_close_clicked():
        frame_menu.lower()

    def change_view(number):
        global view_number
        view_numbers = {0: 12,1: 1,2: 2,3: 3,4: 4,5: 5,6: 6,7: 7,8: 8,9: 9,10: 10,11: 11,12: 12, 13: 1}
        view(view_numbers.get(number, 1))
        if number == 0:
            view_number = 12
        elif number == 13:
            view_number = 1
        else:
            view_number = number
    
    def change_view_btn(number):
        global view_number
        if number == 0:
            view_number = 1
        else:
            view_number = 0
        view(view_number)


    #######MENU BOCZNE#######
    quotes = ["“I never dreamed about success. I worked for it.” —Estée Lauder",
                "“Goal setting is the secret to a compelling future.” —Tony Robbins",
                "“Setting goals is the first step in turning the invisible into the visible.” —Tony Robbins",
                "“If you can dream it, you can do it.” ―Walt Disney",
                "“Opportunities don’t happen, you create them.” —Chris Grosser"]

    #logo
    image = Image.open("graphic_elements/homepage/menu_bg.png")
    photo = ImageTk.PhotoImage(image)
    menu_bg_label = tk.Label(frame_menu, image=photo, bd=0)
    menu_bg_label.image = photo
    menu_bg_label.place(x=0, y=0)

    #menu close- button
    image = Image.open("graphic_elements/homepage/menu_close_btn.png")
    photo = ImageTk.PhotoImage(image)
    menu_close_button = tk.Button(frame_menu, image=photo, bd=0, activebackground="#E2E2E2", highlightthickness=0, command=menu_close_clicked)
    menu_close_button.image = photo
    menu_close_button.grid(row=0, column=0, sticky="nw", padx=window_width*0.003, pady=window_height*0.006)
    
    #random quote
    quote_label = tk.Label(frame_menu,text= random.choice(quotes),bg="#E2E2E2",fg="#023047",font=("Arial Rounded MT Bold", 11), wraplength=250, justify='center')
    quote_label.grid(row=1, column=0, pady=(window_height*0.15,0))

    #Change view button
    view_button = tk.Button(frame_menu, width=20, text = "Change view", bg="#D1D1D1", bd=0, activebackground="#D1D1D1", highlightthickness=0 ,font = ("Arial Rounded MT Bold", 16), command=lambda:change_view_btn(view_number))
    view_button.grid(row=2,column=0, padx=window_width*0.04, pady=(window_height*0.099, 0))

    #Notes button
    notes_button = tk.Button(frame_menu, width=20, text = "Notes", bg="#D1D1D1", bd=0, activebackground="#D1D1D1", highlightthickness=0 ,font = ("Arial Rounded MT Bold", 16), command=open_notes_window)
    notes_button.grid(row=3,column=0, pady=(window_height*0.054, 0))
    
    #Log out button
    logout_button = tk.Button(frame_menu, width=20, text = "Log out", bg="#D1D1D1", fg="#DA4242", activeforeground="#DA4242", bd=0, activebackground="#D1D1D1", highlightthickness=0 ,font = ("Arial Rounded MT Bold", 16), command=logout)
    logout_button.grid(row=4,column=0, pady=window_height*0.42)




    #####WIDOK GLOWNY####

    def view(number):
        def show_date_label():
                today = time.strftime("%A, %d %B, %Y")
                date_label = tk.Label(frame_calendar, text=today, bg="#F0F0F0", font=20)
                date_label.grid(row=0, column=2, padx=(90,0), pady=30, columnspan=2)

        if number == 0:
            frame_calendar.lift()
            #NAPISY
            ####### welcome_label.config(text="")
                
            #welcome text and date
            welcome_label = tk.Label(frame_calendar, text=f"Welcome back {name}!", font=20, bg="#F0F0F0")
            welcome_label.grid(row=0, column=2, padx=(90,0), pady=30, columnspan=2)

            window.after(5000, lambda: welcome_label.config(text=""))
            window.after(5000, show_date_label)

            #menu- button
            image_menu = Image.open("graphic_elements/homepage/menu_open_btn.png")
            photo_menu = ImageTk.PhotoImage(image_menu)
            menu_open_button = tk.Button(frame_calendar, image =photo_menu, bd = 0, highlightthickness=0, command=menu_open_clicked)
            menu_open_button.image = photo_menu
            menu_open_button.grid(row=0, column=0, padx=15, pady=10)

            #add note
            image = Image.open("graphic_elements/homepage/add_btn.png")
            photo = ImageTk.PhotoImage(image)
            add_button = tk.Button(frame_calendar, image=photo, bd = 0, highlightthickness=0, command=add_note_click)
            add_button.image = photo
            add_button.grid(row=4, column=6, padx=0, pady=0)
            add_button.lift()

            #remove note
            image = Image.open("graphic_elements/homepage/remove_btn.png")
            photo = ImageTk.PhotoImage(image)
            remove_button = tk.Button(frame_calendar, image=photo, bd = 0, highlightthickness=0, command=remove_note_click)
            remove_button.image = photo
            remove_button.grid(row=4, column=5, padx=30, pady=0)
            remove_button.lift()

            #Miesiace
            #01
            image = Image.open("graphic_elements/homepage/months/january.png")
            photo = ImageTk.PhotoImage(image)
            january = tk.Button(frame_calendar, image = photo, bd = 0, command=lambda:change_view(1))
            january.image = photo
            january.grid(row=1, column=1, padx=(155,0), pady=35)
            
            #02
            image = Image.open("graphic_elements/homepage/months/february.png")
            photo = ImageTk.PhotoImage(image)
            february = tk.Button(frame_calendar, image = photo, bd = 0, command=lambda:change_view(2))
            february.image = photo
            february.grid(row=1, column=2, padx=(70,0), pady=0)

            #03
            image = Image.open("graphic_elements/homepage/months/march.png")
            photo = ImageTk.PhotoImage(image)
            march = tk.Button(frame_calendar, image = photo, bd = 0, command=lambda:change_view(3))
            march.image = photo
            march.grid(row=1, column=3, padx=(70,0), pady=0)

            #04
            image = Image.open("graphic_elements/homepage/months/april.png")
            photo = ImageTk.PhotoImage(image)
            april = tk.Button(frame_calendar, image = photo, bd = 0, command=lambda:change_view(4))
            april.image = photo
            april.grid(row=1, column=4, padx=(70,0), pady=0)

            #05
            image = Image.open("graphic_elements/homepage/months/may.png")
            photo = ImageTk.PhotoImage(image)
            may = tk.Button(frame_calendar, image = photo, bd = 0, command=lambda:change_view(5))
            may.image = photo
            may.grid(row=2, column=1, padx=(140,0), pady=0)

            #06
            image = Image.open("graphic_elements/homepage/months/june.png")
            photo = ImageTk.PhotoImage(image)
            june = tk.Button(frame_calendar, image = photo, bd = 0, command=lambda:change_view(6))
            june.image = photo
            june.grid(row=2, column=2, padx=(70,0), pady=0)

            #07
            image = Image.open("graphic_elements/homepage/months/july.png")
            photo = ImageTk.PhotoImage(image)
            july = tk.Button(frame_calendar, image = photo, bd = 0, command=lambda:change_view(7))
            july.image = photo
            july.grid(row=2, column=3, padx=(70,0), pady=0)

            #08
            image = Image.open("graphic_elements/homepage/months/august.png")
            photo = ImageTk.PhotoImage(image)
            august = tk.Button(frame_calendar, image = photo, bd = 0, command=lambda:change_view(8))
            august.image = photo
            august.grid(row=2, column=4, padx=(70,0), pady=0)

            #09
            image = Image.open("graphic_elements/homepage/months/september.png")
            photo = ImageTk.PhotoImage(image)
            september = tk.Button(frame_calendar, image = photo, bd = 0, command=lambda:change_view(9))
            september.image = photo
            september.grid(row=3, column=1, padx=(140,0), pady=40)

            #10
            image = Image.open("graphic_elements/homepage/months/october.png")
            photo = ImageTk.PhotoImage(image)
            october = tk.Button(frame_calendar, image = photo, bd = 0, command=lambda:change_view(10))
            october.image = photo
            october.grid(row=3, column=2, padx=(70,0),pady=0)

            #11
            image = Image.open("graphic_elements/homepage/months/november.png")
            photo = ImageTk.PhotoImage(image)
            november = tk.Button(frame_calendar, image = photo, bd = 0, command=lambda:change_view(11))
            november.image = photo
            november.grid(row=3, column=3, padx=(70,0), pady=0)

            #12
            image = Image.open("graphic_elements/homepage/months/december.png")
            photo = ImageTk.PhotoImage(image)
            december = tk.Button(frame_calendar, image = photo, bd = 0, command=lambda:change_view(12))
            december.image = photo
            december.grid(row=3, column=4, padx=(70,0), pady=0)

        else:
            frame_month.lift()
            
            #menu- button
            image_menu = Image.open("graphic_elements/homepage/menu_open_btn.png")
            photo_menu = ImageTk.PhotoImage(image_menu)
            menu_open_button = tk.Button(frame_month, image =photo_menu, bd = 0, highlightthickness=0, command=menu_open_clicked)
            menu_open_button.image = photo_menu
            menu_open_button.grid(row=0, column=0, padx=(15,0), pady=(16,0), sticky="nsew")

            #arrow back- button
            image = Image.open("graphic_elements/homepage/arrow_back.png")
            photo = ImageTk.PhotoImage(image)
            arrow_back_button = tk.Button(frame_month, image =photo, bd = 0, highlightthickness=0, command=lambda:change_view(view_number-1))
            arrow_back_button.image = photo
            arrow_back_button.grid(row=1, column=1, padx=(20,0), pady=(450,0), sticky="nsew")

            #arrow forward- button
            image = Image.open("graphic_elements/homepage/arrow_forward.png")
            photo = ImageTk.PhotoImage(image)
            arrow_forward_button = tk.Button(frame_month, image =photo, bd = 0, highlightthickness=0, command=lambda:change_view(view_number+1))
            arrow_forward_button.image = photo
            arrow_forward_button.grid(row=1, column=2, padx=(1317,0), pady=(450,0), sticky="nsew")

            #add note
            image = Image.open("graphic_elements/homepage/add_btn.png")
            photo = ImageTk.PhotoImage(image)
            add_button = tk.Button(frame_month, image=photo, bd = 0, highlightthickness=0, command=add_note_click)
            add_button.image = photo
            add_button.grid(row=2, column=3, padx=0, pady=326)

            if number == 1:
                image = Image.open("graphic_elements/homepage/months_2/january.png")
                resized_image = image.resize(new_size)
                photo = ImageTk.PhotoImage(resized_image)
                january_m = tk.Label(window, image = photo)
                january_m.image = photo
                january_m.place(relx=0.109, rely=0.0405)

            elif number == 2:
                image = Image.open("graphic_elements/homepage/months_2/february.png")
                resized_image = image.resize(new_size)
                photo = ImageTk.PhotoImage(resized_image)
                february_m = tk.Label(window, image = photo)
                february_m.image = photo
                february_m.place(relx=0.109, rely=0.04)
            
            elif number == 3:
                image = Image.open("graphic_elements/homepage/months_2/march.png")
                resized_image = image.resize(new_size)
                photo = ImageTk.PhotoImage(resized_image)
                march_m = tk.Label(window, image = photo)
                march_m.image = photo
                march_m.place(relx=0.109, rely=0.04)

            elif number == 4:
                image = Image.open("graphic_elements/homepage/months_2/april.png")
                resized_image = image.resize(new_size)
                photo = ImageTk.PhotoImage(resized_image)
                april_m = tk.Label(window, image = photo)
                april_m.image = photo
                april_m.place(relx=0.109, rely=0.04)

            elif number == 5:
                image = Image.open("graphic_elements/homepage/months_2/may.png")
                resized_image = image.resize(new_size)
                photo = ImageTk.PhotoImage(resized_image)
                may_m = tk.Label(window, image = photo)
                may_m.image = photo
                may_m.place(relx=0.108, rely=0.04)

            elif number == 6:
                image = Image.open("graphic_elements/homepage/months_2/june.png")
                resized_image = image.resize(new_size)
                photo = ImageTk.PhotoImage(resized_image)
                june_m = tk.Label(window, image = photo)
                june_m.image = photo
                june_m.place(relx=0.109, rely=0.04)

            elif number == 7:
                image = Image.open("graphic_elements/homepage/months_2/july.png")
                resized_image = image.resize(new_size)
                photo = ImageTk.PhotoImage(resized_image)
                july_m = tk.Label(window, image = photo)
                july_m.image = photo
                july_m.place(relx=0.109, rely=0.04)

            elif number == 8:
                image = Image.open("graphic_elements/homepage/months_2/august.png")
                resized_image = image.resize(new_size)
                photo = ImageTk.PhotoImage(resized_image)
                august_m = tk.Label(window, image = photo)
                august_m.image = photo
                august_m.place(relx=0.109, rely=0.04)

            elif number == 9:
                image = Image.open("graphic_elements/homepage/months_2/september.png")
                resized_image = image.resize(new_size)
                photo = ImageTk.PhotoImage(resized_image)
                september_m = tk.Label(window, image = photo)
                september_m.image = photo
                september_m.place(relx=0.109, rely=0.04)

            elif number == 10:
                image = Image.open("graphic_elements/homepage/months_2/october.png")
                resized_image = image.resize(new_size)
                photo = ImageTk.PhotoImage(resized_image)
                october_m = tk.Label(window, image = photo)
                october_m.image = photo
                october_m.place(relx=0.109, rely=0.04)

            elif number == 11:
                image = Image.open("graphic_elements/homepage/months_2/november.png")
                resized_image = image.resize(new_size)
                photo = ImageTk.PhotoImage(resized_image)
                november_m = tk.Label(window, image = photo)
                november_m.image = photo
                november_m.place(relx=0.109, rely=0.04)

            else:
                image = Image.open("graphic_elements/homepage/months_2/december.png")
                resized_image = image.resize(new_size)
                photo = ImageTk.PhotoImage(resized_image)
                december_m = tk.Label(window, image = photo)
                december_m.image = photo
                december_m.place(relx=0.109, rely=0.04)

    view(view_number)


# #################################################################

    # remove_note_btn = tk.Button(
    #     window, 
    #     text = "Remove note",
    #     bg="#E4E4E4",
    #     font=("Arial Rounded MT Bold", 15),
    #     bd = 0,
    #     highlightthickness=0,
    #     activebackground="#E4E4E4",
    #     command=remove_note_click
    #     )
    # remove_note_btn.place(x=480, y=308)


#######################################################################
# # funkcja dodawania notatki
# def add_note_click(parent_window):
    
#     add_note_click = tk.Toplevel(parent_window)
#     add_note_click.title("Add Note")
#     add_note_click.configure(bg="#F5F5F5")
#     add_note_click.iconbitmap("graphic_elements/logo_icon.ico")
#     add_note_click.geometry("400x300")
        
#     # napisy
#     label_title = tk.Label(
#         add_note_click,
#         text="Enter the title of the note:",
#         bg="#F5F5F5",
#         fg="#023047",
#         font=("Arial Rounded MT Bold", 10)
#     )
#     label_title.place(x=20, y=20)

#     label_content = tk.Label(
#         add_note_click,
#         text="Enter the content of the note:",
#         bg="#F5F5F5",
#         fg="#023047",
#         font=("Arial Rounded MT Bold", 10),
#     )
#     label_content.place(x=20, y=70)

#     # boxy do wpisywania
#     note_font = ("Helvetica", 8)
#     note_title = tk.Entry(add_note_click, bg="#E4E4E4", width =60,  font = note_font, border=0)
#     note_title.place(x=20, y=43)

#     note_content = tk.Text(add_note_click, bg="#E4E4E4", width =60, height=10, font = note_font, border=0)
#     note_content.place(x=20, y=93)

#     # przycisk zapisu notatki
#     save_button = tk.Button(
#         add_note_click, 
#         text="Save", 
#         bg="#E4E4E4",
#         font=("Arial Rounded MT Bold", 8),
#         bd = 0,
#         highlightthickness=0,
#         activebackground="#E4E4E4",
#         command=lambda: save_note(add_note_click, note_title.get(), note_content.get("1.0", "end-1c")),
#         )
#     save_button.place(x=180, y=260)

# def save_note(window, title, content):
#     try:
#         tools.add_note_to_firebase(title, content)
#     except Exception as e:
#         print("Wystąpił błąd podczas zapisywania notatki:", str(e))

#     window.destroy()

#root.mainloop()


# Function to display notes
def display_notes(parent_window):
    notes = tools.get_notes_from_firebase()
    for widget in parent_window.winfo_children():
        widget.destroy()

    if notes:
        for note in notes:
            note_frame = tk.Frame(parent_window, bg="#E4E4E4", bd=1, relief="solid")
            note_frame.pack(pady=5, padx=10, fill="x", expand=True)

            title_label = tk.Label(note_frame, text=note['title'], bg="#E4E4E4", fg="#023047", font=("Arial Rounded MT Bold", 12), anchor="w")
            title_label.pack(anchor="w", padx=10, pady=5)

            content_label = tk.Label(note_frame, text=note['content'], bg="#E4E4E4", fg="#023047", font=("Helvetica", 10), wraplength=350, justify="left", anchor="w")
            content_label.pack(anchor="w", padx=10, pady=5)
    else:
        no_notes_label = tk.Label(parent_window, text="No notes available", bg="#F5F5F5", fg="#023047", font=("Arial Rounded MT Bold", 12))
        no_notes_label.pack(pady=20)


# Function to handle adding a new note
def add_note_click(parent_window):
    add_note_click = tk.Toplevel(parent_window)
    add_note_click.title("Add Note")
    add_note_click.configure(bg="#F5F5F5")
    add_note_click.iconbitmap("graphic_elements/logo_icon.ico")
    add_note_click.geometry("400x300")

    # Labels
    label_title = tk.Label(
        add_note_click,
        text="Enter the title of the note:",
        bg="#F5F5F5",
        fg="#023047",
        font=("Arial Rounded MT Bold", 10)
    )
    label_title.place(x=20, y=20)

    label_content = tk.Label(
        add_note_click,
        text="Enter the content of the note:",
        bg="#F5F5F5",
        fg="#023047",
        font=("Arial Rounded MT Bold", 10),
    )
    label_content.place(x=20, y=70)

    # Entry boxes
    note_font = ("Helvetica", 8)
    note_title = tk.Entry(add_note_click, bg="#E4E4E4", width=60, font=note_font, border=0)
    note_title.place(x=20, y=43)

    note_content = tk.Text(add_note_click, bg="#E4E4E4", width=60, height=10, font=note_font, border=0)
    note_content.place(x=20, y=93)

    # Save button
    save_button = tk.Button(
        add_note_click,
        text="Save",
        bg="#E4E4E4",
        font=("Arial Rounded MT Bold", 8),
        bd=0,
        highlightthickness=0,
        activebackground="#E4E4E4",
        command=lambda: save_note(add_note_click, note_title.get(), note_content.get("1.0", "end-1c")),
    )
    save_button.place(x=180, y=260)
    

# Function to save a note
def save_note(window, title, content):
    try:
        tools.add_note_to_firebase(title, content)
        window.destroy()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving the note: {str(e)}")

# Function to open the notes window
def open_notes_window():
    notes_window = tk.Toplevel()
    notes_window.title("Notes")
    notes_window.configure(bg="#F5F5F5")
    notes_window.geometry("500x600")

    # Create a frame for the canvas and scrollbar
    frame_canvas = tk.Frame(notes_window, bg="#F5F5F5")
    frame_canvas.pack(fill="both", expand=True)

    # Add a canvas in that frame
    canvas = tk.Canvas(frame_canvas, bg="#F5F5F5")
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar to the canvas
    scrollbar = ttk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create another frame inside the canvas
    notes_frame = tk.Frame(canvas, bg="#F5F5F5")

    # Add that new frame to a window in the canvas
    canvas.create_window((0, 0), window=notes_frame, anchor="nw")

    display_notes(notes_frame)


def display_remove_notes(parent_window):
    notes = tools.get_notes_from_firebase()
    for widget in parent_window.winfo_children():
        widget.destroy()

    if notes:
        for note in notes:
            note_frame = tk.Frame(parent_window, bg="#E4E4E4", bd=1, relief="solid")
            note_frame.pack(pady=5, padx=10, fill="x", expand=True)

            # Dodajemy bind dla zdarzenia kliknięcia na note_frame
            note_frame.bind("<Button-1>", lambda e, note_id=note['id']: tools.delete_note_from_firebase(note_id))

            title_label = tk.Label(note_frame, text=note['title'], bg="#E4E4E4", fg="#023047", font=("Arial Rounded MT Bold", 12), anchor="w")
            title_label.pack(anchor="w", padx=10, pady=5)

            content_label = tk.Label(note_frame, text=note['content'], bg="#E4E4E4", fg="#023047", font=("Helvetica", 10), wraplength=350, justify="left", anchor="w")
            content_label.pack(anchor="w", padx=10, pady=5)

            # Opcjonalnie, możesz dodać bind dla zdarzenia kliknięcia na etykiety (title_label, content_label)
            title_label.bind("<Button-1>", lambda e, note_id=note['id']: tools.delete_note_from_firebase(note_id))
            content_label.bind("<Button-1>", lambda e, note_id=note['id']: tools.delete_note_from_firebase(note_id))
    else:
        no_notes_label = tk.Label(parent_window, text="No notes available", bg="#F5F5F5", fg="#023047", font=("Arial Rounded MT Bold", 12))
        no_notes_label.pack(pady=20)

def open_remove_notes_window():
    notes_window = tk.Toplevel()
    notes_window.title("Notes")
    notes_window.configure(bg="#F5F5F5")
    notes_window.geometry("500x600")

    # Create a frame for the canvas and scrollbar
    frame_canvas = tk.Frame(notes_window, bg="#F5F5F5")
    frame_canvas.pack(fill="both", expand=True)

    # Add a canvas in that frame
    canvas = tk.Canvas(frame_canvas, bg="#F5F5F5")
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar to the canvas
    scrollbar = ttk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create another frame inside the canvas
    notes_frame = tk.Frame(canvas, bg="#F5F5F5")

    # Add that new frame to a window in the canvas
    canvas.create_window((0, 0), window=notes_frame, anchor="nw")

    display_remove_notes(notes_frame)