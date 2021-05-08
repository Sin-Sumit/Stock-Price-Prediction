from flask import Flask, render_template, request
from model_1 import sarimax_model
from plotly.offline import plot
from plotly.graph_objs import Scatter
from flask import Markup
import datetime

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
@app.route("/results", methods=["POST","GET"])
def results():
    ticker = request.form['ticker']
    X = sarimax_model(ticker)
    # xlabel=[1999-11-18,1999-11-19,1999-11-20,1999-11-21,1999-11-22,1999-11-23,1999-11-24,1999-11-25,1999-11-26]
    xlabel=X[0]
    ylabel=X[1]
    da=X[2]
    # ylabel=[27.17,24.15,20.15,20.05,18.04,15.15,25.05,28.36,27.96]
    return render_template(
        "output.html",
        xlabel=xlabel,ylabel=ylabel,da=da
    )

if __name__=="__main__":
    app.run(debug=True)
