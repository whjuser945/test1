import flask
from flask_cors import CORS
from flask import Flask
from main_hw import app_hw

app = Flask(__name__)
app.register_blueprint(app_hw)
app.config['TEMPLATES_AUTO_RELOAD'] = True
CORS(app)

@app.route('/index')
def index():
    return flask.send_from_directory('static', 'index.html')

@app.route('/ceshi')
def ceshi():
    return flask.send_from_directory('static', 'ceshi.html')
@app.route('/ceshi2')
def ceshi2():
    return flask.send_from_directory('static', 'ceshi2.html')

@app.route('/demodata')
def demodata():
    return flask.send_from_directory('static', 'demodata.csv')

@app.route('/barchart-tutorial')
def barcharttutorial():
    return flask.send_from_directory('static', 'd3-tutorial/barchart.html')

@app.route('/scatter-tutorial')
def scatter_tutorial():
    return flask.send_from_directory('static', 'd3-tutorial/scatter.html')

@app.route('/scatter-tutorial-simple')
def scatter_tutorial_simple():
    return flask.send_from_directory('static', 'd3-tutorial/scatter-simple.html')

@app.route('/static/<fname>')
def sendfile(fname):
    return flask.send_from_directory('static', fname)

# https://icon-icons.com/icon/heart-love-like-favourite-follow/131237
# https://icon-icons.com/icon/heart-love-favorite-favourite/13187
@app.route('/favicon.ico') 
def favicon(): 
    return flask.send_from_directory('static', 'loveheart.ico', mimetype='image/vnd.microsoft.icon')

app.run(host='0.0.0.0', port=11666, debug=True)
