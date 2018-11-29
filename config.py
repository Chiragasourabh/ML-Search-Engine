import pyrebase
config = {
    "apiKey": "AIzaSyAyMHEsX7egWQYHQzNmKtdy8xGkd1cXBXE",
    "authDomain": "rummage-1.firebaseapp.com",
    "databaseURL": "https://rummage-1.firebaseio.com",
    "projectId": "rummage-1",
    "storageBucket": "rummage-1.appspot.com",
    "messagingSenderId": "335274514402"
}

firebase =  pyrebase.initialize_app(config)
auth=firebase.auth()
db = firebase.database()

def register_with_email_and_password(email,password):
    try:
        user=auth.create_user_with_email_and_password(email,password)
        auth.send_email_verification(user['idToken'])
        return auth.get_account_info(user['idToken'])
    except:
        return "Registration failed"

def signin_with_email_and_password(email,password):
    try:
        user=auth.sign_in_with_email_and_password(email,password)
        return auth.get_account_info(user['idToken'])
    except:
        return "Login Failed"

def reset_password_with_email(email):
        auth.send_password_reset_email(email)

def sendMessage(name,phoneNum,email,message):
    data = {
    "name": name ,
    "phone": phoneNum ,
    "email": email ,
    "message": message
    }
    db.child("messages").push(data)
