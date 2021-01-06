from flask import Flask, render_template
app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/blog/2020/dogs')
def blog2():
    return 'Hello, dogs!'