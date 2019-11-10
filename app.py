from flask import Flask, request, jsonify, render_template, redirect
from profanityfilter import ProfanityFilter

pf = ProfanityFilter()


def censor(text):
    '''censor all offensive words with *'''
    pf.set_censor("*")
    censored = pf.censor(text)
    return censored


app = Flask(__name__)


@app.route('/', methods=['GET'])
def homepage():
    return redirect('https://documenter.getpostman.com/view/9310664/SW18waDy?version=latest')


@app.route('/', methods=['POST'])
def censortext():
    """ Returns censored text """
    text = request.form['text']
    censored_text = censor(text)
    return jsonify(censored_text=censored_text)


if __name__ == '__main__':
    app.run(debug=True)
