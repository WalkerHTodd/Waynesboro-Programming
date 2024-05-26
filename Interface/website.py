from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    title = 'Messing With Stupid Flask'
    return title

@app.route('/about/')
def about():
    title = 'About Us'
    return title

if __name__ == '__main__':
    app.run(debug=True)