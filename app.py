from flask import Flask, request, render_template
import wikipedia as wp
#import speech_recognition as sr

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

@app.route('/register')
def Register():
    return render_template('register.html')

@app.route('/auth', methods=['POST'])
def login_post():
    username = request.form['txtEmail']
    password = request.form['txtPassword']
    return username



@app.route('/wiki')
def wikitest():
	return wp.summary("who invented facebook?", sentences=2)

if __name__ == '__main__':
    app.run(debug = True)
