from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html', header="index", info="index" )

@app.route('/me_1')
def me_1():
    return render_template('me_1.html', header="me_1", info="me_1" )

@app.route('/me_2')
def me_2():
    return render_template('me_2.html', header="me_2", info="me_2" )

@app.route('/me_3')
def me_3():
    return render_template('me_3.html', header="me_3", info="me_3" )

@app.route('/me_4')
def me_4():
    return render_template('me_4.html', header="me_4", info="me_4" )