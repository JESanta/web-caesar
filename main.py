from flask import Flask, request
from caesar import rotate_string
app = Flask(__name__)
app.config['DEBUG'] = True
form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/" method = "post" target = "_self">
            <legend></legend>
            Rotate by: <input type="text" value=0 name="rot"><br>
            <textarea name="text">{0}
            </textarea><br>
            <input type="submit" value="Submit">
        </form>

    </body>
</html>
"""
@app.route("/")
def index():
    return form.format("")

@app.route('/', methods=['POST'])
def encrypt ():
    rot = int(request.form['rot'])
    rot_text = str(request.form['text'])
    encrypt_message = rotate_string(rot_text, rot)
    return form.format(encrypt_message)
    
app.run()