from flask import Flask
from flask import render_template
from markupsafe import escape
from flask import request, redirect, url_for
import os


email = ''
password = ''
clas = ''
prof = ''
about = ''
accept = ''
sex = ''

UPLOAD_FOLDER = './static/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/list_prof/<res>')
def list_prof(res):
    return render_template('', res = res)


@app.route('/answer', methods=['POST', 'GET'])
def answer():
    if request.method == 'GET':
        return render_template('forlastnewtest.html')
    elif request.method == 'POST':
        global email
        global password
        global clas
        global prof
        global about
        global accept
        global sex
        email = request.form['email']
        password = request.form['password']
        clas = request.form['class']
        print(clas)
        prof = request.form['prof']
        about = request.form['about']
        accept = request.form['accept']
        sex = request.form['sex']
        return redirect(url_for('auto_answer'))


@app.route('/auto_answer')
def auto_answer():
    return render_template('auto_answer.html', email = email, password = password,
                           clas = clas, prof = prof, about = about,
                           accept = accept, sex = sex)



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
