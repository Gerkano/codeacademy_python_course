from flask import Flask, render_template
from articles.dictionary import data


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', data=data)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
