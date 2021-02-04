from flask import Flask, render_template, request, redirect
from flask_mail import Message, Mail
# from config import mail_username, mail_password
import os

app = Flask(__name__)

app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME'),
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD'),
)

mail = Mail(app)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            email = request.form.get('email')
            message = request.form.get('message')

            msg = Message(
                subject=f"Mail from {name}", 
                body=f"Name: {name}\nEmail: {email}\n\n{message}",
                sender=mail_username,
                recipients=['k.shupa@girlincode.com'],
            )
            mail.send(msg)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong, try again'


if __name__ == "__main__":
    app.run(threaded=True, port=5000)
