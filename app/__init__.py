from flask            import Flask
from flask_bootstrap  import Bootstrap
from flask import render_template



app = Flask(__name__, static_url_path='/static')

# App main route + generic routing
@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path>')
def index(path):
    return render_template('layouts/default.html', content= render_template("/pages/index.html"))