from flask import Flask, render_template
import wikipedia as wp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')
	
@app.route('/home')
def home():
    return render_template('home.html')
	
@app.route('/about')
def about():
    return render_template('about.html')
	
@app.route('/howitworks')
def howitworks():
    return render_template('howitworks.html')
	
@app.route('/contact')
def contact():
    return render_template('404.html')
	
@app.route('/auth')
def auth():
    return render_template('404.html')
	
@app.route('/wiki')
def wikitest():
	return wp.summary("who invented facebook?", sentences=2)

if __name__ == '__main__':
    app.run(debug = True)