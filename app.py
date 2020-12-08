import pandas as pd
from eganalyze import __version__
from eganalyze.lib import EgData
from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', version=__version__)
    if request.method == 'POST':
        df = pd.read_csv(request.files['file'].stream)
        data = EgData(df)
        return render_template('index.html', version=__version__, results=data)
