from flask import Flask, render_template, request, redirect
from datetime import datetime
import csv

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_csv(data):
    with open('database.csv', 'a', newline='') as database:
        name = data['name']
        email = data['email']
        message = data['message']
        date_created = datetime.now().replace(second=0, microsecond=0)
        csv_writer = csv.writer(database, delimiter=',',  
                                quotechar='"', quoting=csv.QUOTE_MINIMAL
                                )
        csv_writer.writerow([name, email, message, date_created])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong, try again'


if __name__ == "__main__":
    app.run(port=5000)
