from flask import Flask, redirect, render_template
from modules.reading import Data

app = Flask(__name__)


@app.route('/')
def main():
    d = Data()
    return render_template('index.html', df=d.data.to_dict(orient='records'))
