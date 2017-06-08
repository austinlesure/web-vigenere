from flask import Flask, request, redirect
from vigenere import encrypt
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

page_header = '''
    <!doctype html>
    <html>
        <head>
            <title>Web Vigenere</title>
            <style>
            h1 {
                text-align: center;
                font-family: monospace;
            }
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
            .error {
                color: red;
                text-align: center;
            }
        </style>
        </head>
        <body>
            <h1>Web Vigenere</h1>
'''

page_form = '''
            <form method='POST'>
                <label for='keyword'>Enter keyword: </label>
                <input type='text' name='keyword' id='keyword' value='{0}'/>
                <br />
                <textarea name='message' id='message'>{1}</textarea>
                <br />
                <input type="submit" value="Vigenere!">
            </form>
'''

page_footer = '''
        </body>
    </html>
'''

@app.route('/', methods=['POST'])
def encrypt_page():
    keyword = cgi.escape(request.form['keyword'])
    for char in keyword:
        if char.isalpha() == False:
            error_msg = 'Keyword must only conatin latin letters.'
            return redirect('/?error={0}'.format(error_msg))


    message = request.form['message']
    secret_message = encrypt(message, keyword)
    return page_header + page_form.format(keyword, secret_message) + page_footer

@app.route("/")
def index():

    error = request.args.get("error")

    if error:
        error_esc = cgi.escape(error, quote=True)
        error_element = '<p class="error">' + error_esc + '</p>'
    else:
        error_element = ''

    return page_header + page_form.format('', '') + error_element + page_footer

app.run()
