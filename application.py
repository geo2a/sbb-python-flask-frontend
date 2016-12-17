# -*- coding: utf-8 -*-

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
import json
import requests
from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

backend_endpoint = "http://54.213.202.245:8083/files"

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/students/<student_id>")
def student_files(student_id):
    payload = {'s_id': student_id}
    r = requests.get( backend_endpoint
                    , auth=('123', '123')
                    , params=payload)
    files = map(lambda x: hl(x['file']), json.loads(r.text))

    # code = files['contents']
    # lexer = get_lexer_by_name("pascal", stripall=True)
    # formatter = HtmlFormatter(linenos=True)
    # result = highlight(code, lexer, formatter)

    return render_template('files.html', files=files)
    # return result
    # return HtmlFormatter().get_style_defs('.highlight')

def hl(file):
    code = file
    lexer = get_lexer_by_name("pascal", stripall=True)
    formatter = HtmlFormatter(linenos=True)
    result = highlight(file['contents'], lexer, formatter)
    code['contents'] = result 
    return code   

if __name__ == "__main__":
    app.run()