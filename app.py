from flask import Flask, request, render_template, flash, redirect, url_for, session
import wikipedia as wp
import config

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return render_template('home.html', answer = "Hi there ....")

@app.route('/', methods=['POST'])
def my_form_post():
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


@app.route('/contact', methods=['POST'])
def contact_form_post():
    name = request.form['name']
    mobile = request.form['phonenumber']
    email = request.form['email']
    messageData = request.form['messages']
    try:
        config.sendMessage(name,mobile,email,messageData)
        flash("Hey "+ name +"! Your Message Has Been Sent Successfully .","success")
    except:
        flash("Hey "+ name +"! Sorry ... Some Internal Problem","danger")
    return redirect(url_for('contact'))

@app.route('/auth')
def auth():
    return render_template('login.html')


@app.route('/auth', methods=['POST'])
def login_post():
    email = request.form['txtEmail']
    password = request.form['txtPassword']
    #try:
    #    u=config.signin_with_email_and_password(email,password)
    #except:
    session['username'] = email
    flash(session['username'],"danger")
    return redirect(url_for('auth'))
    #return u


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

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug = True)
