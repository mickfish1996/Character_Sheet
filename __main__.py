import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate(".\character-sheet-68995-firebase-adminsdk-4b2e4-a00dcf1875.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def get_user_email():
    email = input("Please enter your email: ")
    
    return email

def display(data):
    for key in data:
        print(f"{key}: ", end ="")
    
def display_users(db, email):
    results = db.collection("users").where("email", "==", email).get()
    for result in results:
        id = result.id
        
    result = db.collection("users").document(id).get()
    
    data = result.to_dict()
    
    data = data["Character Name"]
    i = 1
    
    print("Characters")
    for key in data:
        print(f"\t{i}. {key}")
        i += 1
        
    characterName = input("Character Name: ")
    display(data[characterName])
    
    
def main():   
    email = get_user_email()  

    print("1. choose character to display")
    choice = int(input("\tOption: "))  

    if choice == 1:
        display_users(db,email)
        
if __name__ == "__main__":
    main()
    
        
    


