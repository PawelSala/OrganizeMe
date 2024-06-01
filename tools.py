import pyrebase
from dotenv import dotenv_values

env_vars = dotenv_values('.env')

firebase_config = {
    "apiKey": env_vars["apiKey"],
    "authDomain": env_vars["authDomain"],
    "databaseURL": env_vars["databaseURL"],
    "projectId": env_vars["projectId"],
    "storageBucket": env_vars["storageBucket"],
    "messagingSenderId": env_vars["messagingSenderId"],
    "appId": env_vars["appId"]
}

# Inicjacja firebase
def firebase_init():
    global auth, firebase
    try:
        firebase = pyrebase.initialize_app(firebase_config)
        auth = firebase.auth()
        return True
    except Exception as e:
        print(e)
        return False


# Funkcja do logowania
def login(email, password):
    global user_id
    # logowanie działa jak powinno, return true żeby można było dalej pracować
    #return True
    if validate_email(email):
        
        try:
            #auth.get_user_by_email(email)
            user = auth.sign_in_with_email_and_password(email, password)
            user_id = user['localId']
            return True
        except Exception as e:
            print("zły login lub hasło")
            return False
    return False


# Funkcja do rejestracji
def register(email, password, name):
    try:
        if validate_email(email):
            auth.create_user_with_email_and_password(email=email, password=password)
            add_name_to_firebase(name, email)
            return True
    except Exception as e:
        print(e)
        return False
    
def add_name_to_firebase(name, email):
    try:
        db = firebase.database()
        db.child(email[:email.find(".")]).push({"Imię": name})
        print("Notatka została zapisana w firebase.")
        return True
    except Exception as e:
        print("Wystąpił błąd podczas dodawania notatki:", str(e))
        return False


def get_name_from_firebase(email):
    try:
        db = firebase.database()
        snapshot = db.child(email[:email.find(".")]).get()
        for child in snapshot.each():
            name = child.val().get("Imię")
            return name
    except Exception as e:
        print("Wystąpił błąd podczas pobierania imienia:", str(e))
        return None


# Funkcja pobierająca ID użytkownika z firebase
# def get_user_ID(email):
#     try:
#         user = auth.get_user_by_email(email)
#         return user.uid
#     except Exception as e:
#         print(e)
#         return None


def validate_email(email):
    if "@" in email:
        username, domain = email.split("@")
        if "." in domain:
            return True
    print("Zły email")
    return False

# funckja dodawania notatki do firebase
# def add_note_to_firebase(title, content):
#     try:
#         db = firebase.database()
#         db.child("notes").push({"title": title, "content": content})
#         print("Notatka została zapisana w firebase.")
#         return True
#     except Exception as e:
#         print("Wystąpił błąd podczas dodawania notatki:", str(e))
#         return False

def add_note_to_firebase(title, content):
    try:
        db = firebase.database()
        db.child(user_id).push({"title": title, "content": content})
        print("Notatka została zapisana w firebase.")
        return True
    except Exception as e:
        print("Wystąpił błąd podczas dodawania notatki:", str(e))
        return False
	
def get_notes_from_firebase():
    try:
        db = firebase.database()
        notes = db.child(user_id).get()  # Pobranie wszystkich notatek dla użytkownika
        if notes.each():  # Sprawdzenie, czy są jakiekolwiek notatki
            # Inicjalizacja pustej listy na notatki
            all_notes = []
            # Iteracja przez każdą notatkę
            for note in notes.each():
                # Pobranie ID notatki
                note_id = note.key()
                # Pobranie zawartości notatki
                note_data = note.val()
                # Dodanie ID do zawartości notatki
                note_data["id"] = note_id
                # Dodanie notatki do listy wszystkich notatek
                all_notes.append(note_data)
            return all_notes
        else:
            print("Brak notatek w Firebase dla użytkownika", user_id)
            return []
    except Exception as e:
        print("Wystąpił błąd podczas pobierania notatek:", str(e))
        return []
    
def delete_note_from_firebase(note_id):
    try:
        db = firebase.database()
        # Usunięcie notatki na podstawie jej ID
        db.child(user_id).child(note_id).remove()
        print("Notatka została usunięta z Firebase.")
        return True
    except Exception as e:
        print("Wystąpił błąd podczas usuwania notatki z Firebase:", str(e))
        return False