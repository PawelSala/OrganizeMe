import GUI_base
import graphics
import tools

def logout():
    print("Logout button clicked")
    graphics.login_window(main_window.master,on_login_click, on_go_register_click)

#dzialanie guzikow-zmiana okien, po wcisnieciu guzika.
def on_go_register_click():
    print("Register button clicked!")
    graphics.register_window(main_window.master, back_to_login_click, on_register_click)

def on_register_click(email, password, name, confirm_password):
    print("Registration button clicked!")
    if tools.validate_email(email) and password==confirm_password:
        if tools.register(email,password,name):
            graphics.login_window(main_window.master,on_login_click, on_go_register_click)

def on_login_click(email,password):
    print("Login button clicked!")
    if tools.login(email,password):
        graphics.home_window(main_window.master, add_note_click, remove_note_click, tools.get_name_from_firebase(email), logout)

def back_to_login_click():
    print("Back to login!")
    graphics.login_window(main_window.master, on_login_click, on_go_register_click)


#dzialanie guzikow
def add_note_click():
    print("Want to add note button clicked!")
    graphics.add_note_click(main_window.master)

def remove_note_click():
    print("Want to remove note clicked!")
    graphics.open_remove_notes_window()


def main():
    global main_window
    tools.firebase_init()
    main_window = GUI_base.MyWindow()
    graphics.login_window(main_window.master, on_login_click, on_go_register_click)
    main_window.mainloop()


if __name__ == '__main__':
    main()
