from flask import Flask, request, render_template, flash, redirect, url_for, session
import wikipedia as wp
import config
from datetime import datetime
#import thread

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return render_template('home.html', answer = "Hi there ...." , login=config.isLoggedIn())

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['search']
    try:
        ans = wp.summary(text,sentences=2)
        if(config.isLoggedIn()):
            #thread.start_new_thread(config.historify, (text,request.remote_addr))
            config.historify(session['id'],text,request.remote_addr)
            return render_template('home.html',answer=ans , login=True)
        else:
            flash("Login to Save History and to get better search results","info")
            config.historify("Annonymous",text,request.remote_addr)
            return render_template('home.html',answer=ans , login=False)
    except:
        return render_template('home.html',answer = "Oh Ohh ... Sorry. I couldnt get that . will get that in next version", login=config.isLoggedIn())



@app.route('/home', methods=['POST'])
def home_my_form_post():
    text = request.form['search']
    try:
        ans = wp.summary(text,sentences=2)
        if(config.isLoggedIn()):
            config.historify(session['id'],text,request.remote_addr)
            return render_template('home.html',answer=ans , login=True)
        else:
            flash("Login to Save History and to get better search results","info")
            return render_template('home.html',answer=ans , login=False)
    except:
        return render_template('home.html',answer = "Oh Ohh ... Sorry. I couldnt get that . will get that in next version", login=config.isLoggedIn())

@app.route('/home')
def home():
    return render_template('home.html', answer = "Hi there ....", login=config.isLoggedIn())

@app.route('/about')
def about():
    return render_template('about.html', login=config.isLoggedIn())

@app.route('/howitworks')
def howitworks():
    return render_template('howitworks.html', login=config.isLoggedIn())

@app.route('/contact')
def contact():
    return render_template('contact.html', login=config.isLoggedIn())


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
    return render_template('login.html', login=config.isLoggedIn())


@app.route('/auth', methods=['POST'])
def login_post():
    email = request.form['txtEmail']
    password = request.form['txtPassword']
    if(config.signin_with_email_and_password(email,password)):
        return redirect(url_for('profile'))
    else:
        flash("Login Failed ! Please Check Your Credentials","warning")
        return redirect(url_for('auth'))
    #return u


@app.route('/register')
def Register():
    return render_template('register.html', login=config.isLoggedIn())

@app.route('/register', methods=['POST'])
def register_post():
    name = request.form['username']
    phone = request.form['txtMobile']
    email = request.form['txtEmail']
    password = request.form['password1']
    if(config.register_with_email_and_password(name,phone,email,password)):
        flash("Registration Successful. Please Check mailbox to Varify your email and login here ","success")
        return redirect(url_for('auth'))
    else:
        flash("Registration Failed. Account already exist with email id : "+email+"","danger")
        return redirect(url_for('Register'))


@app.route('/forgotpassword')
def ResetPassword():
    return render_template('forgotpassword.html', login=config.isLoggedIn())

@app.route('/forgotpassword', methods=['POST'])
def ResetPassword_post():
    email = request.form['txtEmail']
    if(config.reset_password_with_email(email)):
        flash("Password Reset Link has been sent to "+email+".","success")
        return redirect(url_for('auth'))
    else:
        flash("Account Not Found. Please Check Email Address "+email+".","danger")
        return redirect(url_for('ResetPassword'))

@app.route('/wiki')
def wikitest():
	return wp.summary("who invented facebook?", sentences=2)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', login=config.isLoggedIn())


@app.route('/dashboard')
def dashboard():
    if config.isLoggedIn():
        return redirect(url_for('profile'))
    else:
        return redirect(url_for('auth'))


@app.route('/dashboard/profile')
def profile():
    if config.isLoggedIn():
        return render_template('dashboard/profile.html', login=config.isLoggedIn(),id =session['id'],email =session['username'],name = session['name'],phone = session['phone'],score="#",tag="Beginner" )
    else:
        return redirect(url_for('auth'))

@app.route('/dashboard/profile/changepassword')
def changepassword():
    if config.isLoggedIn():
        email = session['username']
        if(config.reset_password_with_email(email)):
            flash("Password Reset Link has been sent to "+email+".","success")
            return redirect(url_for('profile'))
        else:
            flash("Account Not Found. Please Check Email Address "+email+".","danger")
            return redirect(url_for('profile'))
    else:
        return redirect(url_for('auth'))

@app.route('/dashboard/history')
def history():
    if config.isLoggedIn():
        jsonobj=config.history().val()
        return render_template('dashboard/history.html', login=True,json=jsonobj)
    else:
        return redirect(url_for('auth'))

@app.route('/dashboard/future')
def future():
    if config.isLoggedIn():
        return render_template('dashboard/future.html', login=True)
    else:
        return redirect(url_for('auth'))


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    session.pop('id', None)
    session.pop('name', None)
    session.pop('phone', None)
    flash("Logged Out Successfully","info")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug = True)
