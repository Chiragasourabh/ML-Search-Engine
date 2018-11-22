from flask import Flask, request, render_template
import wikipedia as wp
import config
import speech_recognition as sr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html', answer = "Hi there ....")

@app.route('/', methods=['POST'])
def my_form_post():
    '''r=sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        audio=r.listen(source)
    return r.recognize_google(audio)'''
    text = request.form['search']
    #return wp.summary(r.recognize_google(audio),sentences=2)
    return render_template('home.html',answer = wp.summary(text,sentences=2))

@app.route('/home', methods=['POST'])
def home_my_form_post():
    text = request.form['search']
    return render_template('home.html',answer = wp.summary(text, sentences = 2))

@app.route('/home')
def home():
    return render_template('home.html', answer = "Hi there ....")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/howitworks')
def howitworks():
    return render_template('howitworks.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/auth')
def auth():
    return render_template('login.html')


@app.route('/auth', methods=['POST'])
def login_post():
    email = request.form['txtEmail']
    password = request.form['txtPassword']
    return str(config.signin_with_email_and_password(email,password))

@app.route('/register')
def Register():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register_post():
    name = request.form['username']
    email = request.form['txtEmail']
    password = request.form['password1']
    return str(config.register_with_email_and_password(email,password))

@app.route('/forgotpassword')
def ResetPassword():
    return render_template('forgotpassword.html')

@app.route('/forgotpassword', methods=['POST'])
def ResetPassword_post():
    email = request.form['txtEmail']
    return str(config.reset_password_with_email(email))

@app.route('/wiki')
def wikitest():
	return wp.summary("who invented facebook?", sentences=2)

if __name__ == '__main__':
    app.run(debug = True)
