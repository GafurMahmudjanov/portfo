from flask import Flask, render_template,request,url_for,redirect
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        data = f'''
        email: {email},
        subject: {subject},
        message: {message}'''

        with open('database.txt', 'a') as file_db:
            file_db.write(data + '\n')
        return redirect('/thankyou.html')
    else:
        return 'something went wrong. try again!'



