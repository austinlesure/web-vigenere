from flask import Flask, request, redirect
from vigenere import encrypt
import caesar
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/vigenere', methods=['POST'])
def vigenere_page():
    template = jinja_env.get_template('v_form.html')
    keyword = request.form['keyword']
    for char in keyword:
        if char.isalpha() == False:
            error_msg = 'Error: Keyword must only contain latin letters.'
            return redirect('/vigenere?error={0}'.format(error_msg))
    message = request.form['message']
    secret_message = encrypt(message, keyword)
    return template.render(keyword = keyword, message = secret_message, title = 'Web Vigenere')

@app.route('/vigenere')
def v_index():
    template = jinja_env.get_template('v_form.html')
    error = request.args.get("error")
    if error:
        return template.render(error_msg = error, title = 'Web Vigenere')
    else:
        return template.render(title = 'Web Vigenere')

@app.route('/caesar', methods=['POST'])
def ceasar_page():
    template = jinja_env.get_template('c_form.html')
    rot = int(request.form['rotate'])
    message = request.form['message']
    secret_message = caesar.encrypt(message, rot)
    return template.render(rotate = rot, message = secret_message, title = 'Web Caesar')

@app.route('/caesar')
def c_index():
    template = jinja_env.get_template('c_form.html')
    error = request.args.get("error")
    if error:
        return template.render(error_msg = error, title = 'Web Caesar')
    else:
        return template.render(title = 'Web Caesar')

@app.route('/')
def index():
    template = jinja_env.get_template('index.html')
    return template.render(title = 'Choose Encryption')

app.run()
